import random

def create_lists():
    global lists
    lists = [["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
             ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
             ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
             ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
             ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
             ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
             ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
             ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
             ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
             ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"]]

def create_coordinates():
    global o_num
    global y
    global x
    while (True):
        y = random.randint(0, 9)
        x = random.randint(0, 9)
        empty_place = 0
        for i in range (0, 10):
            for l in range (0, 10):
                if lists[i][l] == "?":
                    empty_place += 1
        if (lists[y][x] == "?"):
            lists[y][x] = "o"
            o_num += 1
            break
        elif (empty_place == 0):
            break

def solve(num):
    global o_num
    o_num = 0
    create_lists()
    for i in range (num):
        create_coordinates()
        for y2 in range (0,10):
            for x2 in range (0,10):
                if (lists[y2][x2] != "o") and ((x2 == x) or (y2 == y) or (y2 + x2 == y + x) or (y2 - x2 == y - x)):
                    lists[y2][x2] = "x"

    if o_num == 10:
        finish = True
        print_lists()

def print_lists():
    for list in lists:
        print (list)
    print("\n")

finish = False

while (finish != True):
    solve(10)