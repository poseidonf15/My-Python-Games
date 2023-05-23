import turtle
import joystick
from main import the_one
"""
from computer import brain_x
from computer import brain_o
"""

a = turtle.Pen()
a.width(3)
a.speed(0)
a.left(180)

a.up()
a.goto(-50,150)
a.down()

a.goto(-50,-150)

a.up()
a.goto(50,150)
a.down()

a.goto(50,-150)

a.up()
a.goto(-150,50)
a.down()

a.goto(150,50)

a.up()
a.goto(-150,-50)
a.down()

a.goto(150,-50)

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn_num = 0

def def1():
    global turn_num
    global the_one
    global board
    joystick.button1.config(state = "disabled")
    board[0] = 1
    turn_num += 1
    if (the_one == x):
        draw_x(-140, 140)
    else:
        draw_o(-100, 140)

def def2():
    global turn_num
    global the_one
    global board
    joystick.button2.config(state = "disabled")
    board[1] = 1
    turn_num += 1
    if (the_one == x):
        draw_x(-40, 140)
    else:
        draw_o(0, 140)

def def3():
    global turn_num
    global the_one
    global board
    joystick.button3.config(state = "disabled")
    board[2] = 1
    turn_num += 1
    if (the_one == x):
        draw_x(60, 140)
    else:
        draw_o(100, 140)

def def4():
    global turn_num
    global the_one
    global board
    joystick.button4.config(state = "disabled")
    board[3] = 1
    turn_num += 1
    if (the_one == "x"):
        draw_x(-140, 40)
    else:
        draw_o(-100, 40)

def def5():
    global turn_num
    global the_one
    global board
    joystick.button5.config(state = "disabled")
    board[4] = 1
    turn_num += 1
    if (the_one == "x"):
        draw_x(-40, 40)
    else:
        draw_o(0, 40)

def def6():
    global turn_num
    global the_one
    global board
    joystick.button6.config(state = "disabled")
    board[5] = 1
    turn_num += 1
    if (the_one == "x"):
        draw_x(60, 140)
    else:
        draw_o(100, 140)

def def7():
    global turn_num
    global the_one
    global board
    joystick.button7.config(state = "disabled")
    board[6] = 1
    turn_num += 1
    if (the_one == "x"):
        draw_x(-140, 60)
    else:
        draw_o(-100, 60)

def def8():
    global turn_num
    global the_one
    global board
    joystick.button8.config(state = "disabled")
    board[7] = 1
    turn_num += 1
    if (the_one == "x"):
        draw_x(-40, -60)
    else:
        draw_o(0, -60)

def def9():
    global turn_num
    global the_one
    global board
    joystick.button9.config(state = "disabled")
    board[8] = 1
    turn_num += 1
    if (the_one == "x"):
        draw_x(60, -60)
    else:
        draw_o(100, -60)


def draw_o(num1, num2):
    a.up()
    a.goto(num1, num2)
    a.down()

    a.circle(40)

def draw_x(num1, num2):
    a.up()
    a.goto(num1, num2)
    a.down()

    a.goto(num1 + 80, num2 - 80)

    a.up()
    a.goto(num1, num2 - 80)
    a.down()

    a.goto(num1 + 80, num2)










    
