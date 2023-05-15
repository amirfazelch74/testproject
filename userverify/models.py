from django.db import models

# Create your models here.
class Userverify(models.Model):
    phone=models.TextField(max_length=20,blank=True)
    is_verified=models.BooleanField(default=False)
    smscode=models.SmallIntegerField()
    active_code=models.BooleanField(default=False)
    pass