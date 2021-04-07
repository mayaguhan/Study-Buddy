from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ

import requests
from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

user_URL = environ.get('user_URL') or "http://user:5000/user"
homework_URL = environ.get('homework_URL') or "http://homework:5100/homework"
liaise_URL = environ.get('liaise_URL') or "http://liaise:5200/liaise"


# Get All Liaise Detail
@app.route("/liaise_detail")
def get_liaise_detail():
    try:
        result = retrieveLiaiseDetailAll()
        return jsonify(result), result['code']
        
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
        print(ex_str)

        return jsonify({
            "code": 500,
            "message": "liaise_detail.py internal error: " + ex_str
        }), 500
    
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " +str(request.get_data())
    })


# Get All Liaise Detail by Homework Id
@app.route("/liaise_detail/homework_id/<string:homework_id>")
def liaise_detail_by_homework_id(homework_id):
    if homework_id:
        try:
            result = retrieveLiaiseDetail(homework_id)
            return jsonify(result), result['code']
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "liaise_detail.py internal error: " + ex_str
            }), 500
    
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " +str(request.get_data())
    })


# Get All Liaise Detail by Liaise Id
@app.route("/liaise_detail/liaise_id/<string:liaise_id>")
def liaise_detail_by_liaise_id(liaise_id):
    if liaise_id:
        try:
            result = retrieveLiaiseDetailByLiaiseId(liaise_id)
            return jsonify(result), result['code']
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "liaise_detail.py internal error: " + ex_str
            }), 500
    
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " +str(request.get_data())
    })


# Get All Liaise Detail by User Id
@app.route("/liaise_detail/user_id/<string:user_id>/<string:role>")
def liaise_detail_by_user_id(user_id, role):
    if user_id:
        try:
            if role == "student":
                result = retrieveLiaiseDetailByUserIdStudent(user_id)
            elif role == "tutor":
                result = retrieveLiaiseDetailByUserIdTutor(user_id)
            return jsonify(result), result['code']
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "liaise_detail.py internal error: " + ex_str
            }), 500
    
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " +str(request.get_data())
    })




# Get All Liaise Detail
def retrieveLiaiseDetailAll():
    # Invoke Liaise Microservice to retrieve homework_id
    liaisons_result = invoke_http(liaise_URL, method='GET')
    liaisons_code = liaisons_result["code"]

    if liaisons_code not in range(200,300):
        print("\n-----Publishing the Liaise error message with routing_key=liaise.error-----")
        message = json.dumps(liaisons_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="liaise.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nLiaise Error ({:d}) published to the RabbitMQ Exchange:".format(liaisons_code), liaisons_result)
        return {
            "code": 500,
            "data": {"liaise_result": liaisons_result},
            "message": "Liaise has been sent for error handling"
        }

    if len(liaisons_result["data"]["liaisons"]) > 0:
        for liaise in liaisons_result["data"]["liaisons"]:
            homework_id = liaise["homework_id"]

            # Invoke Homework Microservice to retrieve homework detail
            homework_result = invoke_http(homework_URL + '/' + str(homework_id), method='GET')
            homework_code = homework_result["code"]

            if homework_code not in range(200,300):
                print("\n-----Publishing the Homework error message with routing_key=homework.error-----")
                message = json.dumps(homework_result)
                amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="homework.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
                print("\nHomework Error ({:d}) published to the RabbitMQ Exchange:".format(homework_code), homework_result)
                return {
                    "code": 500,
                    "data": {"homework_result": homework_result},
                    "message": "Homework has been sent for error handling"
                }
            homework_detail = homework_result["data"]
            tutor_id = liaise["tutor_id"]
            student_id = homework_result["data"]["student_id"]


            # Invoke User Microservice to retrieve Tutor detail
            tutor_result = invoke_http(user_URL + '/user_id/' + str(tutor_id), method='GET')
            tutor_code = tutor_result["code"]

            if tutor_code not in range(200,300):
                print("\n-----Publishing the User error message with routing_key=user.error-----")
                message = json.dumps(tutor_result)
                amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="user.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
                print("\nUser Error ({:d}) published to the RabbitMQ Exchange:".format(tutor_code), tutor_result)
                return {
                    "code": 500,
                    "data": {"tutor_result": tutor_result},
                    "message": "User has been sent for error handling"
                }
            tutor_detail = tutor_result["data"]


            # Invoke User Microservice to retrieve Student detail
            student_result = invoke_http(user_URL + '/user_id/' + str(student_id), method='GET')
            student_code = student_result["code"]

            if student_code not in range(200,300):
                print("\n-----Publishing the User error message with routing_key=user.error-----")
                message = json.dumps(student_result)
                amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="user.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
                print("\nUser Error ({:d}) published to the RabbitMQ Exchange:".format(student_code), student_result)
                return {
                    "code": 500,
                    "data": {"student_result": student_result},
                    "message": "User has been sent for error handling"
                }
            student_detail = student_result["data"]

            liaise["homework"] = homework_detail
            liaise["student"] = student_detail
            liaise["tutor"] = tutor_detail
    else:
        return jsonify(
        {
            "code": 404,
            "message": "There are no liaisons."
        }), 404 

    return {
        "code": 201,
        "data": {
            "liaisons_result" : liaisons_result
        }
    }


