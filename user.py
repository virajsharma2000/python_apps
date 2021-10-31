from twilio.rest import Client
account_sid="<your sid>"
auth_token="your token"
Client=Client(account_sid, auth_token)
call=Client.calls.create(
from_="+13213513640",
to="+917982266126",
twiml="<Response><Say>thanks for trying are documentation</Say></Response>",
)
print(call.sid)
