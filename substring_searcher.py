def searcher(searched_word_list,targetfile,excepted_words,max_len,min_len,log_status):
    if min_len == None:
        min_len = 0

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
                        if log_status == True:
                            print("flagged word: "+str(element))
                        write = False
                    
                #Wort in targetfile schreiben
                if write == True and len(element) < max_len and len(element) > min_len:
                    success_count = success_count + 1
                    if log_status == True:
                        print(element)
                    file2 = open(targetfile, "a")
                    file2.write(str(element))
                    file2.close()

        file3 = open(targetfile,"a")
        file3.write("--------------------------\n")
        file3.close()

    if log_status == True:
        print("-------------------------------\n")
        print("Treffer: "+str(success_count))
    else:
        return("Aufgabe erfolgreich beendet")