# Get All Liaise Detail by Homework Id
def retrieveLiaiseDetail(homework_id):
    return_list = []

    # Invoke Liaise Microservice to retrieve tutor_id
    liaisons_result = invoke_http(liaise_URL + '/liaiseByHomework/' + str(homework_id) + '/Pending', method='GET')
    liaisons_code = liaisons_result["code"]

    if liaisons_code not in range(200,300):
        print("\n-----Publishing the Liaise error message with routing_key=liaise.error-----")
        message = json.dumps(liaisons_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="liaise.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nLiaise Error ({:d}) published to the RabbitMQ Exchange:".format(liaisons_code), liaisons_result)
        return {
            "code": 500,
            "data": {"liaise_result": liaisons_result},
            "message": "Liaise has been sent for error handling"
        }

    if len(liaisons_result["liaisons"]) > 0:
        for liaise in liaisons_result["liaisons"]:
            tutor_id = liaise["tutor_id"]
            
            # Invoke User Microservice to retrieve Tutor detail
            tutor_result = invoke_http(user_URL + '/user_id/' + str(tutor_id), method='GET')
            tutor_code = tutor_result["code"]

            if tutor_code not in range(200,300):
                print("\n-----Publishing the User error message with routing_key=user.error-----")
                message = json.dumps(tutor_result)
                amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="user.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
                print("\nUser Error ({:d}) published to the RabbitMQ Exchange:".format(tutor_code), tutor_result)
                return {
                    "code": 500,
                    "data": {"tutor_result": tutor_result},
                    "message": "User has been sent for error handling"
                }


            # Invoke User Microservice to retrieve Tutor rating
            tutor_rating_result = invoke_http(liaise_URL + '/averageRating/' + str(tutor_id), method='GET')
            tutor_rating_code = tutor_rating_result["code"]
            if tutor_rating_code not in range(200,300):
                print("\n-----Publishing the User error message with routing_key=user.error-----")
                message = json.dumps(tutor_rating_result)
                amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="user.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
                print("\nUser Error ({:d}) published to the RabbitMQ Exchange:".format(tutor_rating_code), tutor_rating_result)
                return {
                    "code": 500,
                    "data": {"tutor_rating_result": tutor_rating_result},
                    "message": "User has been sent for error handling"
                }
            tutor_result["data"]["rating"] = tutor_rating_result["average"]
            tutor_result["data"]["tutor_id"] = liaise["tutor_id"]
            tutor_result["data"]["liaise_id"] = liaise["liaise_id"]
            tutor_result["data"]["homework_id"] = liaise["homework_id"]
            tutor_result["data"]["offering"] = liaise["offering"]
            tutor_result["data"]["status"] = liaise["status"]
            return_list.append(tutor_result)

    return {
        "code": 201,
        "data": {
            "liaisons_result" : return_list
        }
    }


