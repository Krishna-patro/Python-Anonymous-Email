# Python-Anonymous-Email
A conceptual script for sending emails with a custom sender address.
# Python Anonymous Email Sender (Conceptual)

This project provides a conceptual overview of how to send emails without revealing your primary email address. It explains the role of a third-party SMTP relay service in handling the delivery. The code demonstrates how the `From` header of an email can be set to a custom address, but it's crucial to understand that a service is required to handle the authentication and relay.

## Features
- Shows how to set a custom sender address.
- Provides a template for connecting to a relaying SMTP server.

## Requirements
- An account with a third-party SMTP service (e.g., Mailtrap, SendGrid).

## Usage
1. Sign up for a third-party SMTP relay service.
2. Open `send_anonymous_email.py`.
3. Replace the placeholder variables with your service credentials.
4. Run the script from your terminal.
