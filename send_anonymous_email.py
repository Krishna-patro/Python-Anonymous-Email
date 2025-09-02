import smtplib
from email.mime.text import MIMEText

sender_email = "no-reply@yourdomain.com"
recipient_email = "recipient_email@example.com"
smtp_server = "smtp.your_anonymous_service.com"
smtp_port = 587
service_username = "your_service_username"
service_password = "your_service_password"

def send_anonymous_email(recipient, subject, body):
    """
    Sends an email using a service that allows spoofing the sender's address.
    """
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(service_username, service_password)
            server.sendmail(service_username, recipient, msg.as_string())

        print("Anonymous email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    subject = "Hello from the Void"
    body = "This message was sent from a Python script without revealing the sender's true email address."
    send_anonymous_email(recipient_email, subject, body)
