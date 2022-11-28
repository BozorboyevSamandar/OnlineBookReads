from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser

# @receiver(post_save, sender=CustomUser)
# def send_email(sender, instance, created, **kwargs):
# send email
# if created:
#     send_mail(
#         "Welcome to OnlineBook website"
#         f"Hi, {user.username}. Welcome to onlinebook website. Enjoy the books and reviews."
#         "samandarbozorboyev29@gmail.com",
#         [user.email]
#     )
