from flask import Flask, redirect, url_for, render_template, request, flash
import os
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
    # if request.method == "POST":
    #
    #     # req = request.form
    #
    #     # username = req.get("nm")
    #     # email = req.get("email")
    #     # password = req.get("nm")
    #
    #     if "save" in request.form:
    #         flash("Сохраняю!", "success")
    #         return render_template("loging.html")
    #     else:
    #         flash("Отмена!", "warning")
    #         return render_template("loging.html")
    #
    # return render_template("loging.html")


# Message flashing

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form

        username = req.get("username")
        email = req.get("email")
        password = req.get("password")

        if not len(password) >= 10:
            flash("Password length must be at least 10 characters", "warning")
            return render_template("sign_up.html")
        else:
            flash("Account created!", "success")
            return render_template("sign_up.html")

    return render_template("sign_up.html")

if __name__ == "__main__":
    app.secret_key = "super secret key"

    app.run(debug=True)
    # app.run(host='0.0.0.0')




@app.route("/usr")
def user(usr):
    # f"<h1>{}</h1>"
    # f"<h1>{}</h1>"
    return render_template("usr.html")


