from tkinter import *
import random

window = Tk()
window.geometry("800x500")
window.resizable(False, False)

choice = ""
scoreP = 0
scoreE = 0

def scissors():
    global choice
    global scoreP
    global scoreE
    enemy()
    if (choice == "ROCK"):
        status.config(text = "YOU LOSE")
        scoreE += 1
    elif (choice == "PAPER"):
        status.config(text = "YOU WIN")
        scoreP += 1
    else:
        status.config(text = "NONE")
    playerscore.config(text = f"YOUR SCORE: {scoreP}")
    enemyscore.config(text = f"ENEMY SCORE: {scoreE}")

def rock():
    global choice
    global scoreP
    global scoreE
    enemy()
    if (choice == "PAPER"):
        status.config(text = "YOU LOSE")
        scoreE += 1
    elif (choice == "SCISSORS"):
        status.config(text = "YOU WIN")
        scoreP += 1
    else:
        status.config(text = "NONE")
    playerscore.config(text = f"YOUR SCORE: {scoreP}")
    enemyscore.config(text = f"ENEMY SCORE: {scoreE}")

def paper():
    global choice
    global scoreP
    global scoreE
    enemy()
    if (choice == "SCISSORS"):
        status.config(text = "YOU LOSE")
        scoreE += 1
    elif (choice == "ROCK"):
        status.config(text = "YOU WIN")
        scoreP += 1
    else:
        status.config(text = "NONE")
    playerscore.config(text = f"YOUR SCORE: {scoreP}")
    enemyscore.config(text = f"ENEMY SCORE: {scoreE}")

def enemy():
    global choice
    choice = random.choice(["ROCK", "PAPER", "SCISSORS"])
    maintext.config(text = f"ENEMY CHOOSE: {choice}")

scisorrsbutton = Button(text = "SCISSORS", width = 15, command = scissors)
scisorrsbutton.grid(row = 0, column = 0)

rockbutton = Button(text = "ROCK", width = 15, command = rock)
rockbutton.grid(row = 0, column = 1, padx = 228)

paperbutton = Button(text = "PAPER", width = 15, command = paper)
paperbutton.grid(row = 0, column = 2)

maintext = Label(text = "ENEMY CHOOSE: ")
maintext.grid(row = 1, column = 1, pady = 200)

playerscore = Label(text = "YOUR SCORE: 0")
playerscore.grid(row = 1, column = 0)

enemyscore = Label(text = "ENEMY SCORE: 0")
enemyscore.grid(row = 1, column = 2)

status = Label(text = "")
status.grid(row = 2, column = 1)

window.mainloop()
