import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# load credentials
def load_credentials():
    try:
        load_dotenv()
        return os.getenv('EMAIL'), os.getenv('PASSWORD')
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

# load file html
def load_email_template(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

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
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    try:
        send_email("mail@mail.com", "Test", "email.html")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

