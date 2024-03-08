
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from .tasks import test_send_mail

# Create your views here.


@api_view(['POST'])
def my_vieww(request):
    # test_send_mail()
    return Response({'hi':'hello'})