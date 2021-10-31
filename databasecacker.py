import mysql.connector
s = mysql.connector.connect(host = input("Enter mysql server address: "),
                            user = input("Enter user name: "),
                            password = input("Enter password: "),
                            database = input("Enter database: ")
)
print('start writing mysql Code now')
while True:
    c = s.cursor()
    c.execute(input("mysql>"))
    o = c.fetchall()
    u = [i[0] for i in c.description]
    print(u)
    for x in o:
        print(x)
