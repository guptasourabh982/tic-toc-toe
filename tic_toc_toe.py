from tkinter import *
from tkinter.messagebox import showinfo
from itertools import permutations
y = ""
x = 2
player1 = []
player2 = []

def define_sign(number):
    global y, x, player1, player2

    if number == 1:
        if x % 2 == 0:
            y = "X"
            player1.append(number)
            print(player1)
            b1.config(text=y, background="green")
        elif x%2 != 0:
            y = "O"
            player2.append(number)
            print(player2)
            b1.config(text=y, background="red")
        x+=1

    if number == 2:
        if x%2 == 0:
            y = "X"
            player1.append(number)
            print(player1)
            b2.config(text=y, background="green")
        elif x%2 != 0:
            y = "O"
            player2.append(number)
            print(player2)
            b2.config(text=y, background="red")
        x+=1

    if number == 3:
        if x%2 == 0:
            y = "X"
            player1.append(number)
            print(player1)
            b3.config(text=y, background="green")
        elif x%2 != 0:
            y = "O"
            player2.append(number)
            print(player2)
            b3.config(text=y, background="red")
        x+=1

    if number == 4:
        if x%2 == 0:
            y = "X"
            player1.append(number)
            print(player1)
            b4.config(text=y, background="green")
        elif x%2 != 0:
            y = "O"
            player2.append(number)
            print(player2)
            b4.config(text=y,background="red")
        x+=1

    if number == 5:
        if x%2 == 0:
            y = "X"
            player1.append(number)
            print(player1)
            b5.config(text=y, background="green")
        elif x%2 != 0:
            y = "O"
            player2.append(number)
            print(player2)
            b5.config(text=y, background="red")
        x+=1

    if number == 6:
        if x%2 == 0:
            y = "X"
            player1.append(number)
            print(player1)
            b6.config(text=y, background="green")
        elif x%2 != 0:
            y = "O"
            player2.append(number)
            print(player2)
            b6.config(text=y, background="red")
        x+=1

    if number == 7:
        if x%2 == 0:
            y = "X"
            player1.append(number)
            print(player1)
            b7.config(text=y, background="green")
        elif x%2 != 0:
            y = "O"
            player2.append(number)
            print(player2)
            b7.config(text=y, background="red")
        x+=1

    if number == 8:
        if x%2 == 0:
            y = "X"
            player1.append(number)
            print(player1)
            b8.config(text=y, background="green")
        elif x%2 != 0:
            y = "O"
            player2.append(number)
            print(player2)
            b8.config(text=y, background="red")
        x+=1

    if number == 9:
        if x%2 == 0:
            y = "X"
            player1.append(number)
            print(player1)
            b9.config(text=y, background="green")
        elif x%2 != 0:
            y = "O"
            player2.append(number)
            print(player2)
            b9.config(text=y, background="red")
        x+=1
    if len(player1) == 5 or len(player2) == 5:
        showinfo("Game Result", "Nobody wins")
        b1.config(text="", background="white")
        b2.config(text="", background="white")
        b3.config(text="", background="white")
        b4.config(text="", background="white")
        b5.config(text="", background="white")
        b6.config(text="", background="white")
        b7.config(text="", background="white")
        b8.config(text="", background="white")
        b9.config(text="", background="white")
        x = 2
        player1 = []
        player2 = []
        return

    set1 = permutations([1, 2, 3])
    set2 = permutations([4, 5, 6])
    set3 = permutations([7, 8, 9])
    set4 = permutations([1, 4, 7])
    set5 = permutations([2, 5, 8])
    set6 = permutations([3, 6, 9])
    set7 = permutations([1, 5, 9])
    set8 = permutations([3, 5, 7])

    for i in set1, set2, set3, set4, set5, set6, set7, set8:
        for j in list(i):
            plyr1 = all(elm in player1 for elm in j)
            plyr2 = all(elm in player2 for elm in j)

            if plyr1 == True:
                showinfo("Game Results", "Player 1 wins.")
                b1.config(text="", background="white")
                b2.config(text="", background="white")
                b3.config(text="", background="white")
                b4.config(text="", background="white")
                b5.config(text="", background="white")
                b6.config(text="", background="white")
                b7.config(text="", background="white")
                b8.config(text="", background="white")
                b9.config(text="", background="white")
                x = 2
                player1 = []
                player2 = []
                break
            elif plyr2 == True:
                showinfo("Game Results", "Player 2 wins.")
                b1.config(text="", background="white")
                b2.config(text="", background="white")
                b3.config(text="", background="white")
                b4.config(text="", background="white")
                b5.config(text="", background="white")
                b6.config(text="", background="white")
                b7.config(text="", background="white")
                b8.config(text="", background="white")
                b9.config(text="", background="white")
                x = 2
                player1 = []
                player2 = []
                break




root = Tk()
root.title("Tic-Toc-Toe")
l1 = Label(root, text="Player 1 : x ", font="TimesNewRoman 14 bold")
l1.grid(row=0, column=0)

l2 = Label(root, text=" Player 2 : O", font="TimesNewRoman 14 bold")
l2.grid(row=0, column=1)

b1 = Button(root, width=15, height=5, command=lambda:define_sign(1))
b1.grid(row=1, column=0)

b2 = Button(root, width=15, height=5, command=lambda:define_sign(2))
b2.grid(row=1, column=1)

b3 = Button(root, width=15, height=5, command=lambda:define_sign(3))
b3.grid(row=1, column=2)

b4 = Button(root, width=15, height=5, command=lambda:define_sign(4))
b4.grid(row=2, column=0)

b5 = Button(root, width=15, height=5, command=lambda:define_sign(5))
b5.grid(row=2, column=1)

b6 = Button(root, width=15, height=5,command=lambda:define_sign(6))
b6.grid(row=2, column=2)

b7 = Button(root, width=15, height=5, command=lambda:define_sign(7))
b7.grid(row=3, column=0)

b8 = Button(root, width=15, height=5, command=lambda:define_sign(8))
b8.grid(row=3, column=1)

b9 = Button(root, width=15, height=5, command=lambda:define_sign(9))
b9.grid(row=3, column=2)

root.mainloop()
