import mysql.connector

mydb = mysql.connector.Connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "",
    database = "giveaway"
)
mycursor = mydb.cursor()

def write_user(val):
    sql = "insert into users_bot(name,surname,age,city,address,phonenumber,email) values(%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, val)
    mydb.commit()

def read_users():
    sql = "select * from users_bot"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

def update_user(val):
    sql = "update users_bot set name = %s, surname = %s, age = %s, city = %s, address = %s, phonenumber = %s, email = %s where id = %s"
    mycursor.execute(sql, val)
    mydb.commit()

def delete_user(val):
    sql = "delete from users_bot where id = %s"
    mycursor.execute(sql, val)
    mydb.commit()

while True:
    choice = int(input("[1]Add user\n[2]List of users\n[3]Update user\n[4]Delete users\n[0]Exit\n"))
    if choice == 1:
        name = input("Insert name: ")
        surname = input("Insert surname: ")
        age = int(input("Insert age: "))
        city = input("Insert city: ")
        address = input("Insert address: ")
        phonenumber = int(input("Insert phone number: "))
        email = input("Insert email: ")
        val = (name, surname, age, city, address, phonenumber, email)
        write_user(val)
    elif choice == 2:
        users = read_users()
        for u in users:
            print(u)
    elif choice == 3:
        id = int(input("Insert user ID: "))
        name = input("Insert new name: ")
        surname = input("Insert new urname: ")
        age = int(input("Insert new age: "))
        city = input("Insert new city: ")
        address = input("Insert new address: ")
        phonenumber = int(input("Insert new phone number: "))
        email = input("Insert new email: ")
        val = (name, surname, age, city, address, phonenumber, email, id)
        update_user(val)
    elif choice == 4:
        id = int(input("Insert user id: "))
        val = (id,)
        delete_user(val)
    elif choice == 0:
        break