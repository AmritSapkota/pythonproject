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

        print('Table already exist please insert data')

    conn.commit()

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
