# google_sheets.py
import gspread
from google.oauth2.service_account import Credentials
from config import GOOGLE_CREDENTIALS_PATH, SPREADSHEET_NAME, WORKSHEET_NAME

class GoogleSheetsHandler:
    def __init__(self):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_PATH, scopes=scope)
        self.client = gspread.authorize(creds)
        self.sheet = self.client.open(SPREADSHEET_NAME).worksheet(WORKSHEET_NAME)

    def log_call_data(self, call_data):
        """
        Log call data into Google Sheets.
        """
        row = [
            call_data["caller_name"],
            call_data["caller_number"],
            call_data["appointment_date"],
            call_data["appointment_time"],
            call_data["caller_email"]
        ]
        self.sheet.append_row(row)