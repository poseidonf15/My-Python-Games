import random
from interface import board

def brain_x(i, no_num):
    global board
    if (i == 1):
        while (num in no_num):
            num = random.randint(0,10)
        board[num] = 1
            
        
        


def brain_o(i, no_num):

