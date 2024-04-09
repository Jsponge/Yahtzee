import tkinter as tk
import turtle
import random

dice1=1
dice2=1
dice3=1
dice4=1
dice5=1
dice6=1
selected=2

# Different pages available
def changePage(root, player1, player2, player3, player4):
    global page
    # Clear the textbox

    if page == player1:
        page = player2
        root.title("Player 2")
        label1.config(text="Player 2")
    elif page == player2:
        page = player3
        root.title("Player 3")
        label1.config(text="Player 3")
    elif page == player3:
        page = player4
        root.title("Player 4")
        label1.config(text="Player 4")
    elif page == player4:
        page = player1
        root.title("Player 1")
        label1.config(text="Player 1")



def changePage2(root, player1, player2, player3, player4):
    global page
    # Clear the textbox

    if page == player1:
        page = player4
        root.title("Player 4")
        label1.config(text="Player 4")
    elif page == player2:
        page = player1
        root.title("Player 1")
        label1.config(text="Player 1")
    elif page == player3:
        page = player2
        root.title("Player 2")
        label1.config(text="Player 2")
    elif page == player4:
        page = player3
        root.title("player3")
        label1.config(text="Player 3")


def exitpage(root, leave):
    if leave == leave:
        root.destroy()

def roll():
    global dice1, dice2, dice3, dice4, dice5, dice6
    if dice1 != selected:
      dice1=random.randint(1,6)
      if dice2 != selected:
        dice2=random.randint(1,6)
    if dice3 != selected:
        dice3=random.randint(1,6)
    if dice4 != selected:
        dice4=random.randint(1,6)
    if dice5 != selected:
        dice5=random.randint(1,6)
    if dice6 != selected:
        dice6=random.randint(1,6)
    totalvalue=dice1+dice2+dice3+dice4+dice5+dice6
# def acesOnly():
#     global dice1, dice2, dice3, dice4, dice5, dice6
    
wn = turtle.Turtle()

wn.register_shape("C:\\Users\\iCan Student\\Desktop\\My work\\Sec 4\\Ican\\Python\\Yathzee\\dice\\dice side 1.gif")

dice1 = turtle.Turtle()
dice1.goto(0, 0)
dice1.shape("C:\\Users\\iCan Student\\Desktop\\My work\\Sec 4\\Ican\\Python\\Yathzee\\dice\\dice side 1.gif")
dice1.speed(0) 

root = tk.Tk()

root.geometry("550x585")
player1 = tk.Frame(root, bg="grey")
player2 = tk.Frame(root, bg="grey")
player3 = tk.Frame(root, bg="grey")
player4 = tk.Frame(root, bg="grey")

page = player1
root.title("Player 1")

buttonframe = tk.Frame(player1)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)
buttonframe.columnconfigure(4, weight=1)
buttonframe.columnconfigure(5, weight=1)
buttonframe.configure(bg="grey")

empty = tk.Label(buttonframe, bg="grey")
empty.grid(row=0, column=1, sticky=tk.W+tk.E)
empty = tk.Label(buttonframe, bg="grey")
empty.grid(row=2, column=1, sticky=tk.W+tk.E)
empty = tk.Label(buttonframe, bg="grey")
empty.grid(row=12, column=1, sticky=tk.W+tk.E)
empty = tk.Label(buttonframe, bg="grey")
empty.grid(row=14, column=1, sticky=tk.W+tk.E)


label = tk.Button(buttonframe, text="Yahtzee", font=('Arial', 22, 'bold'), bg="white")
label.grid(row=1, column=2, sticky=tk.W+tk.E)

# First label
label1 = tk.Button(buttonframe, height=1, font=('Arial', 16, 'bold', 'italic'), bg="white")
label1.config(text="Player 1")
label1.grid(row=1, column=5, sticky=tk.W+tk.E)

roll = tk.Button(buttonframe, height=1, text="Roll", command=lambda: roll(), font=('Arial', 16, 'bold', 'italic'), bg="white")
roll.grid(row=13, column=1, sticky=tk.W+tk.E)

leave = tk.Button(buttonframe, height=1, command=lambda: exitpage(root, leave), text="exit", font=('Arial', 18))
leave.grid(row=4, column=2, sticky=tk.W+tk.E)

btnl = tk.Button(buttonframe, text="<", command=lambda: changePage2(root, player1, player2, player3, player4), font=('Arial', 18))
btnl.grid(row=4, column=1, sticky=tk.W+tk.E)

btnr = tk.Button(buttonframe, text=">", command=lambda: changePage(root, player1, player2, player3, player4), font=('Arial', 18))
btnr.grid(row=4, column=5, sticky=tk.W+tk.E)

