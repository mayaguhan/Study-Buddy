from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from datetime import timedelta
from os import environ
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Homework(db.Model):
    __tablename__ = 'homework'

    homework_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.String(11), nullable=False)
    subject = db.Column(db.String(20), nullable=False)
    meeting_type = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.String(20), nullable=True, default='Unsolve')

    def __init__(self, homework_id, student_id, subject, meeting_type, title, description, price, image, deadline):
        self.homework_id = homework_id
        self.student_id = student_id
        self.subject = subject
        self.meeting_type = meeting_type
        self.title = title
        self.description = description
        self.price = price
        self.image = image
        self.deadline = deadline

    def json(self):
        return {"homework_id": self.homework_id, 
                "student_id": self.student_id, 
                "subject": self.subject, 
                "meeting_type": self.meeting_type,
                "title": self.title, 
                "description": self.description, 
                "price": self.price, 
                "image": self.image, 
                "deadline": self.deadline, 
                "created": self.created,
                "status": self.status}


# Get All Homework
@app.route("/homework")
def get_all():
    homework_list = Homework.query.all()
    if len(homework_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "homeworks": [homework.json() for homework in homework_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no homeworks."
        }
    ), 404


# Get All Available Homework
@app.route("/homework/availableHomework/<string:student_id>")
def get_all_available(student_id):
    todays_datetime = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
    homework_list = Homework.query.filter(and_(Homework.student_id != student_id, Homework.status == "Unsolve", Homework.deadline > todays_datetime)).all()
    print(homework_list)
    if len(homework_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "homeworks": [homework.json() for homework in homework_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no homeworks."
        }
    ), 404

# Get a Single Homework
@app.route("/homework/<string:homework_id>")
def find_by_homework_id(homework_id):
    homework = Homework.query.filter_by(homework_id=homework_id).first()
    if homework:
        return jsonify(
            {
                "code": 200,
                "data": homework.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Homework not found."
        }
    ), 404


# Get All Homework by Status
@app.route("/homework/homeworkByStatus/<string:status>")
def get_homework_status(status):
    homework_list = Homework.query.filter_by(status=status).all()
    if homework_list:
        return jsonify(
            {
                "code": 200,
                "homework": [homework.json() for homework in homework_list]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no homework for this status."
        }
    ), 404


# Get All Homework by Student Id
@app.route("/homework/homeworkByStudentId/<string:student_id>")
def get_homework_student(student_id):
    homework_list = Homework.query.filter_by(student_id=student_id).all()
    if homework_list:
        return jsonify(
            {
                "code": 200,
                "homework": [homework.json() for homework in homework_list]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no homework for this user."
        }
    ), 404



# Get All Homework by Student Id and Status
@app.route("/homework/homeworkByStudentIdStatus/<string:student_id>/<string:status>")
def get_homework_student_status(student_id, status):
    homework_list = Homework.query.filter_by(student_id=student_id, status=status).all()
    if homework_list:
        return jsonify(
            {
                "code": 200,
                "homework": [homework.json() for homework in homework_list]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no homework of this status for this user."
        }
    ), 404


# Add a Homework
@app.route("/homework/addHomework", methods=['POST'])
def create_homework():
    data = request.get_json()
    homework = Homework(None, **data)
    try:
        db.session.add(homework)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the homework."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": homework.json()
        }
    ), 201


# Delete a Homework
@app.route("/homework/<string:homework_id>", methods=['DELETE'])
def delete_homework(homework_id):
    homework = Homework.query.filter_by(homework_id=homework_id).first()
    if homework:
        db.session.delete(homework)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "homework_id": homework_id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "homework_id": homework_id
            },
            "message": "Homework not found."
        }
    ), 404


#Update Homework Status
@app.route("/homework/updateStatus/<string:homework_id>", methods=['PUT'])
def update_status(homework_id):
    try:
        homework = Homework.query.filter_by(homework_id=homework_id).first()
        if not homework:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "homework_id": homework_id
                    },
                    "message": "Homework not found."
                }
            ), 404
        data = request.get_json()
        if data['status']:
            homework.status = data['status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": homework.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "homework": homework_id
                },
                "message": "An error occurred while updating the homework. " + str(e)
            }
        ), 500







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=True)