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