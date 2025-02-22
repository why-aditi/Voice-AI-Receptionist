# email_sender.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD

class EmailSender:
    def __init__(self):
        self.smtp_server = SMTP_SERVER
        self.smtp_port = SMTP_PORT
        self.sender_email = SENDER_EMAIL
        self.sender_password = SENDER_PASSWORD

    def send_email(self, to_email, appointment_details):
        """
        Send an appointment confirmation email.
        """
        subject = "Appointment Confirmation"
        body = f"""
        Hi {appointment_details['caller_name']},

        Your appointment has been confirmed for:
        Date: {appointment_details['appointment_date']}
        Time: {appointment_details['appointment_time']}

        Contact us at +1234567890 for any changes.

        Thank you!
        """

        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, to_email, msg.as_string())