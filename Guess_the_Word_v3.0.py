import random
import time
from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()
screen.setup(width=0.333, height=0.333, startx=1200, starty=100)
screen.bgcolor("black")
screen.title("Hangman")
turtle.color("red")

print(" ")
print('Herzlich Willkommen zu meinem "Guess the Word" Game!')

while next:

    turtle.pensize(2)
    turtle.penup()
    turtle.goto(-100, -100)
    turtle.showturtle()
    turtle.pendown()

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

    print("Lösungswort: " + ("_" * solutionlength) + " (" + str(solutionlength) + " Buchstaben)")

    invalid = True

    guess = input("Gebe einen Buchstaben ein: ")

    while invalid:
        if not guess.isalpha():
            print(" ")
            print("\u001b[38;5;160m" + "Dies ist kein gültiger Buchstabe!" + "\u001b[0m")
            print(" ")
            guess = input("Gebe einen gültigen Buchstaben ein: ")
            print(" ")
        else:
            guess = guess.lower()
            invalid = False
            break

    while turns > 0:
        guesses += guess
        print()

        if guess not in solution:
            turns -= 1
            print("\u001b[38;5;160m" + "Falsch" + "\u001b[0m")
            time.sleep(0.5)
            print(" ")
            correct = False
        else:
            print("\u001b[38;5;40m" + "Richtig" + "\u001b[0m")
            time.sleep(0.5)
            print(" ")
            correct = True

        if turns == 0:
            print("Lösungswort: " + solution)
            print(" ")
            time.sleep(0.5)
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
                time.sleep(0.5)
                print("\u001b[38;5;40m" + "Du gewinnst!" + "\u001b[0m")
                turns = 0
            break

        if not correct:
            if turns == 9:
                turtle.right(90)
                turtle.circle(50, -180)
            elif turns == 8:
                turtle.circle(50, 90)
                turtle.right(90)
                turtle.forward(200)
            elif turns == 7:
                turtle.right(90)
                turtle.forward(100)
            elif turns == 6:
                turtle.right(90)
                turtle.forward(50)
            elif turns == 5:
                turtle.right(90)
                turtle.circle(30)
                turtle.circle(30, 180)
            elif turns == 4:
                turtle.right(90)
                turtle.forward(20)
            elif turns == 3:
                turtle.left(30)
                turtle.forward(20)
            elif turns == 2:
                turtle.back(20)
                turtle.right(60)
                turtle.forward(20)
            elif turns == 1:
                turtle.back(20)
                turtle.left(30)
                turtle.back(10)
                turtle.right(90)
                turtle.forward(10)
            elif turns == 0:
                turtle.right(180)
                turtle.forward(20)
                turtle.hideturtle()

        if turns == 0:
            print(" ")
            time.sleep(1)
            nextround = input('Möchtest du nochmals eine Runde spielen? Gebe "J" für Ja ein oder "N" für Nein! ')
            if nextround == "J" or nextround == "j":
                turtle.clear()
                break
            else:
                print("Vielen Dank fürs spielen!")
                quit()

        else:
            print(" (" + str(solutionlength) + " Buchstaben)")
            print("Du hast noch " + str(turns) + " Versuche!")

            invalid = True

            while invalid:
                guess = input("Gebe einen gültigen Buchstaben ein: ")
                if not guess.isalpha():
                    print(" ")
                    print("\u001b[38;5;160m" + "Dies ist kein gültiger Buchstabe!" + "\u001b[0m")
                    print(" ")
                    guess = input("Gebe einen richtigen Buchstaben ein: ")
                    print(" ")
                else:
                    guess = guess.lower()
                    invalid = False
                    break
