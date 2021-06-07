
import psycopg2
import random
from main import connect
import admin


def menu():
    print("**********Services************")
    print("1. Search Route")
    print("2. Reserve Ticket")
    print("3. Cancel Ticket")
    print("4. Reserve vehicle")
    print("5. Vehicle Timetable")

    selectedService = int(input("Select service: "))
    if (selectedService == 1):
        searchRoute()
    elif (selectedService == 2):
        reserve_ticket()
    elif (selectedService == 3):
        term_and_condition()
    elif (selectedService == 4):
        pass
    elif (selectedService == 5):
        vehicle_timetable()
    else:
        print("-------Please Enter Vaild Service.-----------")
        menu()


def searchRoute():
    route = input("Enter your destination: ")
    data = admin.fetch_data_bus()
    for row in data:
        if row[1] == route:
            print('Bus No: ', row[0])
            print('Destination: ', row[1])
            print('time: ', row[2])
            print('Seats ', row[3])
            print('----------------------------------')

    # fetching all bus info with this destination


def create_table():
    conn, cur = connect()
    try:
        cur.execute(
            'CREATE TABLE ticket (name VARCHAR(10), dest VARCHAR(10),  busno VARCHAR(10), phoneno INT, ticketno INT)')
    except:
        print('table already exist please enter the data.')
    conn.commit()


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
    create_table()
    name = input("Name: ")
    dest = input("Destinatino: ")
    busno = input("Bus no: ")
    phoneno = int(input("Phone no: "))
    ticket_no = random.randint(1000101, 9999999)

    # checking ticket
    while not check_ticket(ticket_no):
        ticket_no = generate_rand()

    conn, cur = connect()
    try:
        cur.execute('INSERT INTO ticket VALUES(%s, %s, %s, %s, %s)',
                    (name, dest, busno, phoneno, ticket_no))
        print("!! Ticket Reserved !!")
        print("your ticket info is----->")
        data = fetch_data_ticket()
        print_ticket_info(data)

    except Exception as e:
        print('error', e)
    # commiting the transaction.
    conn.commit()


def fetch_data_ticket():
    conn, cur = connect()
    try:
        cur.execute('SELECT * FROM ticket')
    except:
        print('Ticket Error')
    data = cur.fetchall()
    return data


def print_ticket_info(data):

    for row in data:
        count = 0
        for x in row:
            if count == 0:
                print('Name:', x)
                count += 1
            elif count == 1:
                print('Destination:', x)
                count += 1
            elif count == 2:
                print('Bus no;', x)
                count += 1
            elif count == 3:
                print('Phone no:', x)
                count += 1
            elif count == 4:
                print('Ticket no:', x)
                count += 1

        print("------------------")


def term_and_condition():
    print("------------------------------------------------------------------")
    print("you can only cancel the ticket before the 1 hour of departure time ")
    print('while cancelling the ticket your  30% payment will be deducted     ')
    print("yoor money will be return to the same card from which you booked the ticket")
    print("if you still want to cancel the ticket please enter 'yes' if you dont please enter  'no'")
    print("---------------------------------------------------------------------------------------")
    op = input("do you want to cancel your ticket yes/no:-->")
    if op == 'yes':
        cancel_ticket()
    elif op == 'no':
        menu()


def cancel_ticket():

    ticketno = int(input("Enter your ticket numbeer:-->"))
    result = check_ticket(ticketno)
    if result:
        print("The ticket nuber you entered is not issued yet")

    else:
        conn, cur = connect()
        try:
            print(" Your ticket is successfully cancelled  :--->", ticketno)
            cur.execute("DELETE from ticket where ticketno =ticketno;")
            print("---------------------------------------------")
        except:
            print("    ")
            menu()

        conn.commit()

    menu()


def reserve_vehicle():
    pass


def vehicle_timetable():
    data = admin.fetch_data_bus()
    admin.print_data_bus(data)
