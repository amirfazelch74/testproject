import random
import string
import uuid
from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from users.sender import send_otp


# Create your models here.
class User(AbstractUser):
    # phone=models.TextField(max_length=20,blank=False)
    # is_verified=models.BooleanField(default=False)
    # smscode=models.SmallIntegerField(max_length=6)
    # active_code=models.BooleanField(default=False)
    # code_created=models.DateTimeField(auto_now_add=False)

    pass


class OtpRequestQueryset(models.QuerySet):
    def is_valid(self, reciever, request, password):
        current_time=timezone.now()
        return self.filter(
            reciever=reciever,
            request_id=request,
            password=password,
            created__lt=current_time,
            created__gt=current_time-timedelta(seconds=120)

        ).exists()


class Otpmanagement(models.Manager):
    def get_queryset(self):
        return OtpRequestQueryset(self.model, self._db)

    def is_valid(self, reciever, request, password):
        return self.get_queryset().is_valid(reciever, request, password)

    def generate(self, data):
        otp = self.model(channel=data['channel'], reciever=data['reciever'])
        otp.save(using=self._db)
        send_otp(otp)
        return otp


# class Otpmanagement (models.manager):
#     def generate (self, data):
#
#
#         return otp
def generate_otp():
    rand = random.SystemRandom()
    digits = rand.choices(string.digits, k=4)
    return ''.join(digits)


class OtpRequest(models.Model):
    class Otpchannel(models.TextChoices):
        PHONE = 'phone'
        EMAIL = 'e-mail'

    request_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    channel = models.CharField(max_length=10, choices=Otpchannel.choices, default=Otpchannel.PHONE)
    reciever = models.CharField(max_length=50)
    password = models.CharField(max_length=4, default=generate_otp)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    objects = Otpmanagement()
