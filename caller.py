from twilio.rest import Client
account_sid="<SID>"
auth_token="your auth token"
Client=Client(account_sid, auth_token)
call=Client.calls.create(
twiml="<Response><Say>thanks for trying our documanttation talk to kalpana sharma</Say><Dial>+919310990499</Dial></Response>",
from_="+13213513640",
to="+919958561465",
)
print(call.sid)
