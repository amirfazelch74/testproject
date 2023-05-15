from django.shortcuts import render

from djangoProject.forms import Sms_login


def phone_login(request):
    sms_login = Sms_login(request.POST or None)
    if sms_login.is_valid():

# Create your views here.
