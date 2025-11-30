# agents/alert_agent.py

import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables
load_dotenv()

class AlertAgent:
    def __init__(self):
        # Read Twilio credentials and emergency contact
        self.TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
        self.TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
        self.TWILIO_PHONE = os.getenv("TWILIO_PHONE")
        self.EMERGENCY_PHONE = os.getenv("EMERGENCY_PHONE")

        # Validate all credentials are present
        if not all([self.TWILIO_SID, self.TWILIO_AUTH_TOKEN, self.TWILIO_PHONE, self.EMERGENCY_PHONE]):
            raise ValueError("Twilio credentials or emergency phone are missing in .env")

        # Initialize Twilio client
        self.client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)

    def send_alert(self, user_location=None):
        """
        Sends an emergency SMS to the configured emergency contact.
        If user_location is provided, include it in the message.
        """
        try:
            msg_body = "🚨 Emergency! Help needed for a woman in danger."
            if user_location:
                msg_body += f" Location: {user_location}"

            message = self.client.messages.create(
                body=msg_body,
                from_=self.TWILIO_PHONE,
                to=self.EMERGENCY_PHONE
            )

            return f"🚨 SOS Alert Sent! Emergency contact: {self.EMERGENCY_PHONE}"

        except Exception as e:
            return f"Error sending alert: {str(e)}"
