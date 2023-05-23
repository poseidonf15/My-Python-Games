import tkinter
from tkinter import *
from cell import Cell
import settings

def close():
    window.destroy()

window = Tk()
window.resizable(False, False)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (settings.WIDTH / 2))
y = int((screen_height / 2) - (settings.HEIGHT / 2))

window.geometry(f"{settings.WIDTH}x{settings.HEIGHT}+{x}+{y}")

num = 0

for i in range (9):
    for l in range(9):
        c = Cell(l, i)
        c.create_btn_object()
        c.btn_object.grid(row = i, column = l)
        window.update()

for i in range (9):
    c = Cell(i, 9)
    c.create_choice_button()
    c.choice_btn_object.grid(row = 9, column = i)

c = Cell(0, 10)
c.create_clear_btn()
c.clear_btn_object.grid(row = 10, column = 0, columnspan = 3)

c = Cell(0, 10)
c.create_erase_btn()
c.erase_btn_object.grid(row = 10, column = 3, columnspan = 3)

close_btn_object = Button(text = "Close", width = 24, height = 3, bg = "#ccd9d0", activebackground = "#ccd9d0", activeforeground = "black", command = close)
close_btn_object.grid(row = 10, column = 6, columnspan = 3)




window.mainloop()