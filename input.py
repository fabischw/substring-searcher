#main file, bitte diese generelle Version verwenden, wenn genug Programmierkenntnisse vorhanden sind

import substring_searcher#Such-Modul importieren

#Eingabe Logik
def terminal_inpt():
    print("Willkommen zum vereinfachten Substring Searcher User-Input, bitte folgen Sie einfach den Anweisungen, um ihre Suchanfrage zu starten")

    #substring-Liste
    print("\n\n1. Schritt: Substring Liste erstellen.\nGeben Sie, wenn Sie dazu aufgefordert werden, den zu suchenden substring ein. Wenn sie keinen weiteren substring eingeben wollen, drücken Sie einfach Enter, ohne eine Eingabe zu tätigen")
    current_inpt = "DEFAULTINPUT"
    searched_word_list = []
    while current_inpt != "":
        current_inpt = input("Bitte nächsten Substring eingeben! ")
        if current_inpt != "":
            searched_word_list.append(current_inpt)

    #targetfile
    print("\n\n2. Schritt: Zieldatei auswählen.\nWenn Sie keine spezielle Zieldatei wählen möchten, drücken Sie einfach Enter, ohne eine Eingabe zu tätigen. Die Ergebnisse werden standartmäßig in der Datei 'results.txt' in diesem Ordner gespeichert.")
    targetfile = input("Bitte Zieldatei eingeben.")
    if targetfile == "":
        targetfile = "results.txt"

    #excepted_words
    print("\n\n3. Schritt: Exceptions Liste erstellen.\nGeben Sie, wenn Sie dazu aufgefordert werden, Wörter, welche Sie grundsätzlich aussortieren wollen ein. Wenn sie kein weiteres Wort / gar kein Wort eingeben wollen, drücken Sie einfach Enter, ohne eine Eingabe zu tätigen")
    current_inpt = "DEFAULTINPUT"
    excepted_words = []
    while current_inpt != "":
        current_inpt = input("Bitte nächstes Wort eingeben! ")
        if current_inpt != "":
            excepted_words.append(current_inpt)

    #maximale Länge
    print("\n\n4. Schritt: Maximale Länge der Ergebnisse festlegen.\n Wenn Sie keine Maximallänge eingeben wollen, drücken Sie einfach Enter, ohne eine Eingabe zu tätigen.")
    max_len = input("Maximallänge der Ergebnisse eingeben.")
    if max_len == "":
        max_len = None
    else:
        try:
            max_len = int(max_len)
            if max_len < 0:
                max_len = None
        except ValueError:
            max_len = None

    #minimale Länge
    print("\n\n5. Schritt: Minimale Länge der Ergebnisse festlegen.\n Wenn Sie keine Minimallänge eingeben wollen, drücken Sie einfach Enter, ohne eine Eingabe zu tätigen.")
    min_len = input("Minimallänge der Ergebnisse eingeben.")
    if min_len == "":
        min_len = None
    else:
        try:
            min_len = int(min_len)
            if min_len < 0:
                min_len = None
        except ValueError:
            min_len = None

    #console logs
    print("\n\n6. Schritt: console logs festlegen.\n")
    log_status = input("Möchten Sie, dass der komplette Prozessvorgang in der Konsole dokumentiert wird ? (j/n)")
    if log_status == "j":
        log_status = True
    else:
        log_status = False

    print("Prozess wird gestartet.")
    print(substring_searcher.searcher(searched_word_list,targetfile,excepted_words,max_len,min_len,log_status))
    

terminal_inpt()