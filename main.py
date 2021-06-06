import psycopg2
import datetime
import random


def connect():

    
    try:
        conn = psycopg2.connect(database="pythonproject", user="postgres",
                                password="amrit", host="127.0.0.1", port="5432")

      
        cur = conn.cursor()

    except (Exception, psycopg2.DatabaseError) as error:

        print("Error while creating PostgreSQL table", error)

 
    return conn, cur



def create_table_emp():
    conn, cur = connect()

    try:

        cur.execute(
            'CREATE TABLE emp (id VARCHAR(10), name VARCHAR(10),  salary INT, busno INT)')

    except:

        print('error')

    conn.commit()


def checkemp(id):
    data= fetch_data_emp()
    flag = True
    # for row in data:
    # if row[0]==id:
    # flag=False
    # break
    # else:
    # continue

    return flag


def insert_data_emp():
    create_table_emp()
    print("------------------------------")
    print("you are in insert  function")
    id = input("inter a id : ")
    result = checkemp(id)
    if result:
        name = input("enter a name:")
        salary = int(input("enter a salary amount "))
        busno = int(input("enter a bus number"))
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

# function to delete the table


def delete_table():

    conn, cur = connect()

    # delete the table
    try:

        cur.execute('DROP TABLE emp')

    except Exception as e:
        print('error', e)

    conn.commit()


def busdetails():
    pass


def empdetails():
    print("choose the operation  on emp")
    print(" for inserting : 1 ")
    print(" for  deleting : 2 ")
    print("               ")
    op = input("enter desired option: ")
    if op == '1':
        insert_data_emp()

    elif op == '2':
        del_data_emp()

    else:
        print(" you entered wrong numbeer ")
        admin()


def announcement():
    pass


def admin():

    print("as you are logged in as admin ")
    print("...................")
    print(" please select the option of the task you wanna do ")
    print("...................")
    print(" for bus details insert/remove:1")
    print(" for employee  details insert/remove:2")
    print(" print employee details:3")
    print(" for adding any anniuncement:4")
    selc = input(" your desired task : ")
    print("...................")
    print("           ")
    if selc == '1':
        busdetails()
    elif selc == '2':
        empdetails()

    elif selc == '3':
        announcement()

    elif selc == '3':
        print_data_emp()

    else:
        print("do you continue as admin ")
        op = input(" enter 'yes' or any other key for main menu")
        if op == 'yes':
            admin()
        else:
            home()

# User Part 
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
        opt = input("Enter appropraite number: ")
        print("        ")
        if opt == '1':
            print("*******you have to enter your admin id and password********")
            id = input("id: ")
            password = input("password: ")
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

    home()
