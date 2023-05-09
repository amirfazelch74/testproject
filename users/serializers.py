from rest_framework import serializers
from .models import OtpRequest


class RequsetOtpserializer(serializers.Serializer):
    reciever = serializers.CharField(max_length=50, allow_null=False)
    channel = serializers.ChoiceField(allow_null=False, choices=OtpRequest.Otpchannel.choices)


class RequestOtpResponsserializer(serializers.ModelSerializer):
    class Meta:
        model = OtpRequest
        fields = ['request_id']

class Verifyotprequestserializer(serializers.Serializer):
    request_id=serializers.UUIDField(allow_null=False)
    password=serializers.CharField(max_length=4,allow_null=False)
    reciever=serializers.CharField(max_length=64,allow_null=False)
class ObtainTokenserializer(serializers.Serializer):
    token=serializers.CharField(max_length=128,allow_null=False)
    refresh=serializers.CharField(max_length=128,allow_null=False)
    created=serializers.BooleanField()