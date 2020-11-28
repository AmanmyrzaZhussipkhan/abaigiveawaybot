import mysql.connector
mydb = mysql.connector.Connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "giveaway",
    port = 3306
)

mycursor = mydb.cursor()

user = None

def auth(val):
    global user
    sql = "select * from users_bot_2 where login = %s and password = %s"
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    if len(data) == 1:
        user = {
            'id':data[0][0],
            'name':data[0][1],
            'surname':data[0][2],
            'age':data[0][3],
            'city':data[0][4],
            'address':data[0][5],
            'phonenumber':data[0][6],
            'email':data[0][7],
            'login':data[0][8],
            'password':data[0][9],
            'is_admin':data[0][10]
        }
        return True
    else:
        return False

def register_user(val):
    sql = "insert into users_bot_2(name, surname, age, city, address, phonenumber, email, login, password, is_admin) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, val)
    mydb.commit()

def read_users():
    sql = "select * from users_bot_2"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

if __name__ == "__main__":
    login = input("Insert login: ")
    password = input("Insert password: ")
    val = (login, password)
    if auth(val):
        print("WELCOME, "+user['name']+' '+user['surname'])
        if user['is_admin'] == 1:
            print("Admin Menu")
            while True:
                choice = int(input("[1]Users\n[0]Exit\n"))
                if choice == 1:
                    while True:
                     choiceIn = int(input("[1]Add user\n[2]List Users\n[0]Exit\n"))
                     if choiceIn == 1:
                         name = input("Insert name: ")
                         surname = input("Insert surname: ")
                         age = int(input("Insert age: "))
                         city = input("Insert city: ")
                         address = input("Insert address: ")
                         phonenumber = int(input("Insert phone number: "))
                         email = input("Insertm email: ")
                         login = input("Insert login: ")
                         password = input("Insert password: ")
                         is_admin = 0
                         choice_is_admin = input("Is Admin? Y/N\n")
                         if choice_is_admin.lower() == "y":
                             is_admin = 1
                         val = (name, surname, age, city, address, phonenumber, email, login, password, is_admin)
                         register_user(val)
                     elif choiceIn == 2:
                         result = read_users()
                         for u in result:
                          print(user)
                     elif choiceIn == 0:
                         break
    else:
        print("Wrong Login or Password")