import psycopg2
import datetime
import random


def connect():

    try:
        conn = psycopg2.connect(database="pythonproject", user="postgres",
                                password="gautam", host="127.0.0.1", port="5432")

        cur = conn.cursor()

    except (Exception, psycopg2.DatabaseError) as error:

        print("Error while creating PostgreSQL table", error)

    return conn, cur


def create_table_bus():
    conn, cur = connect()

    try:

        cur.execute(
            'CREATE TABLE bus (busno VARCHAR(10), dest VARCHAR(10),  time VARCHAR(10), seats INT)')

    except:

        print('error')

    conn.commit()


def create_table_annoncement():
    conn, cur = connect()

    try:

        cur.execute(
            'CREATE TABLE announcement (date VARCHAR(10),message VARCHAR(100))')

    except:

        print('error')

    conn.commit()


def create_table_emp():
    conn, cur = connect()

    try:

        cur.execute(
            'CREATE TABLE emp (id VARCHAR(10), name VARCHAR(10),  salary INT, busno INT)')

    except:

        print('error')

    conn.commit()


def checkemp(id):
    data = fetch_data_emp()
    flag = True
    for row in data:
        if row[0] == id:
            flag = False
            break
        else:
            continue

    return flag


def checkbus(busno):
    data = fetch_data_emp()
    flag = True
    for row in data:
        if row[0] == busno:
            flag = False
            break
        else:
            continue

    return flag


def insert_data_emp():
    create_table_emp()
    print("------------------------------")
    print("you are in insert  function")
    id = input("enter customer  id : ")
    result = checkemp(id)
    if result:
        name = input("enter a name:")
        salary = int(input("enter a salary amount "))
        busno = input("enter a bus number")
        conn, cur = connect()

        try:
            cur.execute('INSERT INTO emp VALUES(%s, %s, %s, %s)',
                        (id, name, salary, busno))

        except Exception as e:
            print('error', e)
    # commiting the transaction.
        conn.commit()
    else:
        print("employee already exist ")

    empdetails()


def del_data_emp():
    print("you are in delete function")
    Id = input("enter a id:")
    result = checkemp(Id)
    if result:
        print("this id doesnot exist in the list")

    else:
        conn, cur = connect()
        try:
            cur.execute("DELETE from emp whare id=Id;")

        except:
            print("error while deleting")

        conn.commit()

    empdetails()


def fetch_data_emp():

    conn, cur = connect()

    try:
        cur.execute('SELECT * FROM emp')

    except:
        print('error !')

    data = cur.fetchall()

    return data


def print_data_emp(data):

    print('Query result: ')
    print()

    for row in data:

        print('id: ', row[0])
        print('name: ', row[1])
        print('salary: ', row[2])
        print('busno: ', row[3])
        print('----------------------------------')

    admin()

# function to delete the table


def insert_data_bus():
    create_table_bus()
    print("------------------------------")
    print("you are in insert  function")
    busno = input("enter bus no : ")
    result = checkbus(busno)
    if result:
        dest = input("enter a destination:")
        time = input("enter a time for bus ")
        seats = int(input("enter seats number"))
        conn, cur = connect()

        try:
            cur.execute('INSERT INTO bus VALUES(%s, %s, %s, %s)',
                        (busno, dest, time, seats))

        except Exception as e:
            print('error', e)
    # commiting the transaction.
        conn.commit()
    else:
        print("employee already exist ")

    busdetails()


def del_data_bus():
    print("you are in delete function")
    Busno = input("enter a bus no:")
    result = checkbus(Busno)
    if result:
        print("this bus no doesnot exist in the list")

    else:
        conn, cur = connect()
        try:
            cur.execute("DELETE from bus where busno=Busno;")

        except:
            print("error while deleting")

        conn.commit()

    busdetails()


def fetch_data_bus():

    conn, cur = connect()

    try:
        cur.execute('SELECT * FROM bus')

    except:
        print('error !')

    data = cur.fetchall()

    return data


def print_data_bus(data):

    print('Query result: ')
    print()

    for row in data:

        print('Bus No: ', row[0])
        print('Destination: ', row[1])
        print('time: ', row[2])
        print('Seats ', row[3])
        print('----------------------------------')

    admin()


def busdetails():
    print("choose the operation  on emp")
    print(" for inserting : 1 ")
    print(" for  deleting : 2 ")
    print("for printing bus details : 3")
    print("               ")
    op = input("enter desired option: ")
    if op == '1':
        insert_data_bus()

    elif op == '2':
        del_data_bus()

    elif op == '3':
        data = fetch_data_bus()
        print_data_bus(data)

    else:
        print(" you entered wrong numbeer ")
        admin()


def empdetails():
    print("choose the operation  on emp")
    print(" for inserting : 1 ")
    print(" for  deleting : 2 ")
    print(" for printing details:3")
    print("               ")
    op = input("enter desired option: ")
    if op == '1':
        insert_data_emp()

    elif op == '2':
        del_data_emp()

    elif op == '3':
        data = fetch_data_emp()
        print_data_emp(data)

    else:
        print(" you entered wrong numbeer ")
        admin()


def fetch_announcement():

    conn, cur = connect()

    try:
        cur.execute('SELECT * FROM announcement')

    except:
        print('error !')

    data = cur.fetchall()

    return data


def addannouncement():
    create_table_annoncement()
    print("type a announcement message here")
    print("----------------------------------")
    date = input("enter todays date")
    message = input("message---------->")
    conn, cur = connect()
    try:
        cur.execute('INSERT INTO announcement VALUES(%s,%s)',
                    (date, message))

    except Exception as e:
        print('error', e)

    admin()


def print_announcement():
    print('Query result: ')
    print()
    data = fetch_announcement()

    for row in data:

        print(row[0])
        print(row[1])

        print('----------------------------------')


def admin():
    print("as you are logged in as admin ")
    print("...................")
    print(" please select the option of the task you wanna do ")
    print("...................")
    print(" for bus details insert/remove/print:1")
    print(" for employee  details insert/remove/print:2")
    print(" for adding any announcement(lost/found/delaya):3")
    selc = input(" your desired task : ")
    print("...................")
    print("           ")
    if selc == '1':
        busdetails()
    elif selc == '2':
        empdetails()

    elif selc == '3':
        addannouncement()

    else:
        print("do you continue as admin ")
        op = input(" enter 'yes' or any other key for main menu")
        if op == 'yes':
            admin()
        else:
            home()


def user():
    pass


# driver function
if __name__ == '__main__':

    opt = ''

    def home():
        print(" choose your role")
        print(" for admin : 1")
        print(" for User: 2 ")
        print("....................")
        opt = input("Enter appropraite number")
        print("        ")
        if opt == '1':
            print(" you have to enter your admin id and password ")
            id = input("id:")
            password = input("password :")
            if id == 'gautam591' and password == '123456':
                print(" you ahve logged in successfully")
                print(".....................")
                admin()
            else:
                print("you entered wrong details please try again ")
                home()
        elif opt == '2':
            user()

        else:
            print("choose at least one option for our service ")
            home()
    print_announcement()
    home()
