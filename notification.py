from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class EmailSender:
    @staticmethod
    def send_email(symbol: str, current_price: float, previous_price: float) -> None:
        # Your email credentials
        sender_email: str = 'your_email@gmail.com'
        sender_password: str = 'your_password'
        receiver_email: str = 'recipient_email@example.com'

        # Create message container
        msg: MIMEMultipart = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f'{symbol} Stock Alert: Price Drop'

        # Email body
        body: str = f'The price of {symbol} has dropped from ${previous_price} to ${current_price} in the last ten minutes.'

        msg.attach(MIMEText(body, 'plain'))

        # Send email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            text: str = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

    @staticmethod
    def send_email_from_app(receiver_email: str, subject: str, body: str) -> None:
        try:
            # Predefined sender email address
            sender_email = 'stock_trader_noreply@example.com'
            
            # Create message container
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            # Email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to local SMTP server (no authentication required)
            server = smtplib.SMTP('localhost')

            # Send email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")