from django.urls import path
from .views import OtpView
urlpatterns=[
    path('otp',OtpView.as_view(),name='otpview')

]