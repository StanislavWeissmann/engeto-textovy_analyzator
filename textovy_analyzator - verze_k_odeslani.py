'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Stanislav Weissmann
email: stana.ws@gmail.com
discord: Standa W.
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

print ("Enter username:")
prihlasovaci_jmeno = input()
print ("Enter password:")
heslo = input()

print()
print("$ python projekt1.py")

# slovník uživatelů s hesly
uzivatele = {"bob" : "123", "ann" : "pass123", "mike" : "password123", 
             "liz": "pass123"}

# kontrola uživatelů a hesel s přivítáním
if uzivatele.get(prihlasovaci_jmeno) == heslo:   
    print("username:", prihlasovaci_jmeno) 
    print("password:", heslo)
    print("-" * 40)
    print("Welcome to the app,", prihlasovaci_jmeno)
    print("We have 3 texts to be analyzed.")
    print("-" * 40)

else:
    print("username:", prihlasovaci_jmeno)
    print("password:", heslo) 
    print("unregistered user, terminating the program..")
    exit() 

# vložení čísla textu a kontrola
print ("Enter a number btw. 1 and 3 to select:")
cislo_textu = input()
print("-" * 40)
if not cislo_textu.isdigit():
    print("You did not enter a number.")
    exit()
if cislo_textu != "1" and cislo_textu != "2" and cislo_textu != "3":
    print("Invalid number.")
    exit()

# převod str na int z outputu... pořadí textu o 1 méně než číslo textu
poradi_textu = int(cislo_textu) - 1

# proměnné pro 1. polovinu úkolu
vyskyt_slov_s_velkym = 0
vyskyt_slov_jen_velka = 0
vyskyt_slov_jen_mala = 0
vyskyt_slov_jen_numeric = 0
soucet_cisel = 0

# slovník pro klíč - délka slova, hodnota - počet slov o dané délce
dict = {}

# vytvoření listu "prevod" z listu TEXTS - pouze zvolený text 
# a jednotlivé prvky jsou slova (i s tečkou a čárkou...) 
prevod = TEXTS[poradi_textu].split() 

# cyklus v novém listu: naplnění proměnných, proměnná a bude vždy obsahovat
# slovo z listu, proměnná W - převod čísla v textu na typ int.
# proměnná součet čísel počítá součet čísel v textu
for a in prevod:
    if a.istitle():
        vyskyt_slov_s_velkym = vyskyt_slov_s_velkym + 1
    if a.isupper() and a.isalpha():
        vyskyt_slov_jen_velka = vyskyt_slov_jen_velka + 1
    if a.islower():
        vyskyt_slov_jen_mala = vyskyt_slov_jen_mala + 1
    if a.isnumeric():
        vyskyt_slov_jen_numeric = vyskyt_slov_jen_numeric + 1
        w = int(a)
        soucet_cisel = soucet_cisel + w

# podmínka s kontrol. - jestliže slovo obsahuje . nebo , pak se délka slova 
# upravuje o -1, jinak je upravená délka totožná se skutečnou délkou
    if "." in a:
        upravena_delka = len(a) - 1
    elif "," in a:
        upravena_delka = len(a) - 1     
    else:
        upravena_delka = len(a)

# naplnění dict - podmínka, jestliže klíč, tj. upravená délka slova je v dict, 
# tak se hodnota zvýší o 1, pokud není v dict klíč, tak se vytvoří s hodnotou 
    if upravena_delka in dict.keys():
        dict [upravena_delka] = dict [upravena_delka] +1
    else:
        dict [upravena_delka] = 1 

# keys je list s klíči v dict (velikost slov), pak setřídění klíčů v sort_keys
keys = dict.keys() 
sort_keys = sorted(keys)

# vytvoření upraveného dict a v cyklu přiřazení hodnot setříděným klíčům
upraveny_dict = {}
for a in sort_keys:
    upraveny_dict [a] = dict [a]  
  
# tisky výsledků    
print ("There are", len(prevod), "words in the selected text.")
print("There are", vyskyt_slov_s_velkym, "titlecase words.")
print("There are", vyskyt_slov_jen_velka, "uppercase words.")
print("There are", vyskyt_slov_jen_mala, "lowercase words.")
print ("There are", vyskyt_slov_jen_numeric, "numeric strings.")
print ("The sum of all the numbers", soucet_cisel)

print("-" *40)
print("LEN|       OCCURENCES      |NR.")
print("-" *40)

for a in upraveny_dict:
    if a < 10:
        print("", a, "|", "*" * upraveny_dict [a], 
              " " * (20-upraveny_dict [a]), "|", upraveny_dict [a])
    else:
        print(a, "|", "*" * upraveny_dict [a], 
              " " * (20-upraveny_dict [a]), "|", upraveny_dict [a])