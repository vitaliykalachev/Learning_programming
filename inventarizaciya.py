from flask import Flask, redirect, url_for, render_template, request, flash
import psycopg2.extras
import os
from script import DB_NAME, DB_USER, DB_HOST, DB_PASS

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

conn = psycopg2.connect(dbname = DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def login():
    if request.method == "POST":
        product_name = request.form["nm"]
        product_weight = request.form["wt"]
        # req = request.form
        #
        # username = req.get("nm")
        # if not len(username) >= 2:
        #     flash("Password length must be at least 10 characters", "warning")
        #
        # else:
        #     flash("Account created!", "success")



        product_weight = product_weight.replace('+', ' ')

        def max_numbers(product_weight):
            return sum([float(i) for i in product_weight.replace(',', '.').split()])

        all_weight = max_numbers(product_weight)

        def all_weight_numbers(all_weight, dec=0):
            prc = "{:." + str(dec) + "f}"  # first cast decimal as str
            # str format output is {:.3f}
            return prc.format(all_weight)

        product_weight = all_weight_numbers(all_weight)

        # user_and_weight = product_name, user_weight
        # for i in user_and_weight():
        #     if i == True:
        #         return user_and_weight()
        print(product_name, product_weight)

        def file_saving_process():
            with conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    product_name_save = product_name
                    product_weight_save = product_weight

                    cur.execute("INSERT INTO inventarizaciya (name, weight) VALUES(%s, %s)", ((product_name_save.lower()), int(product_weight_save),))

                    cur.execute("SELECT * FROM inventarizaciya;")
                    print(cur.fetchall())

            conn.close()



            # name_save = product_name.lower()
            # weight_save = user_weight
            # filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
            #
            # f = open(f"/Users/new/PycharmProjects/inventarizaciya_final/templates/files/{filename1}.csv", "w")
            #
            # f.write(f"\n {name_save}  {weight_save}")
            #
            # f.close()

        # user_and_weight = product_name, product_weight

        def contact():
            request.method == "GET"
            if "save" in request.form:
                file_saving_process()
                print("save ok")
                return
                    # redirect(url_for("product_name", usr = user_and_weight))
            elif "cancel" in request.form:
                print("cancel saving process")
                return render_template('loging.html')
            else:
                return render_template('loging.html')

        contact()
        return redirect(url_for("inventarizaciya"))

    else:
        return render_template("loging.html")

