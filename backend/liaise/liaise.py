from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import and_
from os import environ
from flask_cors import CORS
import json
from decimal import Decimal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


class Liaise(db.Model):
    __tablename__ = 'liaise'

    liaise_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    homework_id = db.Column(db.Integer, nullable=False)
    tutor_id = db.Column(db.Integer, nullable=False)
    offering = db.Column(db.Float(precision=2), nullable=False)
    status = db.Column(db.String(20), nullable=True, default='Pending')
    tutor_rating = db.Column(db.Integer, nullable=True)
    tutor_remark = db.Column(db.String(200), nullable=True)
    

    def __init__(self, liaise_id, homework_id, tutor_id, offering):
        self.liaise_id = liaise_id
        self.homework_id = homework_id
        self.tutor_id = tutor_id
        self.offering = offering
    
    def json(self):
        return {"liaise_id": self.liaise_id,
                "homework_id": self.homework_id,
                "tutor_id": self.tutor_id,
                "offering": self.offering,
                "status": self.status,
                "tutor_rating": self.tutor_rating,
                "tutor_remark": self.tutor_remark}

# Get All Liaise Offerings
@app.route("/liaise")
def get_all():
    liaise_list = Liaise.query.all()
    if len(liaise_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "liaisons": [liaise.json() for liaise in liaise_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no liaisons."
        }
    ), 404


# Get a Single Liaise Offering
@app.route("/liaise/<string:liaise_id>")
def find_by_liaise_id(liaise_id):
    liaison = Liaise.query.filter_by(liaise_id=liaise_id).first()
    if liaison:
        return jsonify(
            {
                "code": 200,
                "data": liaison.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Liaise not found."
        }
    ), 404


# Get All Liaise Offerings by Homework ID
@app.route("/liaise/liaiseByHomework/<string:homework_id>")
def get_homework_all(homework_id):
    liaise_list = Liaise.query.filter(and_(Liaise.homework_id == homework_id, Liaise.status == "Pending")).all()
    
    if liaise_list:
        return jsonify(
            {
                "code": 200,
                "liaisons": [liaise.json() for liaise in liaise_list]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Liaisons for this homework."
        }
    ), 404



# Get All Liaise Offerings by Homework ID
@app.route("/liaise/averageRating/<string:tutor_id>")
def get_average_rating(tutor_id):
    rating = db.session.query(func.avg(Liaise.tutor_rating)).filter_by(tutor_id=tutor_id).first()[0]

    if rating:
        return jsonify(
            {
                "code": 200,
                "average": str(rating)
            }
        )
    return jsonify(
        {
            "code": 200,
            "average": 0
        }
    ), 404

# Submit Liaise Offering
@app.route("/liaise/addLiaison", methods=['POST'])
def create_liaison():
    data = request.get_json()
    liaison = Liaise(None, **data)
    try:
        db.session.add(liaison)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the Liaison."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": liaison.json()
        }
    ), 201


# Delete Liaise Offering
@app.route("/liaise/deleteLiaison/<string:liaise_id>", methods=['DELETE'])
def delete_liaison(liaise_id):
    liaison = Liaise.query.filter_by(liaise_id=liaise_id).first()
    if liaison:
        db.session.delete(liaison)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "liaise_id": liaise_id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "liaise_id": liaise_id
            },
            "message": "Liaison not found."
        }
    )


# Accept Liaise Offering (Update 1 Accepted, the rest as Rejected)
@app.route("/liaise/accept/<string:liaise_id>/<string:homework_id>", methods=['PUT'])
def accept_liaison(liaise_id, homework_id):
    try:
        acceptLiaison = Liaise.query.filter_by(liaise_id=liaise_id).first()
        if not acceptLiaison:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "liase_id": liaise_id
                    },
                    "message": "Liaison not found"
                }
            ), 404
        acceptLiaison.status = "Accepted"
        db.session.commit()

        rejectLiaison = Liaise.query.filter_by(homework_id=homework_id, status="Pending").all()
        if rejectLiaison:
            for row in rejectLiaison:
                row.status = "Rejected"
            db.session.commit()
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    "liaise_id": liaise_id, 
                    "homework_id": homework_id
                }
            }
        ), 200

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "liaise_id": liaise_id
                },
                "message": "An error occurred while updating the Liaison. " + str(e)
            }
        ), 500


# Reject Liaise Offering
@app.route("/liaise/reject", methods=['PUT'])
def reject_liaison():
    data = request.get_json()
    if data['liaise_id']:
        liaise_id = data['liaise_id']
        try:
            rejectLiaison = Liaise.query.filter_by(liaise_id=liaise_id).first()
            if not rejectLiaison:
                return jsonify(
                    {
                        "code": 404,
                        "data": {
                            "liase_id": liaise_id
                        },
                        "message": "Liaison not found"
                    }
                ), 404
            
            rejectLiaison.status = "Rejected"
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": rejectLiaison.json()
                }
            ), 200

        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        "liaise_id": liaise_id
                    },
                    "message": "An error occurred while updating the Liaison. " + str(e)
                }
            ), 500
    else:
        return jsonify(
            {
                "code": 400,
                "message": "An error occurred while updating the Liaison"
            }
        ), 400


@app.route("/liaise/confirmHomework/<string:liaise_id>", methods=['PUT'])
def confirm_homework(liaise_id):
    try:
        liaise = Liaise.query.filter_by(liaise_id=liaise_id).first()
        if not liaise:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "liaise_id": liaise
                    },
                    "message": "Liaise not found."
                }
            ), 404
        data = request.get_json()
        if data['status'] and data['tutor_rating'] and data['tutor_remark']:
            liaise.status = "Confirm"
            liaise.tutor_rating = data['tutor_rating']
            liaise.tutor_remark = data['tutor_remark']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": liaise.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "liaise": liaise_id
                },
                "message": "An error occurred while updating the liaise. " + str(e)
            }
        ), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=True)