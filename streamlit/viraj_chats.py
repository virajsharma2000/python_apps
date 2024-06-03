import pymongo
import hashlib
import datetime

mongo = pymongo.MongoClient('mongodb+srv://virajsharma:pumpulili@cluster0.xclz1ks.mongodb.net/?retryWrites=true&w=majority')

def send_message(from_first_name,from_last_name,authorization,to_first_name,to_last_name,message):
 global mongo
 
 database = mongo['viraj_sharma_db']

 records = {
           'from name':from_first_name + ' ' + from_last_name,
           'to name':to_first_name + ' ' + to_last_name,
           'date and time':datetime.datetime.now().strftime('%B - %d - %Y %I:%M:%S %A'),
           'message':message
            }

 database.messages.insert_one(records)

def report(first_name,last_name):
 global mongo
 
 database = mongo['viraj_sharma_db']
 
 records = database.reports.find({first_name:{'$eq':first_name},last_name:{'$eq':last_name}})

 for record in records:
  number_of_reports = record['number of reports']

 records = {
           'name':first_name + ' ' + last_name,
           'number of reports':int(number_of_repots) + 1
            }

 database.reports.insert_one(records)

def sign_up(first_name,last_name,password):
 global mongo
 
 database = mongo['viraj_sharma_db']

 records = {
           'name':first_name + ' ' + last_name,
           'password':hashlib.sha256(password.encode()).hexdigest()
            }

 database.accounts.insert_one(records)

def sign_in(first_name,last_name,password):
 global mongo
 
 database = mongo['viraj_sharma_db']

 records = database.accounts.find({'name':{'$eq':first_name + ' ' + last_name}})

 for record in records:
  authorization = hashlib.sha256(password.encode()).hexdigest() == record['password']

  return authorization


