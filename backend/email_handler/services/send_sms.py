# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
if not account_sid:
    raise ValueError("TWILIO_ACCOUNT_SID is not set. Check your .env file or environment variables.")
client = Client(account_sid, auth_token)


message = client.messages.create(
    body="i love ila petrovic",
    from_="+18336576054",
    to="+18777804236",
)

print(message.body)