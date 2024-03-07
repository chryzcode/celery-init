
from rest_framework.decorators import api_view
from rest_framework.response import Response
from celery.result import AsyncResult
import json

# Create your views here.
import time
from .tasks import my_task, test_send_mail

@api_view(['POST'])
def my_vieww(request):
    result = my_task.delay(3, 5)
    final_result = result.get(timeout=1)
    # send_my_mail = test_send_mail()
    return Response({'hi':final_result})