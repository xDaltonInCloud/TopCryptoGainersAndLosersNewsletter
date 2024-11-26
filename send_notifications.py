import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser
import logging

def send_email(subject, body, recipients):
    """Send email notifications."""
    config = configparser.ConfigParser()
    config.read("config.ini")

    sender_email = config["email"]["sender"]
    sender_password = config["email"]["password"]
    smtp_server = config["email"]["smtp_server"]
    smtp_port = config["email"]["smtp_port"]

    try:
        with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            for recipient in recipients:
                msg = MIMEMultipart()
                msg["From"] = sender_email
                msg["To"] = recipient
                msg["Subject"] = subject
                msg.attach(MIMEText(body, "plain"))
                server.sendmail(sender_email, recipient, msg.as_string())
                logging.info(f"Email sent to {recipient}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        raise
