from flask import Flask, redirect, url_for, render_template, request
import os
from script import DB_NAME, DB_USER, DB_HOST, DB_PASS
import psycopg2.extras

from inventarizaciya import login
from list_counting_dobraw import adding_in_lists, contact, file_saving_process_to_csv, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/count_save", methods=["POST", "GET"])
def count_save():
    if request.method == "POST":
        adding_in_lists()
        contact()
        return redirect(url_for("count_save"))
    else:
        return render_template("count_save.html")




# @app.route("/count_save", methods=["POST", "GET"])
# def couunt_save_add_in_list():
#     return adding_in_lists()
#
# @app.route("/count_save", methods=["POST", "GET"])
# def couunt_save_data():
#     return contact()


@app.route("/inventarizaciya", methods=["POST", "GET"])
def inventarizaciya():
    return login()




if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0')




@app.route("/usr")
def user(usr):
    # f"<h1>{}</h1>"
    # f"<h1>{}</h1>"
    return render_template("usr.html")


