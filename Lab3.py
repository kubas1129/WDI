import random
import time
import os
import math

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def BoardAnim(x,y,execTime):
    board = [" o" * x for i in range(y)]
    cls()
    while(execTime > 0):
        for i in range(y):
            if (i < y - 1):
                board[y - 1 - i] = board[y - 2 - i]
            else:
                r = random.randint(0, x - 1)
                board[0] = r * " o" + " x" + (x - r - 1) * " o"

        for i in range(y):
            print(board[i])

        time.sleep(0.3)
        execTime -= 0.3;
        cls()


def GrowingSquare(x, y):
    if (x % 2 == 0): x += 1
    if (y % 2 == 0): y += 1
    #board = [[" o" for j in range(y)] for i in range(x)]
    board = [" o"*x for i in range(y)]
    cls()
    execTime = 5
    ys = math.floor(y/2)
    xs = math.floor(x/2)
    k = 0
    addAmount = 1
    rt = ys + k
    rb = ys - k
    ex = False
    rev = False
    while(not ex):

        for i in range(y):
            if(i >= rt and i <= rb):
                if(i == rt or i == rb):
                    board[i] = (" o" * int((x - addAmount)/2)) + (" x" * addAmount) + (" o" * int((x - addAmount)/2))
                else:
                    board[i] = (" o" * (xs - k)) + " x" + (" o" * (2*k-1)) + " x" + (" o" * (xs - k))



        print()
        for i in range(y):
            print(board[i])
        board = [" o" * x for i in range(y)]



        if(addAmount >= min(x,y)):
            rev = True
        if(addAmount <= 1):
            rev = False

        if(rev):
            addAmount -= 2
            k -= 1
            rt = ys - k
            rb = ys + k
        else:
            addAmount += 2
            k += 1
            rt = ys - k
            rb = ys + k


        time.sleep(0.3)
        execTime -= 0.3
        print("")
        cls()
        if(execTime <= 0):
            ex = True


def main():
    #BoardAnim(11,7,14)
    GrowingSquare(7,5)

main()