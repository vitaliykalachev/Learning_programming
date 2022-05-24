from flask import  render_template, request, flash
from app.admin_iventarizaciya import login
from app.list_counting_dobraw import adding_in_lists, contact, redirect, url_for
from app import app

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template("admin/dashboard.html")


@app.route("/admin/count_save", methods=["POST", "GET"])
def admin_count_save():
    if request.method == "POST":
        adding_in_lists()
        contact()
        return redirect(url_for("admin/count_save"))
    else:
        return render_template("admin/count_save.html")



@app.route("/admin/inventarizaciya", methods=["POST", "GET"])
def admin_inventarizaciya():
    return login()


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
    return render_template("admin/usr.html")
