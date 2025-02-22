# config.py
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load Google Sheets API credentials
with open(os.path.join("credentials", "google_credentials.json")) as f:
    GOOGLE_CREDENTIALS = json.load(f)

# Load SMTP credentials
with open(os.path.join("credentials", "smtp_credentials.json")) as f:
    SMTP_CREDENTIALS = json.load(f)

# Google Sheets configuration
SPREADSHEET_NAME = "Appointment Logs"
WORKSHEET_NAME = "Sheet1"

# SMTP Email configuration
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))  # Convert port to integer
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

# Vapi API configuration
VAPI_API_KEY = os.getenv("VAPI_API_KEY")