from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User,OtpRequest

# Register your models here.
admin.site.register(OtpRequest)
@admin.register(User)
class AppUserAdmin(UserAdmin):
    pass