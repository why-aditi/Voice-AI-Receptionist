# vapi_handler.py
import requests
from config import VAPI_API_KEY

class VapiHandler:
    def __init__(self):
        self.base_url = "https://api.vapi.ai/v1"
        self.headers = {
            "Authorization": f"Bearer {VAPI_API_KEY}",
            "Content-Type": "application/json"
        }

    def handle_call(self, call_data):
        """
        Handle incoming call data from Vapi.
        """
        # Extract relevant data from the call
        caller_name = call_data.get("caller_name")
        caller_number = call_data.get("caller_number")
        appointment_date = call_data.get("appointment_date")
        appointment_time = call_data.get("appointment_time")
        caller_email = call_data.get("caller_email")

        # Process the call data (e.g., check availability, confirm booking)
        # For now, we'll just return the extracted data
        return {
            "caller_name": caller_name,
            "caller_number": caller_number,
            "appointment_date": appointment_date,
            "appointment_time": appointment_time,
            "caller_email": caller_email
        }