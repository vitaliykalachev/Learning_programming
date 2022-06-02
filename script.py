import psycopg2.extras
import os

DB_HOST = "ec2-3-218-171-44.compute-1.amazonaws.com"
DB_NAME = "ddd4mnclae5h30"
DB_USER = "atwrtaatphuwev"
DB_PASS = "bbe8f3b93fd8c58cb9ac8c952b4cd9daf74edd1454bec9d83088aaad2d889788"



conn = psycopg2.connect(dbname = DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

# with conn:
#     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
#         # name = input("Введите название: ")
#         # user_weight = input("Введите вес: ")
#         cur.execute(
#             """CREATE TABLE dobraw_count(
#             id serial PRIMARY KEY,
#             name varchar(50) NOT NULL,
#             surname varchar(50) NOT NULL,
#             bht varchar(30) NOT NULL,
#             dobraw varchar(30) NOT NULL
#             );"""
#                     )
#         # cur.execute("INSERT INTO invent_april (name, weight) VALUES(%s, %s)", ((name.lower()), int(user_weight),))
#
        # cur.execute("SELECT * FROM dobraw_count;")
        # cur.fetchall()
#
# conn.close()
#



















# cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# cur.execute("CREATE TABLE invent_april (id SERIAL PRIMARY KEY, name VARCHAR, weight VARCHAR);")
# cur.execute("DROP TABLE invent_april;")
# cur.executescript("""
#     INSERT INTO invent_april (name) VALUES(%s)", ("Бананы",);
#     INSERT INTO invent_april (weight) VALUES(%s)", ("3000",);
#     """)

# cur.execute("INSERT INTO invent_april (name, weight) VALUES(%s, %s)”, ("Бананы", “3000”,))














    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")

    # cur.execute("INSERT INTO student (name) VALUES(%s)", ("Sanda",))

    # cur.execute("SELECT * FROM student;")


# with conn:
#     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
#         # cur.execute("SELECT * FROM student WHERE id = %s",(1,))
#         cur.execute("SELECT * FROM student;")
#         print(cur.fetchall())
        # print(cur.fetchone()["name"])
        # cur.execute("INSERT INTO student (name) VALUES(%s)", ("Brad",))

# conn.commit()
#
# cur.close()

# conn.close()

# import pandas as pd
# import requests
#
# url = "https://data.heroku.com/dataclips/nlickfqedupilzpkruxbhuxxwkfp.csv"
# s = requests.get(url).content
# c = pd.read_csv(s)

import pandas as pd
# from flask import request
# import ssl
# import certifi
# ssl._create_default_https_context = ssl._create_unverified_context
# url="https://data.heroku.com/dataclips/nlickfqedupilzpkruxbhuxxwkfp"
# url(request, context=ssl.create_default_context(cafile=certifi.where()))
#
# c=pd.read_csv(url)
#
# print(c)

# import requests
# import csv
# url = 'https://data.heroku.com/dataclips/nlickfqedupilzpkruxbhuxxwkfp.csv'
# r = requests.get(url)
# text = r.iter_lines()
# reader = csv.reader(text, delimiter=',')
#
# print(text)

