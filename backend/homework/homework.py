from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
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
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.String(20), nullable=True, default='Unsolved')

    def __init__(self, homework_id, student_id, subject, title, description, price, deadline):
        self.homework_id = homework_id
        self.student_id = student_id
        self.subject = subject
        self.title = title
        self.description = description
        self.price = price
        self.deadline = deadline

    def json(self):
        return {"homework_id": self.homework_id, 
                "student_id": self.student_id, 
                "subject": self.subject, 
                "title": self.title, 
                "description": self.description, 
                "price": self.price, 
                "deadline": self.deadline, 
                "created": self.created,
                "status": self.status}


@app.route("/homework")
def get_all():
    homeworklist = Homework.query.all()
    if len(homeworklist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "homeworks": [homework.json() for homework in homeworklist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no homeworks."
        }
    ), 404


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
@app.route("/homework/<string:homework_id>", methods=['PUT'])
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
                    "order_id": order_id
                },
                "message": "An error occurred while updating the order. " + str(e)
            }
        ), 500







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=True)