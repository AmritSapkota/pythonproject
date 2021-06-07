import psycopg2
import random
from main import connect





def menu():
    print("**********Services************")
    print("1. Search Route")
    print("2. Reserve Ticket")
    print("3. Cancel Ticket")
    print("4. Reserve vehicle")
    print("5. Vehicle Timetable")

    selectedService = int(input("Select service: "))
    if (selectedService == 1):
        pass
    elif (selectedService == 2):
        reserve_ticket()
    elif (selectedService == 3):
        pass
    elif (selectedService == 4):
        pass
    elif (selectedService == 5):
        pass
    else:
        print("-------Please Enter Vaild Service.-----------")
        menu()


def searchRoute():
    route = input("Enter your destination: ")

    #fetching all bus info with this destination

def create_table():
    conn, cur = connect()
    try:
        cur.execute(
            'CREATE TABLE ticket (name VARCHAR(10), dest VARCHAR(10),  busno VARCHAR(10), phoneno INT, ticketno INT)')
    except:
        print('Error while creating table.')
    conn.commit()

def fetch_data_ticket():
    conn, cur = connect()
    try:
        cur.execute('SELECT * FROM ticket')
    except:
        print('Ticket Error')
    data = cur.fetchall()
    return data

def check_ticket(ticketno):
    data = fetch_data_ticket()
    flag = True
    for row in data:
        if row[4] == ticketno:
            flag = False
            break
        else:
            continue

    return flag
def generate_rand():
    return random.randint(1000101, 9999999)

def reserve_ticket():
     #create_table()
     name = input("Name: ")
     dest = input("Destinatino: ")
     busno = input("Bus no: ")
     phoneno = int(input("Phone no: "))
     ticket_no = random.randint(1000101, 9999999)

     #checking ticket
     while not check_ticket(ticket_no):
         ticket_no = generate_rand()

     conn, cur = connect()
     try:
        cur.execute('INSERT INTO ticket VALUES(%s, %s, %s, %s, %s)',
                        (name, dest, busno, phoneno, ticket_no))
        print("!! Ticket Reserved !!")

     except Exception as e:
            print('error', e)
    # commiting the transaction.
     conn.commit()





def cancel_ticket():
    pass


def reserve_vehicle():
    pass


def vehicle_timetable():
    pass