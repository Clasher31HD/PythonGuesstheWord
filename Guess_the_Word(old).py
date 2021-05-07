import random

#Beginn Game
print('Herzlich Willkommen zu meinem "Guess the Word" Game!')

versuche = 10
next = True

while next == True:
    print("Ein zufälliges Wort wird ausgesucht")

    #Liste mit Wörter
    wordslist = []
    with open("words.txt", "r") as f:
        for line in f:
            wordslist.extend(line.split())

    len(wordslist) == 0
    lenwörter = len(wordslist)
    lenwörter -= 1
    randomword = random.randint(0, lenwörter)

    #Zufälliges Wort aussuchen
    lösungswort = wordslist[randomword]
    lösungswort = lösungswort.lower()

    #Länge des Wortes herausfinden
    lösungswortlänge = len(lösungswort)
    untertrichlänge = lösungswortlänge*"_"
    untertrichlängesplit = list(untertrichlänge)

    #Länge des Wortes in unterstrichen ausgeben
    print("Lösungswort: " + untertrichlänge + " (" + str(lösungswortlänge) + " Buchstaben)")

    #Split Lösungswort in Buchstaben
    s = lösungswort
    zeichen = list(s)


    while versuche != 0:
        #Eingabe des Buchstabes oder Wortes
        guessstring = input("Gebe einen Buchstaben ein: ")
        guessstring = guessstring.lower()

        #Gratulationsnachricht
        if guessstring == lösungswort:
            print("\u001b[38;5;40m" + "Gratulation! Du hast das korrekte Wort erraten!" + "\u001b[0m")
            break

        #Überprüfe ob nur ein Buchstabe oder das Lösungswort eingegeben wurde
        elif len(guessstring) == 1:
            if guessstring in lösungswort:
                print("\u001b[38;5;40m" + "Der Buchstabe kommt im Wort vor! Versuche einen weiteren Buchstaben!" + "\u001b[0m")
                for zeichen in lösungswort:
                    zeichen += guessstring
                else:
                    zeichen += "_"

#                   deleteplace = lösungswort.index(guessstring)
#                   untertrichlängesplit[deleteplace] = guessstring
#                   del untertrichlängesplit[deleteplace]
#                   replaceword = untertrichlängesplit.insert(deleteplace, guessstring)
#                   untertrichlänge = "".join(untertrichlängesplit)
                print("Lösungswort: " + zeichen + " (" + str(lösungswortlänge) + " Buchstaben)")
                break
            else:
                print("\u001b[38;5;160m" + "Der Buchstabe kommt im Wort nicht vor! Versuche es Nochmal!" + "\u001b[0m")
                versuche -= 1
                print("Verbleibende Versuche: " + str(versuche))
                print("Lösungswort: " + untertrichlänge + " (" + str(lösungswortlänge) + " Buchstaben)")

        else:
            print("\u001b[38;5;160m" + "Dies ist nicht das richtige Wort!" + "\u001b[0m")
            versuche -= 1
            print("Verbleibende Versuche: " + str(versuche))

    #Nächste Runde?
    nextround = input('Möchtest du nochmals eine Runde spielen? Geb "J" für Ja ein oder "N" für Nein! ')
    if nextround == "J" or nextround == "j":
        next = True
        versuche = 10
    else:
        next = False
        print("Vielen Dank fürs spielen!")