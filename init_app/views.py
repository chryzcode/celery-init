
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import your_task, test_send_mail
from datetime import datetime, timedelta

# Create your views here.


@api_view(['POST'])
def my_vieww(request):
    your_task()
    # eta_time = datetime.utcnow() + timedelta(minutes=1)
    # test_send_mail.apply_async(eta=eta_time)
    test_send_mail()
    return Response({'hi':'hello'})