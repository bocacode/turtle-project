# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from extract_gps_coordinates import *
# Find your Account SID and Auth Token in Account Info
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)
body = image_coordinates(img_path)
message = client.messages.create(
    body=body,
    from_='+19259401304',
    to='+14153595829'
    )

print(message.sid)
                