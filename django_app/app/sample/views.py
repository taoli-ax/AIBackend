from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.http import JsonResponse
from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
