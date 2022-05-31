from flask import  render_template, request, flash, jsonify, make_response, get_flashed_messages
from app.admin_iventarizaciya import login
from app.list_counting_dobraw import adding_in_lists, redirect, url_for
from app import app
from datetime import datetime, timedelta
import random
import app.random_quote as raqu
from script import conn
import psycopg2
import pandas as pd

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template("admin/dashboard.html")


@app.route("/admin/count_save", methods=["POST", "GET"])
def admin_count_save():
    adding_in_lists()

    if "save" in request.form:

        flash(u"Данные сохранены", "success")

        # get_flashed_messages()
        print("FLASH ADMIN COUNT save ok")
        redirect(url_for("admin_count_save",))
        return render_template('admin/count_save.html')
        # return render_template('admin/inventarizaciya.html')
        # redirect(url_for("product_name", usr = user_and_weight))
    elif "cancel" in request.form:
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("SELECT * FROM dobraw_count;")
                df = pd.DataFrame
                pandas_heroku = df(cur.fetchall())
                print(pandas_heroku)
                flash(f" Отмена {pandas_heroku}", "warning")

                print("FLASH ADMIN COUNT cancel saving process")
        # return render_template('admin/inventarizaciya.html')
        return redirect(url_for("admin_count_save"))
    else:
        return render_template('admin/count_save.html')




    # return render_template("admin/count_save.html")
    # return redirect(url_for("admin_count_save"))
    # if request.method == "POST":
    #
    #     contact()
    #     return redirect(url_for("admin_count_save"))
    # else:
    #     return render_template("admin/count_save.html")



@app.route("/admin/inventarizaciya", methods=["POST", "GET"])
def admin_inventarizaciya():
    login()
    if "save" in request.form:
        flash("Данные сохранены", "success")

        print("FLASH ADMIN save ok")
        return redirect(url_for("admin_inventarizaciya"))
        # return render_template('admin/inventarizaciya.html')
        # redirect(url_for("product_name", usr = user_and_weight))
    elif "cancel" in request.form:
        flash("Отмена", "warning")
        print("FLASH ADMIN cancel saving process")
        # return render_template('admin/inventarizaciya.html')
        return redirect(url_for("admin_inventarizaciya"))
    else:
        return render_template('admin/inventarizaciya.html')


@app.route("/admin/sign-up", methods=["GET", "POST"])
def admin_sign_up():
    if request.method == "POST":

        req = request.form

        username = req.get("username")
        email = req.get("email")
        password = req.get("password")

        if not len(password) >= 10:
            flash("Password length must be at least 10 characters", "warning")

            return render_template("admin/sign_up.html")
        else:
            flash("Account created!", "success")
            return render_template("admin/sign_up.html")

    return render_template("admin/sign_up.html")

@app.route("/admin/<usr>")
def admin_user(usr):
    f"<h1>{usr}</h1>"
    return render_template("admin/usr.html", usr=usr)



@app.route("/random_quote")
def random_quote():

    mylist2 = random.choice(raqu.mylist)
    flash(u'Invalid password provided', 'error')
    return render_template("admin/random_quote.html",
                           mylist2=mylist2,)
@app.route("/jinja")
def jinja():




    my_name = "Vitaliy"


    age= 25

    langs = ["Python", "JavaScript", "Bash", "C", "Ruby"]

    friends = {
        "Anna" : 37,
        "Eva" : 43,
        "Sandra" : 35,
        "Nikolai" : 40
    }

    colours = ("Red", "Green")

    cool = True

    class GitRemote:
        def __init__(self, name,description, url):
            self.name = name
            self.description = description
            self.url = url
        def pull(self):
            return f"Pullin repo {self.name}"

        def clone(self):
            return f"Cloning into {self.url}"
    my_remote= GitRemote(
        name="Flask Jinja",
        description="Template design tutorial",
        url="https://github.com/julian-nash/jinja.git"
    )
    def repeat(x, qty):
        return x * qty

    date =  datetime.utcnow()

    my_html = "<h1> THIS IS SOME HTML </h1>"

    suspicious = "<script>alert('YOU GOT HACKED')</script>"
    return render_template("admin/jinja.html",
                           my_name=my_name, age=age,
                        langs=langs, friends=friends, colours=colours,
                           cool=cool, GitRemote=GitRemote, repeat=repeat,
                           my_remote=my_remote, date=date, my_html=my_html, suspicious=suspicious,
                           )

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")


users = {
    "mitsuhiko" : {
        "name" : "Armin Ronacher",
        "bio" : "Creator of the Flask framework",
        "twitter_handle" : "@mitsuhiko"
    },

    "gvanrossum" : {

        "name" : "Guido Van Rossum",
        "bio" : "Creator of the Python programming language",
        "twitter_handle" : "@gvanrossum"
    },

    "elonmusk" : {
        "name" : "Elon Musk",
        "bio" : "technology entrepreneur, investor, engineer",
        "twitter_handle" : "@elonmusk"

    }

}

@app.route("/profile/<username>")
def profile(username):

    user = None
    if username in users:
        user = users[username]


    return render_template("admin/profile.html", username=username,user=user)


@app.route("/multiple/<foo>/<bar>/<baz>")
def multi(foo, bar, baz):
    return f"foo is {foo}, bar is {bar}, baz is {baz}"

@app.route("/json", methods=["POST"])
def json():

    if request.is_json:

        req = request.get_json()
        response = {
            "message" : "JSON received",
            "name" : req.get("name")
        }

        res = make_response(jsonify(response), 200)

        return res

    else:

        res = make_response(jsonify({"message" : "No JSON received"}), 400)
        return res