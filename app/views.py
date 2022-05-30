from flask import  render_template, request, flash
from app.inventarizaciya import login
from app.list_counting_dobraw import adding_in_lists, redirect, url_for
from app import app

@app.route('/public/index')
def index():
    return render_template("public/index.html")


@app.route("/public/count_save", methods=["POST", "GET"])
def count_save():
    adding_in_lists()
    # if request.method == "POST":
    #
    #     contact()
    #     return redirect(url_for("public/count_save"))
    # else:
    #     return render_template("public/count_save.html")


@app.route("/public/admin_password")
def admin_password():
    return render_template("public/admin_password.html")

# @app.route("/count_save", methods=["POST", "GET"])
# def couunt_save_add_in_list():
#     return adding_in_lists()
#
# @app.route("/count_save", methods=["POST", "GET"])
# def couunt_save_data():
#     return contact()
# @app.route('/public/inventarizaciya', methods=["POST"])
# def collect():
#     if request.method =="POST":
#         userInput = request.form.get("userInput")
#     return render_template('public/inventarizaciya.html',userInput=userInput)

@app.route("/public/inventarizaciya", methods=["POST", "GET"])
def inventarizaciya():
    login()
    if "save" in request.form:
        flash("Данные сохранены", "success")
        print("FLASH PUBLIC save ok")
        return redirect(url_for("inventarizaciya"))
        # redirect(url_for("product_name", usr = user_and_weight))
    elif "cancel" in request.form:
        flash("Отмена", "warning")
        print("FLASH PUBLIC cancel saving process")
        return redirect(url_for("inventarizaciya"))
    else:
        return render_template('public/inventarizaciya.html')


@app.route("/public/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":

        req = request.form

        username = req.get("username")
        email = req.get("email")
        password = req.get("password")

        if not len(password) >= 10:
            flash("Password length must be at least 10 characters", "warning")
            return render_template("public/sign_up.html")
        else:
            flash("Account created!", "success")
            return render_template("public/sign_up.html")

    return render_template("public/sign_up.html")



@app.route("/public/<usr>")
def user(usr):
    f"<h1>{usr}</h1>"
    return render_template("public/usr.html")
