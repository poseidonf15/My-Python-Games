from tkinter import *
from cell import Cell
import settings

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (settings.WIDTH/2))
y = int((screen_height/2) - (settings.HEIGHT/2))

root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}+{x}+{y}")
root.configure(bg = "black")
root.title("The Minesweeper")

top_frame = Frame(root, bg = "black", width = settings.WIDTH, height = settings.HEIGHT / 4)
top_frame.place(x = 0, y = 0)

game_title = Label(top_frame, bg = "black", fg = "white", text = "MineSweeper Game", font = ("", 48))
game_title.place(x = settings.WIDTH / 4)

left_frame = Frame(root, bg = "black", width = settings.WIDTH / 4, height = settings.HEIGHT - settings.HEIGHT / 4)
left_frame.place(x = 0, y = settings.HEIGHT / 4)

center_frame = Frame(root, bg = "black", width = settings.WIDTH / 100 * 75, height = settings.HEIGHT / 100 * 75)
center_frame.place(x = settings.WIDTH / 4, y = settings.HEIGHT / 4)

for x in range (settings.GRID_SIZE):
    for y in range (settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column = x, row = y)

Cell.create_cell_count_lable(left_frame)
Cell.cell_count_label_object.place(x = settings.WIDTH / 32, y = 0)
Cell.create_mine_count_lable(left_frame)
Cell.cell_mine_label_object.place(x = settings.WIDTH / 32, y = settings.HEIGHT / 4)

Cell.randomize_mines()

root.mainloop()