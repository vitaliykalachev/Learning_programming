from flask import render_template, request
import psycopg2.extras
import os
from script import DB_NAME, DB_USER, DB_HOST, DB_PASS

os.environ['DATABASE_URL'] = "postgres://atwrtaatphuwev:bbe8f3b93fd8c58cb9ac8c952b4cd9daf74edd1454bec9d83088aaad2d889788@ec2-3-218-171-44.compute-1.amazonaws.com:5432/ddd4mnclae5h30"
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

conn = psycopg2.connect(dbname = DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def login():
    if request.method == "POST":
        product_name = request.form["nm"]
        product_weight = request.form["wt"]
        product_weight = product_weight.replace('+', ' ')

        def max_numbers(product_weight): #sum replace ","
            return sum([float(i) for i in product_weight.replace(',', '.').split()])

        all_weight = max_numbers(product_weight)

        def all_weight_numbers(all_weight, dec=0):
            prc = "{:." + str(dec) + "f}"  # first cast decimal as str
            return prc.format(all_weight)

        product_weight = all_weight_numbers(all_weight)
        print(product_name, product_weight)


        def file_saving_process(): #file saving process in PostgreSQL Heroku database
            with conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    product_name_save = product_name
                    product_weight_save = product_weight
                    cur.execute("INSERT INTO inventarizaciya (name, weight) VALUES(%s, %s)", ((product_name_save.lower()), int(product_weight_save),))
                    cur.execute("SELECT * FROM inventarizaciya;")
                    print(cur.fetchall())


        def contact(): #request from html request form
            request.method == "POST"
            if "save" in request.form:
                file_saving_process()
                print("ADMIN save ok")
                return
            elif "cancel" in request.form:
                print("ADMIN cancel saving process")
                return
            else:
                return render_template('admin/inventarizaciya.html')
        contact()
        return

    else:
        return

