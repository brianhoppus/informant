from twilio.rest import TwilioRestClient
import dev_account
import socket

# Use your Account Sid and Auth Token from twilio.com/user/account
client = TwilioRestClient(dev_account.account_sid, dev_account.auth_token)
hostname = socket.gethostname()
message_string = "Successful login on {}".format(hostname)

message = client.messages.create(body=message_string,
  to= dev_account.admin_phone_number,    # Replace with your phone number
  from_= dev_account.twilio_phone_number) # Replace with your Twilio number
print(message.sid)
