from tkinter import Button

class Cell():
    buttons = []
    chs_buttons = []
    chs_num = None
    red_marked = None

    def __init__(self, x, y):
        self.btn_object = None
        self.choice_btn_object = None
        self.x = x
        self.y = y
        self.num = 0


        if self.y < 3:
            if self.x < 6:
                if self.x < 3:
                    self.box = 1
                else:
                    self.box = 2
            else:
                self.box = 3
                
        elif self.y < 6:
            if self.x < 6:
                if self.x < 3:
                    self.box = 4
                else:
                    self.box = 5
            else:
                self.box = 6
                
        else:
            if self.x < 6:
                if self.x < 3:
                    self.box = 7
                else:
                    self.box = 8
            else:
                self.box = 9

    def create_btn_object(self):
        btn = Button(width = 7, height = 3, bg = "#ccd9d0", activebackground = "#ccd9d0", activeforeground = "black")
        self.btn_object = btn
        self.btn_object.bind("<Button-1>", self.button_click)
        Cell.buttons.append(self)

    def create_choice_button(self):
        choice_btn = Button(text = self.x + 1, width = 7, height = 3, bg = "#ccd9d0", activebackground = "#ccd9d0", activeforeground = "black")
        self.choice_btn_object = choice_btn
        self.choice_btn_object.bind("<Button-1>", self.choice_click)
        Cell.chs_buttons.append(self.choice_btn_object)

    @staticmethod
    def create_clear_btn():
        btn = Button(text = "Clear", width = 24, height = 3, bg = "#ccd9d0", activebackground = "#ccd9d0", activeforeground = "black", command = Cell.clear)
        Cell.clear_btn_object = btn

    @staticmethod
    def create_erase_btn():
        btn = Button(text = "Erase", width = 24, height = 3, bg = "#ccd9d0", activebackground = "#ccd9d0", activeforeground = "black", command = Cell.erase)
        Cell.erase_btn_object = btn

    def button_click(self, event):
        if Cell.chs_num != None:
            self.btn_object.config(text = Cell.chs_num)
            self.num = Cell.chs_num
            for button in Cell.buttons:
                button.btn_object.bind("<Button-1>", button.button_click)

            for button in Cell.buttons:
                if button != self and button.num == self.num:
                    if button.box == self.box or button.x == self.x or button.y == self.y:
                        self.btn_object.config(bg = "#cc1212")
                        for disabel_btn in Cell.buttons:
                            if disabel_btn != self and disabel_btn != button:
                                disabel_btn.btn_object.unbind("<Button-1>")
                        break
                    else:
                        self.btn_object.config(bg="#ccd9d0")
                else:
                    self.btn_object.config(bg = "#ccd9d0")
        else:
            self.btn_object.config(text = "", bg = "#ccd9d0")
            self.num = None


    def choice_click(self, event):
        for chs_button in Cell.chs_buttons:
            chs_button.config(bg = "#ccd9d0")
        Cell.erase_btn_object.config(bg = "#ccd9d0")
        self.choice_btn_object.config(bg = "#34e5eb")
        Cell.chs_num = self.x + 1

    @staticmethod
    def clear():
        for button in Cell.buttons:
            button.btn_object.config(text = "", bg = "#ccd9d0")
            button.num = 0

    @staticmethod
    def erase():
        for chs_button in Cell.chs_buttons:
            chs_button.config(bg = "#ccd9d0")
        Cell.erase_btn_object.config(bg = "#34e5eb")
        Cell.chs_num = None


