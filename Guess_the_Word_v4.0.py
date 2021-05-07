import random
import time
from colored import fg, attr
from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()
screen.setup(width=0.333, height=0.333, startx=1200, starty=100)
screen.bgcolor("black")
screen.title("Hangman")
turtle.speed(5)
turtle.color("red")

print(" ")
print('Herzlich Willkommen zu meinem "Guess the Word" Game!')

while next:

    turtle.pensize(2)
    turtle.penup()
    turtle.goto(-100, -100)
    turtle.showturtle()
    turtle.pendown()
    turtle.setheading(-90)

    turns = 10
    char = None

    white = fg('#bfbfbf') + attr('reset')
    green = fg('#008000') + attr('bold')
    yellow = fg('#808000') + attr('bold')
    red = fg('#ff0000') + attr('bold')

    dark_green = fg('#00ff00') + attr('bold')
    dark_red = fg('#800000') + attr('bold')

    easy = green + '"Easy"'
    medium = yellow + '"Medium"'
    hard = red + '"Hard"'

    comma = white + ", "

    print(" ")
    difficulty = input('Gebe den Schwierigkeitsgrad an (' + easy + comma + medium + comma + hard + white + '): ')
    while next:
        difficulty = difficulty.lower()
        if difficulty == "easy":
            difficulty = easy
            char = random.randint(4, 6)
            break
        elif difficulty == "medium":
            difficulty = medium
            char = random.randint(7, 10)
            break
        elif difficulty == "hard":
            difficulty = hard
            char = random.randint(11, 15)
            break
        else:
            print(" ")
            difficulty = input('Gebe einen gültigen Schwierigkeitsgrad an (' + easy + white + comma + medium
                               + comma + hard + white + '): ')

    print(" ")
    print("Gewählter Schwierigkeitsgrad: " + difficulty + white)

    print(" ")
    time.sleep(0.5)
    print("Ein zufälliges Wort wird ausgesucht...")
    time.sleep(1)

    wordslist = []
    with open("words.txt", "r", encoding="latin1") as f:
        for line in f:
            if len(line) == char:
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
            print(dark_red + "Dies ist kein gültiger Buchstabe!" + white)
            print(" ")
            guess = input("Gebe einen gültigen Buchstaben ein: ")
        else:
            guess = guess.lower()
            invalid = False
            break

    while turns > 0:
        guesses += guess

        if guess not in solution:
            turns -= 1
            print(dark_red + "Falsch" + white)
            time.sleep(0.25)
            print(" ")
            correct = False
        else:
            print(dark_green + "Richtig" + white)
            time.sleep(0.25)
            print(" ")
            correct = True

        if turns == 0:
            print("Lösungswort: " + solution.capitalize())
            print(" ")
            time.sleep(0.25)
            print(dark_red + "Du verlierst!" + white)

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
                time.sleep(0.25)
                print(dark_green + "Du gewinnst!" + white)
                turns = 0
            break

        if not correct:
            if turns == 9:
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
            nextround = input('Möchtest du nochmals eine Runde spielen? Schreibe ' + dark_green + '"J" für Ja'
                              + white + ' oder ' + dark_red + '"N" für Nein' + white + '! ')
            nextround = nextround.lower()
            if nextround == "j" or nextround == "ja":
                print(" ")
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
                    print(dark_red + "Dies ist kein gültiger Buchstabe!" + white)
                    print(" ")
                    guess = input("Gebe einen richtigen Buchstaben ein: ")
                    print(" ")
                else:
                    guess = guess.lower()
                    invalid = False
                    break
