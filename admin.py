import psycopg2
import datetime
import random
import main 
import user


def create_table_bus():
    conn, cur = main.connect()

    try:

        cur.execute(
            'CREATE TABLE bus (busno VARCHAR(10), dest VARCHAR(10),  time VARCHAR(10), seats INT)')

    except:

        print('Table already exist please insert data')

    conn.commit()


def create_table_emp():
    conn, cur = main.connect()

    try:

        cur.execute(
            'CREATE TABLE emp (id VARCHAR(10), name VARCHAR(10),  salary INT, busno INT)')

    except:

        print('Table already exist please insert the data')

    conn.commit()


def create_table_news():
    conn, cur = main.connect()

    try:

        cur.execute(
            'CREATE TABLE news (date VARCHAR(10), subject VARCHAR(10), message VARCHAR(10))')

    except:

        print('Table already exist please insert the data')

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
    data = fetch_data_bus()
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
        salary = int(input("enter a salary amount---> "))
        busno = input("enter a bus number--->")
        conn, cur = main.connect()

        try:
            cur.execute('INSERT INTO emp VALUES(%s, %s, %s, %s)',
                        (id, name, salary, busno))

            print("Data insertion succesfull")
            print("---------------------------------")
            empdetails()

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
    conn, cur = main.connect()
    if result:
        print("this id doesnot exist in the list")

    else:
        try:
            cur.execute("DELETE from emp where id=Id;")
            print(" you have successfully deleted  details of employe id:--->", Id)
            print("---------------------------------------------")
            empdetails()
        except:
            print("error while deleting")

        conn.commit()

    empdetails()


def fetch_data_emp():

    conn, cur = main.connect()

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
        print('busno assigned: ', row[3])
        print('----------------------------------')

    admin()

# function to delete the table


def addannouncement():
    create_table_news()
    print("Type a announcement message here")
    print("----------------------------------")
    date = input("Enter todays date-->")
    subject = input("Subject---->(Lost/Found/Delay):")
    message = input("Message---------->")
    conn, cur = main.connect()
    try:
        cur.execute('INSERT INTO news VALUES(%s, %s, %s)',
                    (date, subject, message))
        print("Announcement made successfully!!!!")

    except Exception as e:
        print('Error', e)

    admin()


def insert_data_bus():
    create_table_bus()
    print("------------------------------")
    print("You are in insert  function")
    busno = input("Enter bus no : ")
    result = checkbus(busno)
    if result:
        dest = input("Enter a destination:--->")
        time = input("Enter a time for bus:--> ")
        seats = int(input("Enter seats number:->"))
        conn, cur = main.connect()

        try:
            cur.execute('INSERT INTO bus VALUES(%s, %s, %s, %s)',
                        (busno, dest, time, seats))

            print("Data insertion Successfull")
            print("------------------------------>")
            busdetails()

        except Exception as e:
            print('error', e)
    # commiting the transaction.
        conn.commit()
    else:
        print("Error while inserting the data   ")

    busdetails()


def del_data_bus():
    print("You are in delete function")
    Busno = input("Enter a bus no:-->")
    result = checkbus(Busno)
    if result:
        print("This bus no doesnot exist in the list")

    else:
        conn, cur = main.connect()
        try:
            cur.execute("DELETE from bus where busno=Busno;")
            print(" You have successfully deleted Bus details of busno:--->", Busno)
            print("---------------------------------------------")
        except:
            print("Error while deleting")

        conn.commit()

    busdetails()


def fetch_data_bus():

    conn, cur = main.connect()

    try:
        cur.execute('SELECT * FROM bus')

    except:
        print('Error !')

    data = cur.fetchall()

    return data


def print_data_bus(data):

    print('Query result: ')
    print()

    for row in data:

        print('Bus No: ', row[0])
        print('Destination: ', row[1])
        print('Time: ', row[2])
        print('Seats ', row[3])
        print('----------------------------------')


def fetch_data_announcement():

    conn, cur = main.connect()

    try:
        cur.execute('SELECT * FROM  news ')

    except:
        print('Error !')

    data = cur.fetchall()

    return data


def print_data_announcement(data):

    print('Query result: ')
    print()

    for row in data:
        print(row[0])
        print(row[1])
        print([row[2]])




def busdetails():
    print("Choose the operation  on bus")
    print(" For inserting : 1 ")
    print(" For  deleting : 2 ")
    print("For printing bus details : 3")
    print("               ")
    op = input("Enter desired option:--> ")
    print("-------------------------------")
    if op == '1':
        insert_data_bus()

    elif op == '2':
        del_data_bus()

    elif op == '3':
        data = fetch_data_bus()
        print_data_bus(data)

    else:
        print(" You have entered Wrong option now we are rendering to the admin section ")
        admin()


def empdetails():
    print(" Choose the operation  on employee")
    print(" For inserting : 1 ")
    print(" For  deleting : 2 ")
    print(" For printing details: 3")
    print("               ")
    op = input("Enter desired option:-----> ")
    print("---------------------------")
    if op == '1':
        insert_data_emp()

    elif op == '2':
        del_data_emp()

    elif op == '3':
        data = fetch_data_emp()
        print_data_emp(data)

    else:
        print(" You have entered Wrong option now we are rendering to the admin section ")
        admin()

def print_data_announcements():
    print("--------------->")
    print("2021/6/8")
    print("lost ")
    print("gautam")
    print("------------>")
    
def admin():
    print("As you are logged in as admin ")
    print("...................")
    print(" Please select the option of the task you wanna do ")
    print("...................")
    print(" For bus details insert/remove/print:1")
    print(" For employee  details insert/remove/print:2")
    print(" For adding any announcement(lost/found/delaya):3")
    selc = input(" Your desired task :---> ")
    print("...................")
    print("           ")
    if selc == '1':
        busdetails()
    elif selc == '2':
        empdetails()

    elif selc == '3':
        addannouncement()

    else:
        print("Do you continue as admin ")
        op = input(" Enter 'yes' or any other key for main menu:------>")
        if op == 'yes':
            admin()
        else:
            ()


def render():
    user.menu()

# driver function