# Get All Liaise Detail by Liaise Id
def retrieveLiaiseDetailByLiaiseId(liaise_id):
    # Invoke Liaise Microservice to retrieve homework_id & tutor_id
    liaisons_result = invoke_http(liaise_URL + "/" + str(liaise_id), method='GET')
    liaisons_code = liaisons_result["code"]

    if liaisons_code not in range(200,300):
        print("\n-----Publishing the Liaise error message with routing_key=liaise.error-----")
        message = json.dumps(liaisons_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="liaise.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nLiaise Error ({:d}) published to the RabbitMQ Exchange:".format(liaisons_code), liaisons_result)
        return {
            "code": 500,
            "data": {"liaise_result": liaisons_result},
            "message": "Liaise has been sent for error handling"
        }

    if len(liaisons_result["data"]) > 0:
        tutor_id = liaisons_result["data"]["tutor_id"]
        homework_id = liaisons_result["data"]["homework_id"]

        # Invoke Homework Microservice to retrieve homework detail
        homework_result = invoke_http(homework_URL + '/' + str(homework_id), method='GET')
        homework_code = homework_result["code"]

        if homework_code not in range(200,300):
            print("\n-----Publishing the Homework error message with routing_key=homework.error-----")
            message = json.dumps(homework_result)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="homework.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("\nHomework Error ({:d}) published to the RabbitMQ Exchange:".format(homework_code), homework_result)
            return {
                "code": 500,
                "data": {"homework_result": homework_result},
                "message": "Homework has been sent for error handling"
            }
        student_id = homework_result["data"]["student_id"]
        liaisons_result["data"]["homework_title"] = homework_result["data"]["title"]
        liaisons_result["data"]["homework_description"] = homework_result["data"]["description"]
        liaisons_result["data"]["homework_subject"] = homework_result["data"]["subject"]
        liaisons_result["data"]["homework_image"] = homework_result["data"]["image"]
        liaisons_result["data"]["student_id"] = student_id


        # Invoke User Microservice to retrieve Tutor detail
        tutor_result = invoke_http(user_URL + '/user_id/' + str(tutor_id), method='GET')
        tutor_code = tutor_result["code"]
        if tutor_code not in range(200,300):
            print("\n-----Publishing the User error message with routing_key=user.error-----")
            message = json.dumps(tutor_result)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="user.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("\nUser Error ({:d}) published to the RabbitMQ Exchange:".format(tutor_code), tutor_result)
            return {
                "code": 500,
                "data": {"tutor_result": tutor_result},
                "message": "User has been sent for error handling"
            }
        liaisons_result["data"]["tutor_username"] = tutor_result["data"]["username"]
        liaisons_result["data"]["tutor_contact"] = tutor_result["data"]["contact"]
        liaisons_result["data"]["tutor_email"] = tutor_result["data"]["email"]
        liaisons_result["data"]["tutor_telegram_id"] = tutor_result["data"]["telegram_id"]
        liaisons_result["data"]["tutor_photo"] = tutor_result["data"]["photo"]


        # Invoke User Microservice to retrieve Student detail
        student_result = invoke_http(user_URL + '/user_id/' + str(student_id), method='GET')
        student_code = student_result["code"]
        if student_code not in range(200,300):
            print("\n-----Publishing the User error message with routing_key=user.error-----")
            message = json.dumps(student_result)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="user.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("\nUser Error ({:d}) published to the RabbitMQ Exchange:".format(student_code), student_result)
            return {
                "code": 500,
                "data": {"student_result": student_result},
                "message": "User has been sent for error handling"
            }
        liaisons_result["data"]["student_username"] = student_result["data"]["username"]
        liaisons_result["data"]["student_contact"] = student_result["data"]["contact"]
        liaisons_result["data"]["student_email"] = student_result["data"]["email"]
        liaisons_result["data"]["student_telegram_id"] = student_result["data"]["telegram_id"]
        liaisons_result["data"]["student_photo"] = student_result["data"]["photo"]

    return {
        "code": 201,
        "data": liaisons_result
    }


