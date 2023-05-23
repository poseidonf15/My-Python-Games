from tkinter import Button, Label, messagebox, PhotoImage
import random
import settings
import sys

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    mine_count = settings.MINES_COUNT

    def __init__(self, x, y, is_mine = False):
        self.img = None
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        mine_img = PhotoImage(file = "Mine.png")
        self.mine_img = mine_img

        flag_img = PhotoImage(file="flag.png")
        self.flag_img = flag_img

        none = PhotoImage(file = "none.png")
        self.none = none

        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(location, image = self.none)
        btn.bind("<Button-1>", self.left_click_actions)
        btn.bind("<Button-3>", self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_lable(location):
        lbl1 = Label(location,
                    bg = "black",
                    fg = "white",
                    text = f"Cells left : {Cell.cell_count}",
                    font = ("", 30)
        )
        Cell.cell_count_label_object = lbl1

    @staticmethod
    def create_mine_count_lable(location):
        lbl2 = Label(location,
                    bg = "black",
                    fg = "white",
                    text = f"mines left : {Cell.mine_count}",
                    font = ("", 30)
        )
        Cell.cell_mine_label_object = lbl2

    def left_click_actions(self, event):
        self.left_click()

    def left_click(self):
        if self.is_mine:
            self.show_mine()
        elif self.is_opened:
            count = 0
            for cell_obj in self.surrounded_cells:
                if cell_obj.is_mine_candidate:
                    count += 1
            if self.surrounded_cells_mines_length == count:
                for cell_obj in self.surrounded_cells:
                    if not cell_obj.is_mine_candidate and not cell_obj.is_opened:
                        cell_obj.left_click()
            self.cell_btn_object.unbind("<Button-1>")
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    if cell_obj.surrounded_cells_mines_length == 0:
                        for cell_obj2 in cell_obj.surrounded_cells:
                            if cell_obj2.surrounded_cells_mines_length == 0:
                                for cell_obj3 in cell_obj2.surrounded_cells:
                                    if cell_obj3.surrounded_cells_mines_length == 0:
                                        for cell_obj4 in cell_obj3.surrounded_cells:
                                            cell_obj4.show_cell()
                                        cell_obj3.show_cell()
                            cell_obj2.show_cell()
                        cell_obj.show_cell()
            self.show_cell()

            if Cell.cell_count == settings.MINES_COUNT:
                messagebox.showinfo(title = "CONGRATULATIONS!", message = "You have won the game!!!")
                sys.exit()

        self.cell_btn_object.unbind("<Button-3>")

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.img = PhotoImage(file = f"{self.surrounded_cells_mines_length}.png")
            self.cell_btn_object.configure(image = self.img)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text = f"Cells left : {Cell.cell_count}")

        self.cell_btn_object.configure(bg = "SystemButtonFace")
        self.is_opened = True


    def show_mine(self):
        self.cell_btn_object.configure(image = self.mine_img)
        messagebox.showinfo(title = "BUSTED!", message = "You have lost the game!!!")
        sys.exit()

    def right_click_actions(self, event):
        if self.is_mine_candidate:
            self.cell_btn_object.configure(image = self.none)
            Cell.mine_count += 1
            if Cell.cell_mine_label_object:
                Cell.cell_mine_label_object.configure(text = f"Mines left : {Cell.mine_count}")
            self.is_mine_candidate = False
        else:
            self.cell_btn_object.configure(image = self.flag_img)
            Cell.mine_count -= 1
            if Cell.cell_mine_label_object:
                Cell.cell_mine_label_object.configure(text = f"Mines left : {Cell.mine_count}")
            self.is_mine_candidate = True

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, int(settings.MINES_COUNT))
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"