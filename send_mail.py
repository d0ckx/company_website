import smtplib
import ssl
import os


def send_mail(message):
    webserver = "smtp.gmail.com"
    port = 465
    username = "dockxpython@gmail.com"
    password = os.getenv("COMPANY_PASSWORD")
    receiver_email = "dockxpython@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(webserver, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)