from tkinter import Button, Label
import settings

class Cell:
    missing_cells_count_label_object = None
    clear_button_object = None
    all = []
    missing_cells = settings.GRID_NUMBER

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.btn_object = None
        self.is_clicked = False
        self.turned_off_list = []
        self.red_marks = 0

    def create_btn_object(self, location):
        btn = Button(location, width = settings.BTN_WIDTH, height = settings.BTN_HEIGHT)
        self.btn_object = btn
        Cell.all.append(self)
        self.btn_object.bind("<Button-1>", self.right_click)

    @staticmethod
    def create_missing_cells_count_label_object(location):
        lbl = Label(location,
                    bg = "black",
                    fg = "white",
                    text = f"Cells left:{Cell.missing_cells}",
                    font = ("", 30)
        )
        Cell.missing_cells_count_label_object = lbl

    @staticmethod
    def create_clear_button_object(location):
        clear_btn = Button(location,
                    text="Clear",
                    font=("", 30),
                    )
        Cell.clear_button_object = clear_btn
        Cell.clear_button_object.bind("<Button-1>", Cell.clear)

    @staticmethod
    def clear(event):
        for cell in Cell.all:
            cell.is_clicked = False
            cell.turned_off_list = []
            cell.red_marks = 0
            Cell.missing_cells = settings.GRID_NUMBER
            Cell.missing_cells_count_label_object.configure(text = f"Cells left:{Cell.missing_cells}")
            cell.btn_object.configure(bg="SystemButtonFace")

    def right_click(self, event):
        if self.red_marks == 0:
            if not self.is_clicked:
                for cell in Cell.all:
                    if ((cell.x == self.x) or (cell.y == self.y) or (cell.y + cell.x == self.y + self.x) or (cell.y - cell.x == self.y - self.x)) and (cell.btn_object != self.btn_object):
                        self.turned_off_list.append(cell)
                        cell.red_marks += 1
                        cell.btn_object.configure(bg = "red")
                self.btn_object.configure(bg = "green")
                Cell.missing_cells -= 1
                Cell.missing_cells_count_label_object.configure(text = f"Cells left:{Cell.missing_cells}")
                self.is_clicked = True
            else:
                for cell in self.turned_off_list:
                    cell.red_marks -= 1
                    if cell.red_marks == 0:
                        cell.btn_object.configure(bg = "SystemButtonFace")
                self.turned_off_list = []
                self.btn_object.configure(bg="SystemButtonFace")
                Cell.missing_cells += 1
                Cell.missing_cells_count_label_object.configure(text = f"Cells left:{Cell.missing_cells}")
                self.is_clicked = False