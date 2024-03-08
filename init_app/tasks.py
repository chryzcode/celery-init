from celery import shared_task
from django.core.mail import send_mail



# Define your task
@shared_task(bind = True)
def test():
    print('Hello')



@shared_task
def test_send_mail():
    send_mail(
        subject = "A Test",
        message = "",
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = ['chryzalaba2003@gmail.com',],
        html_message=f"""
       <h3> Hello, </h3>
       <p>
       How you doing
        </br> See you later
        </p>
        """,
        fail_silently=False,
    )
    print("Your task is executed after 30 seconds")


celery.conf.beat_schedule = {
    'send-email-every-day': {
        'task': 'tasks.test_send_mail',
        'schedule': crontab(minute=1),  # Adjust the time as per your requirement
        # 'args': ('Subject', 'Message', ['recipient@example.com']),
    },
}




