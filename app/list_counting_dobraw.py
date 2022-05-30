import pandas as pd
from flask import Flask, redirect, url_for, render_template, request
import psycopg2.extras
import os
from script import DB_NAME, DB_USER, DB_HOST, DB_PASS

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

conn = psycopg2.connect(dbname = DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# names = ['Виталий', 'Антон', 'Анна']
# surnames = ['Калачёв','Хлестов', 'Вильгельм']
# bhts = [400, 500, 600]
# dobraws = [4.8,5.3,6.3]


# def list_counting():
#     if request.method == "POST":
#         name = request.form["nm"]
#         surnaname = request.form["srnm"]
#
#         product_weight = request.form["wt"]
#
#         product_weight = product_weight.replace('+', ' ')
def adding_in_lists():
    if request.method == "POST":

        name = request.form["nm"]
        # names.append(name)
        surname = request.form["srnm"]
        # surnames.append(surname)

        bht = request.form["bhts"]
        bht = bht.replace('+', ' ')
        def max_numbers(bht):
            return sum([float(i) for i in bht.replace(',', '.').split()])
        all_bhts = max_numbers(bht)
        def all_bhts_counting(all_bhts, dec=0):
            prc = "{:." + str(dec) + "f}"  # first cast decimal as str
            # str format output is {:.3f}
            return prc.format(all_bhts)
        all_bhts_counting_end = all_bhts_counting(all_bhts)
        # bhts.append(all_bhts_counting_end)

        dobraw = request.form["dbrw"]
        dobraw = dobraw.replace('+', ' ')
        def dobraw_float(dobraw):
            return sum([float(i) for i in dobraw.replace(',', '.').split()])
        all_dobraws = dobraw_float(dobraw)
        def all_dobraws_counting(all_dobraws, dec=1):
            prc = "{:." + str(dec) + "f}"  # first cast decimal as str
            # str format output is {:.3f}
            return prc.format(all_dobraws)
        all_dobraws_counting_end = all_dobraws_counting(all_dobraws)
        # dobraws.append(all_dobraws_counting_end)
        # dobraws.append(dobraw)

        print("Имена : ", name, "Фамилии : ", surname, "Баты : ", all_bhts_counting_end, "Добро :", all_dobraws_counting_end)

        def file_saving_process():
            with conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    name_save = name
                    surname_save = surname
                    bhts = all_bhts_counting_end
                    dobraw = all_dobraws_counting_end

                    cur.execute("INSERT INTO dobraw_count (name, surname, bht, dobraw) VALUES(%s, %s, %s, %s)",
                                ((name_save.lower()), (surname_save.lower()),
                                 int(bhts), float(dobraw)))

                    cur.execute("SELECT * FROM dobraw_count;")
                    print(cur.fetchall())

        def contact():
            request.method == "POST"
            if "save" in request.form:
                file_saving_process()
                print("ADMIN COUNT save ok")
                return
                # redirect(url_for("product_name", usr = user_and_weight))
            elif "cancel" in request.form:
                print("ADMIN cancel COUNT saving process")
                return
            else:
                return render_template('admin/count_save.html')
        contact()
    else:
        return
    return
        # redirect(url_for("count_save"))



# def file_saving_process_to_csv():
#     all_list = {'Имена': names,
#                 'Фамилии': surnames,
#                 'Баты': bhts,
#                 'Добро': dobraws}
#     df = pd.DataFrame(all_list)
#     try:
#         df.to_csv('list.csv')
#         print(df)
#     except:
#         pass
#





# contact()

# print(df)



# print(df['Баты'].sum()," Бат" )
# print(df['Добро'].sum(), " Добра ")


# df.to_csv('list.csv')



# print(df.describe())
# df = pd.read_csv('list.csv')
# df.drop([0])





# new_cols = ({names['Имена'],
#             surnames['Фамилии'],
#             bhts['Баты'],
#             dobraws['Добро']})
# df.to_csv('list.csv', columns=new_cols() )
#
# df.read_csv('list.csv')

# df.to_csv(all_list)






# weight_save = user_weight
# filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
#
# f = open(f"/Users/new/PycharmProjects/inventarizaciya_final/templates/files/{filename1}.csv", "w")
#
# f.write(f"\n {name_save}  {weight_save}")
#
# f.close()

# user_and_weight = product_name, product_weight