# Get All Liaise Detail by User Id
def retrieveLiaiseDetailByUserIdTutor(user_id):
    return_list = []
    # Invoke Liaise Microservice to retrieve homework_id
    liaisons_result = invoke_http(liaise_URL + "/liaiseByUserId/" + str(user_id), method='GET')
    liaisons_code = liaisons_result["code"]

    if liaisons_code not in range(200,300):
        print("\n-----Publishing the Liaise error message with routing_key=liaise.error-----")
        message = json.dumps(liaisons_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="liaise.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nLiaise Error ({:d}) published to the RabbitMQ Exchange:".format(liaisons_code), liaisons_result)
        return {
            "code": 500,
            "data": {"liaise_result": liaisons_result},
            "message": "Liaise has been sent for error handling"
        }

    if len(liaisons_result["liaisons"]) > 0:
        for liaison in liaisons_result["liaisons"]:
            homework_id = liaison['homework_id']
            # Invoke Homework Microservice to retrieve homework_id
            homework_result = invoke_http(homework_URL + '/' + str(homework_id), method='GET')
            homework_code = homework_result["code"]

            if homework_code not in range(200,300):
                print("\n-----Publishing the Homework error message with routing_key=homework.error-----")
                message = json.dumps(homework_result)
                amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="homework.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
                print("\nHomework Error ({:d}) published to the RabbitMQ Exchange:".format(homework_code), homework_result)
                return {
                    "code": 500,
                    "data": {"homework_result": homework_result},
                    "message": "Homework has been sent for error handling"
                }
            student_id = homework_result["data"]["student_id"]
            liaison["student_id"] = student_id
            liaison["title"] = homework_result["data"]["title"]
            liaison["description"] = homework_result["data"]["description"]
            liaison["image"] = homework_result["data"]["image"]

            # Invoke User Microservice to retrieve Student detail
            student_result = invoke_http(user_URL + '/user_id/' + str(student_id), method='GET')
            student_code = student_result["code"]
            if student_code not in range(200,300):
                print("\n-----Publishing the User error message with routing_key=user.error-----")
                message = json.dumps(student_result)
                amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="user.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
                print("\nUser Error ({:d}) published to the RabbitMQ Exchange:".format(student_code), student_result)
                return {
                    "code": 500,
                    "data": {"student_result": student_result},
                    "message": "User has been sent for error handling"
                }
            liaison["student_username"] = student_result["data"]["username"]
            liaison["student_telegram_id"] = student_result["data"]["telegram_id"]

            return_list.append(liaison)
    return {
        "code": 201,
        "data": return_list
    }

# Get All Liaise Detail by User Id
def retrieveLiaiseDetailByUserIdStudent(user_id):
    return_list = []
    # Invoke Homework microservice to retrieve all homeworks by student
    homework_result = invoke_http(homework_URL + '/homeworkByStudentIdStatus/' + str(user_id) + '/Progress', method='GET')
    homework_code = homework_result["code"]

    if homework_code not in range(200,300):
        print("\n-----Publishing the Homework error message with routing_key=homework.error-----")
        message = json.dumps(homework_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="homework.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nHomework Error ({:d}) published to the RabbitMQ Exchange:".format(homework_code), homework_result)
        return {
            "code": 500,
            "data": {"homework_result": homework_result},
            "message": "Homework has been sent for error handling"
        }
    
    if len(homework_result["homework"]) > 0:
        for homework in homework_result["homework"]:
            homework_id = homework["homework_id"]
            
            # Invoke Liaise Microservice to retrieve all accepted liaise of this homework
            tutor_liaise_result = invoke_http(liaise_URL + "/liaiseByHomework/" + str(homework_id) + '/Accept', method='GET')
            tutor_liaise_code = tutor_liaise_result["code"]

            if tutor_liaise_code not in range(200,300):
                print("\n-----Publishing the Liaise error message with routing_key=liaise.error-----")
                message = json.dumps(tutor_liaise_result)
                amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="liaise.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
                print("\nLiaise Error ({:d}) published to the RabbitMQ Exchange:".format(tutor_liaise_code), tutor_liaise_result)
                return {
                    "code": 500,
                    "data": {"liaise_result": tutor_liaise_result},
                    "message": "Liaise has been sent for error handling"
                }
            tutor_id = tutor_liaise_result["liaisons"][0]["tutor_id"]

            # Invoke User Microservice to retrieve tutor detail
            tutor_result = invoke_http(user_URL + '/user_id/' + str(tutor_id), method='GET')
            tutor_code = tutor_result["code"]

            if tutor_code not in range(200,300):
                print("\n-----Publishing the User error message with routing_key=user.error-----")
                message = json.dumps(tutor_result)
                amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="user.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
                print("\nUser Error ({:d}) published to the RabbitMQ Exchange:".format(tutor_code), tutor_result)
                return {
                    "code": 500,
                    "data": {"tutor_result": tutor_result},
                    "message": "User has been sent for error handling"
                }
            homework["telegram_id"] = tutor_result["data"]["telegram_id"]
            homework["username"] = tutor_result["data"]["username"]

            return_list.append(homework)

    return {
        "code": 201,
        "data": return_list
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5600, debug=True)