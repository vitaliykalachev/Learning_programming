# import pandas as pd
# from flask import Flask, redirect, url_for, render_template, request
import psycopg2.extras
# import os
from script import DB_NAME, DB_USER, DB_HOST, DB_PASS

# DATABASE_URL = os.environ['DATABASE_URL']
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


cur.execute("SELECT NAME, SURNAME, BHT, DOBRAW FROM dobraw_count;")

rows = cur.fetchall()

for data in rows:
    print("Name : " + str(data[0]))
    print("Surname : " + str(data[1]))
    print("Bhts : " + data[2])
    print("Dobraw : " + data[3])


print("Data selected successfully")


cur.execute("SELECT sum(cast(bht AS INTEGER)) FROM dobraw_count;")
bhts = cur.fetchall()
print(bhts[0][0])

