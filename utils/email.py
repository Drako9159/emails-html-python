import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# load credentials
def load_credentials():
    try:
        load_dotenv()
        email = os.getenv('EMAIL')
        password = os.getenv('PASSWORD')
        if not email or not password:
            raise ValueError("Email or password not found")
        return email, password
    except Exception as e:
        logging.error(f"An error occurred while loading credentials: {e}")
        return None, None

# load file html
def load_email_template(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"An loading template {file_path}: {e}")
        raise


class Email():
    def __init__(self):
        pass

    # send email
    def send_email(self, addressee, affair, html_file):
        
        sender, password = load_credentials()
        
        if sender is None:
            return

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = addressee
        msg['Subject'] = affair

        html = load_email_template(html_file)
        msg.attach(MIMEText(html, 'html'))

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, addressee, msg.as_string())
                server.quit()
                logging.info("Email sent successfully")
        except smtplib.SMTPException as e:
            logging.error(f"SMTP error occurred: {e}")
            raise
    
