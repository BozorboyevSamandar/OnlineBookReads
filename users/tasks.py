from django.core.mail import send_mail
from onlinebook.celery import app

@app.task()
def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        "samandarbozorboyev29@gmail.com",
        recipient_list
    )
