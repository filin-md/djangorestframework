from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_course_update_notification(user_email, course_title):
    subject = 'Обновление курса'
    message = f'Здравствуйте! Курс {course_title} был обновлен.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)