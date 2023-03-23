import mysql.connector
import easygui

def get_recipie(food_name):
    mydb = mysql.connector.connect(
    host = 'localhost',
    username = 'viraj',
    password = 'pumpulili',
    database = 'viraj'
    )

    c = mydb.cursor()

    c.execute('select food_ingredients,procedure from food_recipie where food_name="{}"'.format(food_name))

    r = c.fetchall()

    for records in r:
        food_ingredents = records[0]
        procedure = records[1]

        easygui.msgbox("ingredents\n\n{}\n\n\nprocedure\n\n{}".format(food_ingredents,procedure))


def add_recipie(food_name,ingredients,procedure):
    mydb = mysql.connector.connect(
    host = 'localhost',
    username = 'viraj',
    password = 'pumpulili',
    database = 'viraj'
    )

    c = mydb.cursor()

    c.execute('INSERT INTO food_recipie(food_name,food_ingredents,procedure) VALUES("{}","{}","{}")'.format(food_name))

    mydb.commit()



choices = easygui.enterbox('do you want to add recipie or get recipie? ')

if choices == 'add recipie':
    how_much_ingredients = int(easygui.enterbox('how much ingredents you want to add:'))

    ingredients = ''

    number = 0

    for x in range(how_much_ingredients):
        number += 1

        ingredient = easygui.enterbox('{}.ingredent: '.format(number))

        ingredients += '{}.{}\n'.format(number,ingredient)


    procedure = easygui.textbox('procedure')

    add_recipie(procedure,ingredients)


if choices == 'get recipie':
    food_name = easygui.enterbox('Enter food item:')

    get_recipie(food_name)

    
    

    

        

        

        
    
    
    
