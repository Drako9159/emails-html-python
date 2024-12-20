import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import argparse

# configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

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

# send email
def send_email(addressee, affair, html_file):
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

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description="Send email with a subject and a html file")
    parser.add_argument("-e", "--email", required=True, help="Recipient email address.")
    parser.add_argument("-s", "--subject", required=True, help="Subject of the email.")
    parser.add_argument("-f", "--file", required=True, help="Path to the HTML file to send.")

    args = parser.parse_args()

    try:
        send_email(args.email, args.subject, args.file)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

