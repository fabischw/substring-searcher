# Spiel, bei welchem geraten wird, wie viele Wörter es im Deutschen mit gewissen Wörtern drin gibt.

import random

possible_subwords_arr = [
    "schul",
    "apfel",
    "schiff",
    "boot",
    "papier",
    "haus",
    "toilette",
    "tisch",
    "stuhl",
    "hobel",
    "bank",
    "geld",
    "finanz",
    "holz",
    "metall",
    "gerüst",
    "eisen",
    "baum",
    "schüler",
    "lehrer",
    "arbeit",
    "zahl",
    "stahl",
    "vogel",
    "neu",
    "kopf",
    "voll",
    "gehalt",
    "kontakt"
]



chosen_word_idx = random.randint(0,len(possible_subwords_arr)-1)

chosen_word = possible_subwords_arr[chosen_word_idx]

print("loading ... (this may take up to 2 minutes)")


#HIER GESUCHTE WÖRTER/BUCHSTABENFOLGEN IN DIE LISTE EINTRAGEN
searched_word_list = [chosen_word]#gesuchte Wörter

#HIER DATEI EINGEBEN, IN WELCHE DIE ERGEBNISSE GESPEICHERT WERDEN
targetfile = "reference.txt"#Detei, in welche Ergebnisse gespeichert werden

#HIER WÖRTER EINGEBEN, DIE HERUASGEFILTERT WERDEN SOLLEN 
excepted_words = []#Worte, welche aussortiert werden sollen

#HIER MAXIMALE LÄNGE EINGEBEN
max_len = None#Maximale Länge
if max_len == None:
    max_len = 10000000

success_count = 0 #Count für Anzahl an Treffern

#Deutsche Wortliste öffnen
with open("wordlist-german.txt") as file:
    data = file.readlines()

#Targetfile clearen
with open(targetfile,"w") as clearfile:
                clearfile.write("")

for searched_word in searched_word_list:

    #durch Datensatz loopen
    for element in data:
        if element.find(str(searched_word)) > -1:

            write = True

            #Prüfen, ob Wort in exception Liste ist
            for exceptions in excepted_words:
                if element.find(exceptions) > -1:
                    #print("flagged word: "+str(element))
                    write = False
                
            #Wort in targetfile schreiben
            if write == True and len(element) < max_len:
                success_count = success_count + 1
                print(element)
                file2 = open(targetfile, "a")
                file2.write(str(element))
                file2.close()

    file3 = open(targetfile,"a")
    file3.write("--------------------------\n")
    file3.close()

print("loading complete.")

print("Wie viele Wörter gibt es, die das Wort",chosen_word,"enthalten? ")

schaetzung = input("Schätzung abgeben: ")

try:
    schaetzung = int(schaetzung)
except ValueError:
    print("Eingabe ungültig, bitte geben Sie eine Zahl ein !")
    quit()

if schaetzung <= 0:
    print("Eingabe ungültig, bitte geben Sie eine Zahl ein !")
    quit()




percentage_off = schaetzung / success_count * 100

if percentage_off > 100:
    percentage_off = percentage_off - 100

points = round(percentage_off)


print("Die richtige Antwort lautet: ",str(success_count))

print("Sie haben",points,"Punkte gutgeschrieben bekommen.")


with open("punkte.txt","r") as file2:
    punkte_stored = file2.readlines()
    try:
        punkte_stored = int(punkte_stored)
    except:
        print("an error has occured while saving your points")
        quit()

with open("punkte.txt","r") as file3:
    file3.write(punkte_stored+points)