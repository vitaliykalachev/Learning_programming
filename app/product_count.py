prod1 = {
  "name" : "Кесадилья со шпинатом",
  "bhts" : 220,
  "dobraw": 4.4
}
prod2 = {
  "name" : "Буррито с киноа, сырным соусом и авокадо",
  "bhts" : 250,
  "dobraw": 5
}

prod3 = {
  "name" : "Капуста Баффало",
  "bhts" : 270,
  "dobraw":5.4
}

prod4 = {
  "name" : "Бейгл c запеченной папайей и творожным сыром",
  "bhts" : 250,
  "dobraw":5
}

prod5 = {
  "name" : "Бургер с овощной котлетой",
  "bhts" : 250,
  "dobraw": 5
}

prod6 = {
  "name" : "Тортилья с грибами",
  "bhts" : 240,
  "dobraw":4.8
}

prod7 = {
  "name" : "Тако",
  "bhts" : 260,
  "dobraw": 5.2
}



print(f"{prod7} \n {prod6},\n {prod5}")


print("Bhts \n",prod7["bhts"] + prod6["bhts"] + prod5["bhts"])


print("Dobraw \n",prod7["dobraw"] + prod6["dobraw"] + prod5["dobraw"])
