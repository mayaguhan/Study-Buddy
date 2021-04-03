from flask import Flask, request, jsonify
from os import environ
from flask_cors import CORS
from datetime import datetime

# Import SendGrid Dependencies
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

CORS(app)

# Send Email
@app.route("/notification/email", methods=['POST'])
def send_notification():
    data = request.get_json()

    # emailSubject = "Offer Acceptance from " + data["tutor_name"]
    # emailContent = "You have accepted an offer from " + data["tutor_name"] + " for " + data["homework_title"] + "."

    message = Mail(
        from_email= 'studybuddyapp@outlook.com',
        to_emails= data["receiver"],
        subject= data["subject"],
        html_content= data["content"])
    try:
        sendgrid_client = SendGridAPIClient('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')
        response = sendgrid_client.send(message)
        return jsonify(
            {
            "code": 200,
            "message": "Successfully sent email"
            }
        )
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": e
            }
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800, debug=True)