pl = {
    "Борщ": [180, 3.5],
    "Гоrawшковый суп": [180, 3.6],
    "Морковный карри": [200, 4],
    "Окрошка по-литовски": [190, 3.8]
}



bill_bhts = []
bill_dobraw = []

# list_of_key = for key in pl.items()
# product = input("Напиши: ")
def take_product_from_dict():
    product = input("Напиши: ")
    for products in pl.items():
        if product in products:
            bill_bhts.append(pl[product][0])
            bill_dobraw.append(pl[product][1])
        elif product not in products:
            continue
        else:
            break


for x in range(6):
    take_product_from_dict()
    if x == 2:
        break
    elif x != 3:
        continue
    else:
        print("Finally finished!")


total_bhts = sum(bill_bhts)
total_dobraw = sum(bill_dobraw)

print("Баты :", total_bhts, "Добро :", total_dobraw)





# final_bhts, final_dobraw = sum(bill_bhts), sum(bill_dobraw)

# print("Sum :", returnsum(pl))
    # print("pass")
    # print(bill[0][0], bill[0][1] )