from tkinter import *

window = Tk()
window.geometry("300x350")
window.title("joystick")

choise = IntVar()

radioo = Radiobutton(text = "o", variable = choise, value = 0)
radioo.grid(row = 0, column = 1)

radiox = Radiobutton(text = "x", variable = choise, value = 1)
radiox.grid(row = 1, column = 1)

button1 = Button(text = "1", font = 50, state = "disabled")
button1.grid(row = 2 , column = 0, pady = 55, padx = 50)

button2 = Button(text = "2", font = 50, state = "disabled")
button2.grid(row = 2 , column = 1)

button3 = Button(text = "3", font = 50, state = "disabled")
button3.grid(row = 2 , column = 2, padx = 50)

button4 = Button(text = "4", font = 50, state = "disabled")
button4.grid(row = 3 , column = 0)

button5 = Button(text = "5", font = 50, state = "disabled")
button5.grid(row = 3 , column = 1)

button6 = Button(text = "6", font = 50, state = "disabled")
button6.grid(row = 3 , column = 2)

button7 = Button(text = "7", font = 50, state = "disabled")
button7.grid(row = 4 , column = 0, pady = 55)

button8 = Button(text = "8", font = 50, state = "disabled")
button8.grid(row = 4 , column = 1)

button9 = Button(text = "9", font = 50, state = "disabled")
button9.grid(row = 4 , column = 2)

if __name__ == "__main__":
    window.mainloop()
