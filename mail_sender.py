import smtplib
from email.mime.text import MIMEText
from datetime import date
from trening import generirani_trening
import os
from dotenv import load_dotenv

load_dotenv()

def lambda_handler(event, context):
    datum = date.today()
    datum_danas = datum.strftime("%d/%m/%Y")

    subject = f"Današnji trening ({datum_danas})"
    body = f"{generirani_trening}"
    sender = os.getenv('GMAIL_USERNAME')
    recipients = ["vitostancec@gmail.com"]
    password = os.getenv('GMAIL_PASSWORD')

    def send_email(subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        print("Message sent!")

    send_email(subject, body, sender, recipients, password)