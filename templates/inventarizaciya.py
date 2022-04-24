import os
from datetime import datetime



def all_process_restart(name, weight):
    name = ""
    name = str(input("Название: "))

    while name == "exit":
        print("Останавливаю программу, до встречи:)\n")
        exit()
    print(name)

    weight = str(input("Вес в граммах \n"
                       "(можно написать много поизций через пробел или через знак '+')\n"
                       ": "))
    while weight == "exit":
        print("Останавливаю программу, до встречи:)\n")
        exit()
    weight = weight.replace('+', ' ')


    def max_numbers(weight):
        return sum([float(i) for i in weight.replace(',', '.').split()])



    all_weight = max_numbers(weight)

    def all_weight_numbers(all_weight, dec=0):
        prc = "{:."+str(dec)+"f}" #first cast decimal as str
        #str format output is {:.3f}
        return prc.format(all_weight)


    weight = all_weight_numbers(all_weight)


    print(name, weight)

    def file_saving_process():
        name_save = name.lower()
        weight_save = weight
        filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")

        f = open(f"/Users/new/PycharmProjects/Flask_learning_freeCodeCamp — копия/files{filename1}.csv", "w")

        f.write(f"\n {name_save}  {weight_save}")

        f.close()


    yes = "да"

    # input("Сохранить да/нет?: ").lower()
    yes = True

    while True:
        yes = input("Сохранить, д/н?: ").lower()
        if yes == "да" :
            print("Отлично, сохраняю:)\n")
            file_saving_process()
            return all_process_restart()
            # break
        elif yes == "д" :
            print("Отлично, сохраняю:)\n")
            file_saving_process()
            return all_process_restart()
            # break
        elif yes == "y" :
            print("Отлично, сохраняю:)\n")
            file_saving_process()
            return all_process_restart()
            # break
        elif yes == "exit":
            print("Отлично, сохраняю и останавливаю программу, до встречи:)\n")
            file_saving_process()
            exit()
        elif NameError:
            print("Отмена. Введите данные заново, пожалуйста:)\n")
            return all_process_restart()
            # break
        else:
            print("Отмена. Введите данные заново, пожалуйста:)\n")
            return name
            # break

        break






# def name_or_exit():
#     name = ""
#     while name != "exit":
#         name = str(input("Название: "))
#         all_process_restart()
#     return
# name = ""
# while name != "exit":
#     all_process_restart()



