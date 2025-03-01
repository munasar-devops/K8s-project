
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

today = datetime.today().date()

initial_start = datetime.combine(today, datetime.strptime("17:52", "%H:%M").time())

message_body = "Ramdan Kareem!\n\n"

for i in range(30):
    new_time = initial_start + timedelta(days=i, minutes=i)
    message_body += f"Day {i+1}: Maghrib pray is at: {new_time.strftime('%Y-%m-%d %H:%M')}\n\n"


# setting the SMTP server 
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Email configurations:
SENDER_EMAIL = "muneeh99@gmail.com"
RECEIVER_EMAIL = "muneeh99@gmail.com"
EMAIL_PASSWORD = "suni msnt vhuk yyav"

server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()  # Secure the connection
server.login(SENDER_EMAIL, EMAIL_PASSWORD)


def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# send the email notifcation 
send_email("Maghrib Prayer Time Notification", message_body)
