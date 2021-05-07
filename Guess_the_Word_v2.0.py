import random
import time

print(" ")
print('Herzlich Willkommen zu meinem "Guess the Word" Game!')

win = 0

while next:

    turns = 10

    print(" ")
    time.sleep(0.5)
    print("Ein zufälliges Wort wird ausgesucht...")
    time.sleep(1)

    wordslist = []
    with open("words.txt", "r") as f:
        for line in f:
            wordslist.extend(line.split())

    wordslength = len(wordslist)
    wordslength -= 1
    solution = random.randint(0, wordslength)
    solution = wordslist[solution]
    solution = solution.lower()
    solutionlength = len(solution)

    guesses = ""

    print("Lösungswort: " + ("_"*solutionlength) + " (" + str(solutionlength) + " Buchstaben)")
    guess = input("Gebe einen Buchstaben ein: ")
    guess = guess.lower()

    while turns > 0:
        guesses += guess
        print()

        if guess not in solution:
            turns -= 1
            time.sleep(0.5)
            print("\u001b[38;5;160m" + "Falsch" + "\u001b[0m")
            print(" ")
        else:
            time.sleep(0.5)
            print("\u001b[38;5;40m" + "Richtig" + "\u001b[0m")
            print(" ")

        if turns == 0:
            if win == 0:
                turns = 0
                time.sleep(1)
                print("\u001b[38;5;160m" + "Du verlierst!" + "\u001b[0m")

        while turns > 0:
            failed = 0
            print("Lösungswort: ", end="")
            for char in solution:
                if char in guesses:
                    print(char, end="")
                else:
                    print("_", end="")
                    failed += 1
            if failed == 0:
                turns -= 1
                print("", end="\n")
                print(" ")
                time.sleep(1)
                print("\u001b[38;5;40m" + "Du gewinnst!" + "\u001b[0m")
                turns = 0
            break

        if turns == 0:
            print(" ")
            time.sleep(1)
            nextround = input('Möchtest du nochmals eine Runde spielen? Gebe "J" für Ja ein oder "N" für Nein! ')
            if nextround == "J" or nextround == "j":
                break
            else:
                print("Vielen Dank fürs spielen!")
                quit()

        else:
            print(" (" + str(solutionlength) + " Buchstaben)")

            print("Du hast noch " + str(turns) + " Versuche!")

            guess = input("Gebe einen anderen Buchstaben ein: ")
            guess = guess.lower()
