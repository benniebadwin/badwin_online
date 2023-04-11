from decouple import config, Csv
import requests
from requests.auth import HTTPBasicAuth
import json
import base64
from datetime import datetime

from mpesa_api.mpesa_credentials import MpesaC2bCredential



# get mpesa access token
class MpesaC2bCredential:
    consumer_key = 'VSnv0qW2jhAjKNrqlFDZpZ3NxXbvpMwt'
    consumer_secret = 'QfIReIomJXgxjxc6'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
class LipanaMpesaPassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    Test_c2b_shortcode = "600344"
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    data_to_encode = Business_short_code + passkey + lipa_time
    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')

   
    


# # LIPA NA M-PESA ONLINE
# class LipaNaMpesaPassword:
#     payment_time = datetime.now().strftime("%Y%m%d%H%M%S")
    
#     BusinessShortCode = config("BusinessShortCode")
#     BusinessShortCodeForCToB = config('BusinessShortCodeForCToB')
    
#     passkey = config('PASSKEY')

#     data_to_encode = BusinessShortCode + passkey + payment_time
#     online_password = base64.b64encode(data_to_encode.encode())
#     decode_password = online_password.decode('utf-8')