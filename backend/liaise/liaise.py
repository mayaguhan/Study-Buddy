from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

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
    status = db.Column(db.String(20), nullable=True, default='pending')

    def __init__(self, liaise_id, homework_id, tutor_id, offering, status):
        self.liaise_id = liaise_id
        self.homework_id = homework_id
        self.tutor_id = tutor_id
        self.offering = offering
        self.status = status
    
    def json(self):
        return {"liaise_id": self.liaise_id,
                "homework_id": self.homework_id,
                "tutor_id": self.tutor_id,
                "offering": self.offering,
                "status": self.status}


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
            "message": "Homework not found."
        }
    ), 404


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


@app.route("/liaise/<string:liaise_id>", methods=['PUT'])
def update_liaison(liaise_id):
    try:
        liaison = Liaise.query.filter_by(liaise_id=liaise_id).first()
        if not liaison:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "liase_id": liaise_id
                    },
                    "message": "Liaison not found"
                }
            ), 404

        
        # Liaise id is found and time to update

        data = request.get_json()
        if data['status']:
            liaison.status = data['status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": liaison.json()
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





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=True)