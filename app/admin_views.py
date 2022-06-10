from flask import  render_template, request, flash, jsonify, make_response, redirect
from app.admin_iventarizaciya import login
from app.list_counting_dobraw import adding_in_lists, url_for
from app import app
from datetime import datetime, timedelta
from app.random_quote import mylist
import random
import app.random_quote as raqu
from script import conn
import psycopg2
import pandas as pd
import os
from werkzeug.utils import secure_filename

@app.route('/admin/dashboard')
def admin_dashboard():
    print(f" Flask ENV is set to: {app.config['ENV']}")
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
        flash(" Отмена ", "warning")
        print("FLASH ADMIN COUNT cancel saving process")
        return redirect(url_for("admin_count_save"))
    elif "table" in request.form:
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("SELECT * FROM dobraw_count ;")
                df = pd.DataFrame
                pandas_heroku = df(cur.fetchall())
                print(pandas_heroku)

        return
            # render_template('admin/count_save.html', pandas_heroku=pandas_heroku)

    else:
        return render_template('admin/count_save.html')

    my_name = "Vitaliy"

    return render_template('admin/count_save.html', pandas_heroku=pandas_heroku, my_name=my_name)
# def table():





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

    # iframe = "https://data.heroku.com/dataclips/cnmkkemnkztlaqxpyykjtgdygzxm"
    #
    # return render_template('admin/inventarizaciya.html', iframe=iframe)

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


    mylist1 = random.choice(mylist)
    return render_template("admin/random_quote.html",
                           mylist1=mylist1,)
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


@app.route("/guestbook")
def guestbook():
    return render_template("admin/guestbook.html")

@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message": "JSON received"}), 200)

    return res



app.config["IMAGE_UPLOADS"] = "/Users/new/PycharmProjects/inventarizaciya_final/app/static/img/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG", "JPG", "JPEG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5*1024*1024

def allowed_image(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_image_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            # if allowed_image_filesize(request.cookies.get("filesize")):
            #     print("File exceeded maximum size")
            #     return redirect(request.url)

            image = request.files["image"]

            if image.filename == "":
                print("Image must have a filename")
                return redirect(request.url)

            if not allowed_image(image.filename):
                print("That image extension is not allowed")
                return redirect(request.url)

            else:
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

            print("Image saved")
            print(image)

            return redirect(request.url)

    return render_template("admin/upload_image.html")

@app.route("/admin/product_count")
def product_count():
    return render_template("admin/product_count.html")

@app.route("/admin/table")
def table_element():
    headings = ( "Name", "Role",	"Salary")

    data = (
        ("Rolf Smith",	"Software Engineer",	"$42000"),
        ("Jonny Depp",	"Film Actor",	"$1000000000"),
        ("Steve Jobs",	"Apple Founder",	"$200000000"),
        ("Vitaliy Kalachev",	"Software Engineer",	"$100000"),
        ("Tom Hanks", "Film Actor", "$1000000000"),
        ("Artur Sita", "Englithment person", "$200000000000000000000000000"),
        ("Elon Musk", "Tesla Founder", "$1000000000"),
            )

    return render_template("admin/table.html", headings=headings, data=data)

@app.route("/admin/extract_data")
def extract_data_dobraw():
    headings = ("Name", "Surname", "Bhts", "Dobraw")
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cur.execute("SELECT NAME, SURNAME, BHT, DOBRAW FROM dobraw_count;")

            datas = cur.fetchall()


            # for data in datas:
            #     return(str(data[0]), str(data[1]), data[2], data[3],)
            print("Data selected successfully")


    def all_bhts_count():
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

                cur.execute("SELECT sum(cast(bht AS INTEGER)) FROM dobraw_count;")
                bhts = cur.fetchall()
                all_bhts = bhts[0][0]
        return all_bhts
    def all_dobraw_count():
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

                cur.execute("SELECT sum(cast(dobraw AS FLOAT)) FROM dobraw_count;")
                dobraw = cur.fetchall()
                all_dobraw = dobraw[0][0]
        return all_dobraw
    return render_template("admin/extract_data.html", headings=headings, datas=datas,
                           all_bhts_count=all_bhts_count, all_dobraw_count=all_dobraw_count
                           )

