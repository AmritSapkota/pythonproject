
import psycopg2
import datetime
import random
import admin
import user
import tkinter as tk



def connect():

    try:
        conn = psycopg2.connect(database="pythonproject", user="postgres",
                                password="gautam", host="127.0.0.1", port="5432")

        cur = conn.cursor()

    except (Exception, psycopg2.DatabaseError) as error:

        print("Error while creating PostgreSQL table", error)

    return conn, cur

def home():
        window= tk.Tk()
        opt = ''
        print(" Choose your role")
        print(" For admin : 1")
        print(" For User: 2 ")
        print("....................")
        opt = input("Enter appropraite number:--->")
        window.destroy()
        print("---------------------------------")
        if opt == '1':
            print(" You have to enter your admin id and password ")
            id = input("id:---->")
            password = input("password :---->")
            if id == 'gautam591' and password == '123456':
                print(" You ahve logged in successfully")
                print(".....................")
                admin.admin()
            else:
                print("You entered wrong details please try again ")
                home()
        elif opt == '2':
          user.menu()

        else:
            print("Choose at least one option for our service ")
            home()

home()




if __name__ == '__main__':


    print("we are in driver function")