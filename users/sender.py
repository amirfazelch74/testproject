from sms_ir import SmsIr
sms_ir=SmsIr('EwIVbg5Mup2tACiR4aexiYiLadc3485HaefjZcLtOI2r4CppbrlGQ9v94s3Hip73',
             30007732009803,
)
def send_otp(otp):
    sms_ir.send_sms(
        '09912392891',
        'otp.password',
        30007732009803
    )
    print('otp password ')
    print(otp.password)