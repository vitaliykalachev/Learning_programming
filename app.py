from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/invent")
def invent():

    return render_template("invent.html")
    """<form action="" method="get">
                <input type="text" name="Название">
                <input type="text" weight="Вес в граммах">
                <input type="submit" value="сохранить">
              </form>"""




@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        user_weight = request.form["wt"]

        user_weight = user_weight.replace('+', ' ')

        def max_numbers(user_weight):
            return sum([float(i) for i in user_weight.replace(',', '.').split()])

        all_weight = max_numbers(user_weight)

        def all_weight_numbers(all_weight, dec=0):
            prc = "{:." + str(dec) + "f}"  # first cast decimal as str
            # str format output is {:.3f}
            return prc.format(all_weight)

        user_weight = all_weight_numbers(all_weight)

        # user_and_weight = user, user_weight
        # for i in user_and_weight():
        #     if i == True:
        #         return user_and_weight()
        print(user, user_weight)

        def file_saving_process():
            name_save = user.lower()
            weight_save = user_weight
            filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")

            f = open(f"/Users/new/PycharmProjects/inventarizaciya_final/templates/files/{filename1}.csv", "w")

            f.write(f"\n {name_save}  {weight_save}")

            f.close()

        user_and_weight = user, user_weight

        def contact():
            if "save" in request.form:
                file_saving_process()
                print("save ok")

                return render_template("/loging.html")
                    # redirect(url_for("user", usr = user_and_weight))
            elif "cancel" in request.form:
                print("cancel saving process")
                return render_template('loging.html')
            else:
                return render_template('loging.html')

        contact()
        return redirect(url_for("login"))
        # return render_template("/login1")

        # return redirect(url_for("user", usr=user_and_weight))
        # return render_template('loging.html')

        # return render_template("loging.html")
        # user_and_weight = user, user_weight
        # return redirect(url_for("user", usr = user_and_weight))

        # return redirect(url_for("user", usr = user_and_weight))
                                              # and "user_weight", wght = user_weight))
    else:
        return render_template("loging.html")



if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0')




@app.route("/usr")
def user(usr):
    # f"<h1>{}</h1>"
    # f"<h1>{}</h1>"
    return render_template("usr.html")


