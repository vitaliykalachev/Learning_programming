from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime
from script import DB_NAME, DB_USER,DB_HOST,DB_PASS
import psycopg2.extras

app = Flask(__name__)

conn = psycopg2.connect(dbname = DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
# cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


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
        product_name = request.form["nm"]
        product_weight = request.form["wt"]

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
                    # product_name = input("Введите название: ")
                    # user_weight = input("Введите вес: ")
                    cur.execute("INSERT INTO invent_april (name, weight) VALUES(%s, %s)", ((product_name.lower()), int(product_weight),))

                    cur.execute("SELECT * FROM invent_april;")
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
            if "save" in request.form:
                file_saving_process()
                print("save ok")

                return render_template("/loging.html")
                    # redirect(url_for("product_name", usr = user_and_weight))
            elif "cancel" in request.form:
                print("cancel saving process")
                return render_template('loging.html')
            else:
                return render_template('loging.html')

        contact()
        return redirect(url_for("login"))
        # return render_template("/login1")

        # return redirect(url_for("product_name", usr=user_and_weight))
        # return render_template('loging.html')

        # return render_template("loging.html")
        # user_and_weight = product_name, user_weight
        # return redirect(url_for("product_name", usr = user_and_weight))

        # return redirect(url_for("product_name", usr = user_and_weight))
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


