import joystick
from interface import def1
from interface import def2
from interface import def3
from interface import def4
from interface import def5
from interface import def6
from interface import def7
from interface import def8
from interface import def9

def x():
    the_one = "x"
    joystick.radiox.config(state = "disabled")
    joystick.radioo.config(state = "disabled")
    joystick.button1.config(command = def1(), state = "normal")
    joystick.button2.config(command = def2(), state = "normal")
    joystick.button3.config(command = def3(), state = "normal")
    joystick.button4.config(command = def4(), state = "normal")
    joystick.button5.config(command = def5(), state = "normal")
    joystick.button6.config(command = def6(), state = "normal")
    joystick.button7.config(command = def7(), state = "normal")
    joystick.button9.config(command = def9(), state = "normal")

def  o():
    the_one = "o"
    joystick.radiox.config(state = "disabled")
    joystick.radioo.config(state = "disabled")
    joystick.button1.config(command = def1(), state = "normal")
    joystick.button2.config(command = def2(), state = "normal")
    joystick.button3.config(command = def3(), state = "normal")
    joystick.button4.config(command = def4(), state = "normal")
    joystick.button5.config(command = def5(), state = "normal")
    joystick.button6.config(command = def6(), state = "normal")
    joystick.button7.config(command = def7(), state = "normal")
    joystick.button8.config(command = def8(), state = "normal")
    joystick.button9.config(command = def9(), state = "normal")

joystick.choise.set("none")
joystick.radiox.config(command = x)
joystick.radioo.config(command = o)

joystick.window.mainloop()          
