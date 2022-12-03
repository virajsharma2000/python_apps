import mysql.connector
from flask import Flask,request
import random

app = Flask(__name__)

mydb = mysql.connector.connect(
host = 'localhost',
username = 'viraj',
password = 'pumpulili',
database = 'viraj'
)

@app.route('/payment')

def payment():
    your_account_id = request.values.get('your_account_id')
    which_account_id_to_pay = request.values.get('which_account_id_to_pay')
    amount_to_be_paied = float(request.values.get('amount_to_be_paied'))

    c = mydb.cursor()
    c.execute('select pan_card FROM india_personal_bank WHERE account_id={}'.format(your_account_id))

    r = c.fetchall()

    for records in r:
        pan_card = records[0]


    c = mydb.cursor()

    c.execute('select current_balance from india_personal_bank WHERE account_id={}'.format(your_account_id))

    r = c.fetchall()

    for records in r:
        current_balance_of_account_id1 = records[0]
       
        

    if amount_to_be_paied > current_balance_of_account_id1:
        return 'Error - amount greater than debit amount'

    else:
        
     c.execute('select pan_card from india_personal_bank where account_id={}'.format(your_account_id))

     r = c.fetchall()

     for records in r:
        pan_card = records[0]

     if any(pan_card) == False and amount_to_be_paied > 1000:
      return "Error - you cannot pay more than 1000 if you don't have pan card"

     else:
        c = mydb.cursor()

        c.execute('select current_balance from india_personal_bank WHERE account_id={}'.format(your_account_id))

        r = c.fetchall()

        for records in r:
         current_balance_of_account_id2 = records[0]
        
        current_balance_of_account_id2  -=  amount_to_be_paied  

        c.execute('UPDATE india_personal_bank SET current_balance={} WHERE account_id={}'.format(current_balance_of_account_id2,your_account_id))

        mydb.commit()


        c.execute('select current_balance from india_personal_bank WHERE account_id={}'.format(which_account_id_to_pay))

        r = c.fetchall()

        for records in r:
          curent_balance_of_account_id_whome_to_pay = records[0]


        amount_to_be_paied += curent_balance_of_account_id_whome_to_pay
    
        c.execute('UPDATE india_personal_bank SET current_balance={} WHERE account_id={}'.format(amount_to_be_paied,which_account_id_to_pay))

        mydb.commit()


        return 'payment completed'

     


@app.route('/get_account_details')


def get_account_details():
    account_id = request.values.get('account_id')

    c = mydb.cursor()

    c.execute('select * from india_personal_bank WHERE account_id={}'.format('account_id'))

    r = c.fetchall()

    for records in r:
        return {
               'name':'{} {}'.format(records[1],records[2]),
               'flat_number':records[3],
               'floor_number':records[4],
               'society_name':records[5],
               'contact_number':'{}{}'.format(records[6],records[7]),
               'current_balance':records[8],
               'email':records[9],
               'city':records[10],
               }




@app.route('/create_account')

def create_account():
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    
    account_id = ''.join(random.choice(numbers) for x in range(8))
    print(account_id)

    first_name = request.values.get('your_first_name')
    last_name = request.values.get('your_last_name')

    house_flat_number = request.values.get('your_house_flat_number')
    house_floor_number = request.values.get('your_house_floor_number')
    society_name = request.values.get('your_society_name')

    country_code = '+91'

    phone_number = request.values.get('your_phone_number')

    current_balance = 0.0

    email = request.values.get('your_email')

    city = request.values.get('your_city')

    pan_card = request.values.get('pan_card')

    c = mydb.cursor()

    c.execute('INSERT INTO india_personal_bank (account_id, first_name, last_name,flat_number, floor_number, society_name, country_code_of_user, phone_number_of_user,current_balance,user_email,city, pan_card) VALUES({},"{}","{}","{}",{},"{}","{}","{}","{}","{}","{}","{}")'
              .format(
                account_id,
                  first_name,
                  last_name,
                  int(house_flat_number),
                  int(house_floor_number),
                  
                  society_name,
                  country_code,
                  phone_number,
                  current_balance,
                  email,
                  city,
                  pan_card
                  

            )
              )


    mydb.commit()

    return 'account created successfully!!'

