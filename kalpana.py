from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
app = Flask(__name__)
@app.route('/', methods = ['GET','POST'])
def voice():
    resp = VoiceResponse()
    resp.say("thanks for calling kalpana sharma custmer care")
    resp.dial("+919310990499")
    return str(resp)
if __name__ == "__main__":
  app.run(debug = True)
     
