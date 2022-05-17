from celery import shared_task
from school_registration_system import settings
from .models import Teacher
from django.core.mail import send_mail
from school_registration_system import celery

@celery.app.task
def mail_send_function():
    print("Hello###########################################################")
    teacher = Teacher.objects.filter(is_student=False)
    for i in teacher:
        mail_subject = "Hi!!!! We are testing Celery"
        meassage = "This is Celery Testing. Only Printed mails are send here."
        to_email = i.email
        send_mail(
            subject= mail_subject,
            message = meassage,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently= True,
        )
    return "Done"
