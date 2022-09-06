#main file, bitte diese generelle Version verwenden, wenn genug Programmierkenntnisse vorhanden sind

#HIER GESUCHTE WÖRTER/BUCHSTABENFOLGEN IN DIE LISTE EINTRAGEN
searched_word_list = []#gesuchte Wörter

#HIER DATEI EINGEBEN, IN WELCHE DIE ERGEBNISSE GESPEICHERT WERDEN
targetfile = ""#Detei, in welche Ergebnisse gespeichert werden

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
                    print("flagged word: "+str(element))
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

print("-------------------------------\n")
print("Treffer: "+str(success_count))