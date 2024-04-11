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

#import knihovny pro sys.exit
import sys

print("\n$ python projekt1.py")
prihlasovaci_jmeno = input("\nEnter username: ")
heslo = input("Enter password: ")

# slovník uživatelů s hesly
uzivatele = {"bob" : "123", "ann" : "pass123", "mike" : "password123", 
             "liz": "pass123"}

# kontrola uživatelů a hesel s přivítáním
if uzivatele.get(prihlasovaci_jmeno) == heslo:   
    print("-" * 40)
    print("Welcome to the app,", prihlasovaci_jmeno)
    print("We have 3 texts to be analyzed.")
    print("-" * 40)

else:
    print("unregistered user, terminating the program..")
    sys.exit()

# vložení čísla textu a kontrola
cislo_textu = input("Enter a number btw. 1 and 3 to select: ")
print("-" * 40)
if not cislo_textu.isdigit():
    print("You did not enter a number.")
    sys.exit()
if int(cislo_textu) not in range(0,4):
    print("Invalid number.")
    sys.exit()

# převod str na int z outputu... pořadí textu o 1 méně než číslo textu
poradi_textu = int(cislo_textu) - 1

# proměnné pro 1. polovinu úkolu v dict vyskyty
vyskyty = {"slova_s_velkym" : 0, "slova_jen_velka" : 0, 
           "slova_jen_mala" : 0, "slova_jen_numeric" : 0, "soucet_cisel" : 0}

# slovník pro klíč=délka slova, hodnota=počet slov o dané délce
analyzovane_delky = {}

# vytvoření listu "zvoleny_text" z listu TEXTS - pouze zvolený text 
# a jednotlivé prvky jsou slova (i s tečkou a čárkou...) 
zvoleny_text = TEXTS[poradi_textu].split() 

# přiřazení hodnot ke klíčům ve vyskyty, proměnná "a" bude vždy obsahovat
# slovo z listu, proměnná W - převod čísla v textu na typ int.
# proměnná součet čísel počítá součet čísel v textu 
for a in zvoleny_text:
    if a.istitle():
        vyskyty["slova_s_velkym"] = vyskyty.get("slova_s_velkym", 0) + 1
    if a.isupper() and a.isalpha():
        vyskyty["slova_jen_velka"] = vyskyty.get("slova_jen_velka", 0) + 1
    if a.islower():
        vyskyty["slova_jen_mala"] = vyskyty.get("slova_jen_mala", 0) + 1
    if a.isnumeric():
        vyskyty["slova_jen_numeric"] = vyskyty.get("slova_jen_numeric", 0) + 1
        w = int(a)
        vyskyty["soucet_cisel"] = vyskyty.get("soucet_cisel", 0) + w

# podmínka - jestliže slovo obsahuje "." nebo ",", pak se délka slova 
# upravuje o -1, jinak je upravená délka totožná se skutečnou délkou
    if "." in a or "," in a:
        upravena_delka = len(a) - 1
    else:
        upravena_delka = len(a)

# naplnění analyzovane_delky - upravené délky(velikosti slov) 
# a jejich výskyty (ještě pořád v cyklu pro každé slovo ze zvoleného textu)
    analyzovane_delky[upravena_delka] = analyzovane_delky.get(upravena_delka,0) +1
# a setřídění do nového dict
nove_analyzovane_delky = dict(sorted(analyzovane_delky.items()))
  
# tisky výsledků    
print ("There are", len(zvoleny_text), "words in the selected text.")
print("There are", vyskyty.get("slova_s_velkym"), "titlecase words.")
print("There are", vyskyty.get("slova_jen_velka"), "uppercase words.")
print("There are", vyskyty.get("slova_jen_mala"), "lowercase words.")
print ("There are", vyskyty.get("slova_jen_numeric"), "numeric strings.")
print ("The sum of all the numbers", vyskyty.get("soucet_cisel"))

print("-" *40)
print("LEN|       OCCURENCES      |NR.")
print("-" *40)

for a in nove_analyzovane_delky:
    if a < 10:
        print("", a, "|", "*" * nove_analyzovane_delky[a], 
              " " * (20-nove_analyzovane_delky[a]), "|", nove_analyzovane_delky[a])
    else:
        print(a, "|", "*" * nove_analyzovane_delky[a], 
              " " * (20-nove_analyzovane_delky[a]), "|", nove_analyzovane_delky[a])
