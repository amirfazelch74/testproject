from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from sms_ir import SmsIr
from . import serializers
from .models import OtpRequest


# Create your views here.
class OtpView(APIView):
    def get(self, requset):
        serializer = serializers.RequsetOtpserializer(data=requset.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            otp = OtpRequest.objects.generate(data)
            print(otp)
            try:
                print(Response(data=serializers.RequestOtpResponsserializer(otp).data))
                return Response(data=serializers.RequestOtpResponsserializer(otp).data)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def post(self, request):
        serializer=serializers.Verifyotprequestserializer(data=request.data)
        if serializer.is_valid():
            data=serializer.validated_data

            if OtpRequest.objects.is_valid(data['reciever'],data['request_id'],data['password']):
                return Response(self._handle_login(data))
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def _handle_login(self,otp):
        User=get_user_model()
        query=User.objects.filter(username=otp['reciever'])
        if query.exists():
            created=True
            user=query.first()
        else:
            user=User.objects.create(username=otp['reciever'])
            created=False
        refresh=RefreshToken.for_user(User)
        return serializers.ObtainTokenserializer({
            'refresh':str(refresh),
            'token':str(refresh.access_token),
            'created':created


        }).data
