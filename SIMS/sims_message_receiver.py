from flask import Flask,request
import plyer

app = Flask(__name__)

firstname = input('Enter your first name: ')
lastname = input('Enter your last name: ')

@app.route('/messages/{}/{}'.format(firstname,lastname))

def receive_message():
    first_name = request.args.get('your_firstname')
    last_name = request.args.get('your_lastname')
    messages = request.args.get('message')
    

    plyer.notification.notify(
                             title = 'SIMS',
                             message = 'name:{} {} message:{}'.format(
                                 first_name,
                                 last_name,
                                 messages
                                )
                             )

    return 'message sent successfully'



app.run(port  = '8080',host = '0.0.0.0')
    
    
