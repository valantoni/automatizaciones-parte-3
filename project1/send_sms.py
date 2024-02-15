from twilio.rest import Client
import os
from dotenv import load_dotenv

def send_sms(message, recipient_phone_number):
    try:
        # Load environment variables
        load_dotenv()
        # Twilio credentials
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
        # Create a Twilio client
        client = Client(account_sid, auth_token,recipient_phone_number)
        # Send SMS
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )
        print(f"SMS sent successfully! SID: {message.sid}")

    except Exception as e:
        raise ValueError(e + "Error sending SMS")


