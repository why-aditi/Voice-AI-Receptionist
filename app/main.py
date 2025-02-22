# main.py
from vapi_handler import VapiHandler
from google_sheets import GoogleSheetsHandler
from email_sender import EmailSender

def main():
    # Initialize handlers
    vapi_handler = VapiHandler()
    google_sheets_handler = GoogleSheetsHandler()
    email_sender = EmailSender()

    # Simulate incoming call data (replace with actual Vapi API call)
    call_data = {
        "caller_name": "John Doe",
        "caller_number": "+1234567890",
        "appointment_date": "2023-10-15",
        "appointment_time": "10:00 AM",
        "caller_email": "john.doe@example.com"
    }

    # Handle the call
    processed_data = vapi_handler.handle_call(call_data)

    # Log call data into Google Sheets
    google_sheets_handler.log_call_data(processed_data)

    # Send email confirmation
    if processed_data.get("caller_email"):
        email_sender.send_email(processed_data["caller_email"], processed_data)

if __name__ == "__main__":
    main()