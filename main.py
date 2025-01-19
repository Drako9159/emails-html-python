#!/usr/bin/env python3
import logging
import argparse
from utils.email import Email

# configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

email = Email()

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description="Send email with a subject and a html file")
    parser.add_argument("-e", "--email", required=True, help="Recipient email address.")
    parser.add_argument("-s", "--subject", required=True, help="Subject of the email.")
    parser.add_argument("-f", "--file", required=True, help="Path to the HTML file to send.")

    args = parser.parse_args()

    try:
        email.send_email(args.email, args.subject, args.file)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
