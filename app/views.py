from flask import  render_template, request, flash,  redirect, url_for
from app.inventarizaciya import login
from app.list_counting_dobraw_public import adding_in_lists
from app import app
from app.dao_random_quote import mylist
import random
from script import conn
import psycopg2



@app.route('/public/index')
def index():
    return render_template("public/index.html")



@app.route("/public/count_save", methods=["POST", "GET"])
def count_save():
    adding_in_lists()

    if "save" in request.form:
        flash(u"Данные сохранены", "success")
        redirect(url_for("count_save" ))
        return render_template('public/count_save.html')

    elif "cancel" in request.form:
        flash(" Отмена ", "warning")
        return redirect(url_for("count_save"))

    else:
        return render_template('public/count_save.html')

    return render_template('public/count_save.html')


@app.route("/public/admin_password")
def admin_password():
    return render_template("public/admin_password.html")


@app.route("/public/inventarizaciya", methods=["POST", "GET"])
def inventarizaciya():
    login()
    if "save" in request.form:
        flash("Данные сохранены", "success")
        print("FLASH PUBLIC save ok")
        return redirect(url_for("inventarizaciya"))

    elif "cancel" in request.form:
        flash("Отмена", "warning")
        print("FLASH PUBLIC cancel saving process")

        return redirect(url_for("inventarizaciya"))
    else:
        return render_template('public/inventarizaciya.html')



@app.route("/public/<usr>")
def user(usr):
    f"<h1>{usr}</h1>"
    return render_template("public/usr.html")

@app.route("/public/random_quote")
def public_random_quote():

    mylist1 = random.choice(mylist)
    return render_template("public/random_quote.html",
                           mylist1=mylist1,)




@app.route("/public/extract_data")
def extract_data_dobraw_public():
    headings = ("Name", "Surname", "Bhts", "Dobraw")
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cur.execute("SELECT NAME, SURNAME, BHT, DOBRAW FROM dobraw_count;")

            datas = cur.fetchall()

            cur.execute("SELECT sum(cast(bht AS INTEGER)) FROM dobraw_count;")
            bhts = cur.fetchall()
            all_bhts = bhts[0][0]

            cur.execute("SELECT sum(cast(dobraw AS FLOAT)) FROM dobraw_count;")
            dobraw = cur.fetchall()
            all_dobraw = dobraw[0][0]

            print("Data selected successfully")


    return render_template("public/extract_data.html", headings=headings, datas=datas,
                           all_bhts=all_bhts, all_dobraw=all_dobraw
                           )
