from celery import shared_task
from django.core.mail import send_mail



# Define your task
@shared_task(bind = True)
def test(data):
    print(f'Hello, {data}')



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




