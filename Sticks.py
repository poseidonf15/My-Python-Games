from tkinter import *
import random

window = Tk()
window.geometry("400x300")
window.title("Sticks")

sticks = 50
def computer():
    global sticks
    if (sticks % 4 == 0):
        sticks -= 3
    elif (sticks % 4 == 3):
        sticks -= 2
    elif (sticks % 4 == 2):
        sticks -= 1
    else:
        sticks -= random.randint(1,3)
    if (sticks == 1):
        label_sticks.config(text = sticks * "|")
        status.config(text = "Computer won!", fg = "red")
        button.config(state = DISABLED)
    else:
        label_sticks.config(text = sticks * "|")
        status.config(text = sticks)
        label_move.config(text = "Enter the number between 1 and 3")
        button.config(state = ACTIVE)

def player():
    global sticks
    if (sticks > int(entry_sticks.get())):
        if (int(entry_sticks.get()) == 1 or int(entry_sticks.get()) == 2 or int(entry_sticks.get()) == 3):
            sticks -= int(entry_sticks.get())
            label_sticks.config(text = sticks * "|")
            status.config(text = sticks)
            if (sticks == 1):
                status.config(text = "You won!", fg = "green")
                button.config(state = DISABLED)
            else:
                button.config(state = DISABLED)
                label_move.config(text = "Computer's turn, wait please!")
                window.after(2000, computer)

label_move = Label(text = "Enter the number between 1 and 3", font = ("Arial",15,"bold"))
label_move.pack(side = TOP)

entry_sticks = Entry(font = ("Arial", 15, "bold"), justify = CENTER)
entry_sticks.pack(side = TOP, pady = 10)

label_sticks = Label(text = (sticks * "|"), font = ("Arial", 30, "bold"))
label_sticks.pack(side = TOP)

status = Label(text = sticks, font = ("Arial", 30, "bold"))
status.pack(side = TOP, pady = 10)

button = Button(text = "Take sticks", font = ("Ariel", 15, "bold"), command = player)
button.pack(side = TOP)

window.mainloop()