rules = tk.Button(buttonframe, text="Rules", command=lambda: (), font=('Arial', 18))
rules.grid(row=4, column=4, sticky=tk.W+tk.E)

number1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
number1.grid(row=5, column=1, sticky=tk.W+tk.E)
score1 = tk.Button(buttonframe, text="", command=lambda: (), font=('Arial', 18), bg="white")
score1.grid(row=5, column=2, sticky=tk.W+tk.E)

number2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
number2.grid(row=6, column=1, sticky=tk.W+tk.E)
score2 = tk.Button(buttonframe, text="", command=lambda: (), font=('Arial', 18), bg="white")
score2.grid(row=6, column=2, sticky=tk.W+tk.E)

number3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
number3.grid(row=7, column=1, sticky=tk.W+tk.E)
score3 = tk.Button(buttonframe, text="", command=lambda: (), font=('Arial', 18), bg="white")
score3.grid(row=7, column=2, sticky=tk.W+tk.E)

number4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
number4.grid(row=8, column=1, sticky=tk.W+tk.E)
score4 = tk.Button(buttonframe, text="", command=lambda: (), font=('Arial', 18), bg="white")
score4.grid(row=8, column=2, sticky=tk.W+tk.E)

number5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
number5.grid(row=9, column=1, sticky=tk.W+tk.E)
score5 = tk.Button(buttonframe, text="", command=lambda: (), font=('Arial', 18), bg="white")
score5.grid(row=9, column=2, sticky=tk.W+tk.E)

number6 = tk.Button(buttonframe, text="6", font=('Arial', 18))
number6.grid(row=10, column=1, sticky=tk.W+tk.E)
score6 = tk.Button(buttonframe, text="", command=lambda: (), font=('Arial', 18), bg="white")
score6.grid(row=10, column=2, sticky=tk.W+tk.E)

chance = tk.Button(buttonframe, text="Chance", font=('Arial', 18))
chance.grid(row=11, column=1, sticky=tk.W+tk.E)
score_chance = tk.Button(buttonframe, command=lambda: (), text="", font=('Arial', 18), bg="white")
score_chance.grid(row=11, column=2, sticky=tk.W+tk.E)

number3s = tk.Button(buttonframe, text="3 of a kind", font=('Arial', 18))
number3s.grid(row=5, column=4, sticky=tk.W+tk.E)
score3s = tk.Button(buttonframe, command=lambda: (), text="", font=('Arial', 18), bg="white")
score3s.grid(row=5, column=5, sticky=tk.W+tk.E)

number4s = tk.Button(buttonframe, text="4 of a kind", font=('Arial', 18))
number4s.grid(row=6, column=4, sticky=tk.W+tk.E)
score4s = tk.Button(buttonframe, command=lambda: (), text="", font=('Arial', 18), bg="white")
score4s.grid(row=6, column=5, sticky=tk.W+tk.E)

full = tk.Button(buttonframe, text="Full house", font=('Arial', 18))
full.grid(row=7, column=4, sticky=tk.W+tk.E)
score_full = tk.Button(buttonframe, command=lambda: (), text="", font=('Arial', 18), bg="white")
score_full.grid(row=7, column=5, sticky=tk.W+tk.E)

small = tk.Button(buttonframe, text="Small straight", font=('Arial', 18))
small.grid(row=8, column=4, sticky=tk.W+tk.E)
score_small = tk.Button(buttonframe, text="", command=lambda: (), font=('Arial', 18), bg="white")
score_small.grid(row=8, column=5, sticky=tk.W+tk.E)

large = tk.Button(buttonframe, text="Large straight", font=('Arial', 18))
large.grid(row=9, column=4, sticky=tk.W+tk.E)
score_large = tk.Button(buttonframe, text="", command=lambda: (), font=('Arial', 18), bg="white")
score_large.grid(row=9, column=5, sticky=tk.W+tk.E)

Yahtzee = tk.Button(buttonframe, text="Yahtzee", font=('Arial', 18))
Yahtzee.grid(row=10, column=4, sticky=tk.W+tk.E)
score_yahtzee = tk.Button(buttonframe, text="", command=lambda: (), font=('Arial', 18), bg="white")
score_yahtzee.grid(row=10, column=5, sticky=tk.W+tk.E)

total = tk.Button(buttonframe, text="Total", font=('Arial', 18))
total.grid(row=11, column=4, sticky=tk.W+tk.E)
total1 = tk.Button(buttonframe, text="", command=lambda: (), font=('Arial', 18), bg="white")
total1.grid(row=11, column=5, sticky=tk.W+tk.E)


dice1

dice2

dice3

dice4

dice5

buttonframe.grid(row=0, column=0, sticky=tk.W+tk.E)

# Pack all frames
player1.pack()
player2.pack()
player3.pack()
player4.pack()

root.mainloop()