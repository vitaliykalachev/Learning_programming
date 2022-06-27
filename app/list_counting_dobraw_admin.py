from flask import  render_template, request
import psycopg2.extras
import os
from script import DB_NAME, DB_USER, DB_HOST, DB_PASS, conn




cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


def adding_in_lists():
    if request.method == "POST":
        name = request.form["nm"]
        surname = request.form["srnm"]
        bht = request.form["bhts"]
        bht = bht.replace('+', ' ')
        def max_numbers(bht):
            return sum([float(i) for i in bht.replace(',', '.').split()])
        all_bhts = max_numbers(bht)
        def all_bhts_counting(all_bhts, dec=0):
            prc = "{:." + str(dec) + "f}"  # first cast decimal as str

            return prc.format(all_bhts)
        all_bhts_counting_end = all_bhts_counting(all_bhts)

        dobraw = request.form["dbrw"]
        dobraw = dobraw.replace('+', ' ')
        def dobraw_float(dobraw):
            return sum([float(i) for i in dobraw.replace(',', '.').split()])
        all_dobraws = dobraw_float(dobraw)
        def all_dobraws_counting(all_dobraws, dec=1):
            prc = "{:." + str(dec) + "f}"  # first cast decimal as str

            return prc.format(all_dobraws)
        all_dobraws_counting_end = all_dobraws_counting(all_dobraws)


        print("Имена : ", name, "Фамилии : ", surname, "Баты : ", all_bhts_counting_end, "Добро :", all_dobraws_counting_end)

        def file_saving_process():
            with conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    name_save = name
                    surname_save = surname
                    bhts = all_bhts_counting_end
                    dobraw = all_dobraws_counting_end

                    cur.execute("INSERT INTO dobraw_count (name, surname, bht, dobraw) VALUES(%s, %s, %s, %s)",
                                ((name_save.capitalize()), (surname_save.capitalize()),
                                 int(bhts), float(dobraw)))

                    cur.execute("SELECT * FROM dobraw_count;")
                    print(cur.fetchall())

        def contact():
            request.method == "POST"
            if "save" in request.form:
                file_saving_process()
                print("ADMIN COUNT save ok")
                return

            elif "cancel" in request.form:
                print("ADMIN cancel COUNT saving process")
                return
            else:
                return render_template('admin/count_save.html')
        contact()
    else:
        return