@app.route('/get_pending_challans')

def get_pending_challans():
    challans_of_account_id = request.values.get('challans_of_account_id')
    
    c = mydb.cursor()
    c.execute('select * from challans WHERE status=pending AND challaned_account_id={}'.format(challans_of_account_id))

    r = c.fetchall()

    for records in r:
        return 'challan_id:{}\nchallan_reason:{}\nchallan_amount:{}\n'.format(records[0],records[3],records[4],records[5])

@app.route('/get_completed_challans')

def get_completed_challans():
     challans_of_account_id = request.values.get('challans_of_account_id')

     c = mydb.cursor()
     c.execute('select * from challans WHERE status=completed AND challaned_account_id={}'.format(challans_of_account_id))

     r = c.fetchall()

     for records in r:
        return 'challan_id:{}\nchallan_reason:{}\nchallan_amount:{}\n\n\n'.format(records[0],records[3],records[4],records[5])

@app.route('/create_challan')
    
def create_challan():
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    challan_id = ''.join(random.choice(numbers) for x in range(8))
    account_id_to_be_challaned = request.values.get('account_id_to_be_challaned')
    trafic_police_account_id =  request.values.get('trafic_police_account_id')
    challan_reason = request.values.get('challan_reason')
    challan_status = 'pending'
    challan_amount = request.values.get('challan_amount')

    c = mydb.cursor()
    c.execute('INSERT INTO challans(challan_id,challaned_account_id,trafic_police_account_id,challan_reason,challan_status,challan_amount) VALUES({},{},{},{},{},{})'.format(int(challan_id),int(account_id_to_be_challaned),int(trafic_police_account_id),challan_reason,challan_status,float(challan_amount)))
    mydb.commit()


@app.route('/pay_challan')

def pay_challan():
    challan_id = request.values.get('challan_id')
    
    c = mydb.cursor()
    c.execute('select * from challans WHERE challan_id={}'.format(challan_id))
    

    r = c.fetchall()

    for records in r:
     your_account_id = records[1]
     which_account_id_to_pay = records[2]
     amount_to_be_paied = records[5]
     
     c = mydb.cursor()
     c.execute('select pan_card FROM india_personal_bank WHERE account_id={}'.format(your_account_id))

     r = c.fetchall()

     for records in r:
        pan_card = records[0]


     c = mydb.cursor()

     c.execute('select current_balance from india_personal_bank WHERE account_id={}'.format(your_account_id))

     r = c.fetchall()

     for records in r:
        current_balance_of_account_id1 = records[0]
       
        

     if amount_to_be_paied > current_balance_of_account_id1:
        return 'Error - amount greater than debit amount'

     else:
        
      c.execute('select pan_card from india_personal_bank where account_id={}'.format(your_account_id))

      r = c.fetchall()

      for records in r:
        pan_card = records[0]

      if any(pan_card) == False and amount_to_be_paied > 1000:
       return "Error - you cannot pay more than 1000 if you don't have pan card"

      else:
        c = mydb.cursor()

        c.execute('select current_balance from india_personal_bank WHERE account_id={}'.format(your_account_id))

        r = c.fetchall()

        for records in r:
         current_balance_of_account_id2 = records[0]
        
        current_balance_of_account_id2  -=  amount_to_be_paied  

        c.execute('UPDATE india_personal_bank SET current_balance={} WHERE account_id={}'.format(current_balance_of_account_id2,your_account_id))

        mydb.commit()


        c.execute('select current_balance from india_personal_bank WHERE account_id={}'.format(which_account_id_to_pay))

        r = c.fetchall()

        for records in r:
          curent_balance_of_account_id_whome_to_pay = records[0]


        amount_to_be_paied += curent_balance_of_account_id_whome_to_pay
    
        c.execute('UPDATE india_personal_bank SET current_balance={} WHERE account_id={}'.format(amount_to_be_paied,which_account_id_to_pay))

        mydb.commit()

        c = mydb.cursor()
        c.execute('UPDATE challans SET status=completed WHERE challan_id={}'.format(challan_id))


        return 'payment completed'

     
    
    
    


if __name__ == '__main__':
 app.run(host = '0.0.0.0',port = 8080)
 
    

    
    

        
