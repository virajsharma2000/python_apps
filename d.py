import mysql.connector
t = mysql.connector.connect(host = input("Enter server address: "),
                            user = input("Enter user name: "),
                            password = input("Enter password: "),
                            database = input("Enter database: ")
)
print("start writing mysql code now")
while True:
 c = t.cursor()
 c.execute(input('mysql>'))
 s = c.fetchall()
 o = [i[0]for i in c.description]
 print(o)
 for h in s:
     print(h)
