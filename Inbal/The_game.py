from tkinter import *
from cell import Cell
import settings

window = Tk()
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
# window.geometry(f"{settings.WIDTH}x{settings.HEIGHT}+{int((screen_width/2) - (settings.WIDTH/2))}+{int((screen_height/2) - (settings.HEIGHT/2))}")
window.configure(bg = "black")
window.attributes("full-screen", True)

left_frame = LabelFrame(window, width = settings.WIDTH // 4 * 3)
left_frame.place(x = 0, y = 0)

right_frame = LabelFrame(window, width = settings.WIDTH // 4, height = settings.HEIGHT, bg = "black", relief = FLAT)
right_frame.place(x = settings.WIDTH // 4 * 2, y = 0)


for y in range (settings.GRID_NUMBER):
    for x in range (settings.GRID_NUMBER):
        c = Cell(x, y)
        c.create_btn_object(left_frame)
        c.btn_object.grid(row = x, column = y)

Cell.create_missing_cells_count_label_object(right_frame)
Cell.create_clear_button_object(right_frame)
Cell.missing_cells_count_label_object.place(x = 0, y = 0)
Cell.clear_button_object.place(x = 0, y = 70)

window.mainloop()