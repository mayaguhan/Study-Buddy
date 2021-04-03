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
@app.route("/notification")
def send_notification():
    print("A")
    message = Mail(
        from_email='studybuddyapp@outlook.com',
        to_emails='studybuddyapp@outlook.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    print(message)
    try:
        sendgrid_client = SendGridAPIClient('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')
        response = sendgrid_client.send(message)
        ###
        print("Hello")
        ###
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800, debug=True)