import random
import time

print('Herzlich Willkommen zu meinem "Guess the Word" Game!')
print(" ")
time.sleep(0.5)
print("Ein zufälliges Wort wird ausgesucht...")
time.sleep(1)

#Liste mit Wörter
wordslist = []
with open("words.txt", "r") as f:
    for line in f:
        wordslist.extend(line.split())

len(wordslist) == 0
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

turns = 10
for i in range(turns):
    guesses += guess
    print()

    if guess not in solution:
        turns -= 1
        print("Falsch")
    else:
        print("Richtig")

    print("Du hast noch " + str(turns) + " Versuche")

    print("Lösungswort: ", end="")
    while turns > 0:
        failed = 0
        for char in solution:
            if char in guesses:
                print(char, end="")
            else:
                print("_", end="")
                failed += 1
        if failed == 0:
            print("Du gewinnst")
        break
    print(" (" + str(solutionlength) + " Buchstaben)")

    guess = input("Gebe einen anderen Buchstaben ein: ")
    guess = guess.lower()

    if turns == 0:
        print("Du verlierst")
        break