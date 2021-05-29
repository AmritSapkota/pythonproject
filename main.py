#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="pythonproject", user = "postgres", password = "gautam", host = "127.0.0.1", port = "5432")

print ("Opened database successfully")