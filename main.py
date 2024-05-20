import docx
import time
from art import *
trobat = False
final = False

def reading(file, name):
    global trobat
    global text
    doc = docx.Document(file)
    text = []
    for par in doc.paragraphs:
        if name.lower() in par.text.lower():
            trobat = True
            text.append(par.text.lower())

def starting(num):
    global trobat
    global text
    global final
    if num == "1":
        name = input("Nom de la pel·lícula: ")
        print("")
        n = 1
        while(final == False):
            file = ("hd" + str(n) + ".docx")
            n += 1
            try:
                reading(file, name)
                if (trobat):
                    for x in text:
                        print("".join(str(x)) + ", està al disc dur número " + str(n - 1))

            except:
                if(trobat == False):
                    print("No s'ha trobat a cap word :(")
                final = True
    if num != "1":
        exit()

    if final == True:
        time.sleep(2)
        print("")
        print("Prem qualsevol tecla per sortir del programa")
        input("-->")

def menu():
    art = text2art("FILM      FINDER")
    print(art)
    print("Prem la tecla 1 si vols buscar una pel·lícula")
    print("Prem cualsevol altre tecla si vols sortir del programa")
    menuoption = input("--> ")
    starting(menuoption)

menu()