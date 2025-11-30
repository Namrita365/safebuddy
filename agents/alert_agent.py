import time
import os

class AlertAgent:
    """
    Alert Agent:
    - Sends SOS alerts in case of emergency
    - Currently simulated; can integrate SMS or email APIs later
    """

    def __init__(self):
        pass

    def send_alert(self) -> str:
        """
        Simulate sending an alert
        """
        # Simulate processing time
        time.sleep(1)

        # Get emergency contact from environment variable (if set)
        contact = os.getenv("SAFEBUDDY_EMERGENCY_CONTACT", "No contact configured")
        return f"🚨 SOS Alert Sent! Emergency contact: {contact}"
