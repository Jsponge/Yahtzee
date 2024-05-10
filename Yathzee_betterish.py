import tkinter as tk
from tkinter import PhotoImage
import random
import webbrowser


totalSelected=False
total=0
dice1 = 1
dice2 = 1
dice3 = 1
dice4 = 1
dice5 = 1

dice1selected=False
dice2selected=False
dice3selected=False
dice4selected=False
dice5selected=False
acesselected=False
twoselected=False
threesused=False
fourselected=False
fiveselected=False
sixSelected=False
threeOfAKindSelected=False
fourOfAKindS=False
fullHouseSelected=False
smStraightSelected=False
lgStraightSelected=False
yahtzeeSelected=False
chanceSelected=False
cheatSelected=False
aces=0
twos=0
threes=0
fours=0
fives=0
sixes=0
aces1=0
twos2=0
threes3=0
fours4=0
fives5=0
sixes6=0
threekind=0
fourkind=0
full=0
sm=0
lg=0
yahtz=0
chancee=0

totalValue=0
diceRolled=0

def selectDice1():
    global dice1selected
    if dice1selected==False:
        dice1selected=True
        dice1_label.config(bg="blue")
    else:
        dice1selected=False
        dice1_label.config(bg="white")

def selectDice2():
    global dice2selected
    if dice2selected==False:
        dice2selected=True
        dice2_label.config(bg="blue")
    else:
        dice2selected=False
        dice2_label.config(bg="white")

def selectDice3():
    global dice3selected
    if dice3selected==False:
        dice3selected=True
        dice3_label.config(bg="blue")
    else:
        dice3selected=False
        dice3_label.config(bg="white")
        
def selectDice4():
    global dice4selected
    if dice4selected==False:
        dice4selected=True
        dice4_label.config(bg="blue")
    else:
        dice4selected=False
        dice4_label.config(bg="white")


def selectDice5():
    global dice5selected, dice5color
    if dice5selected==False:
        dice5selected=True
        dice5_label.config(bg="blue")
    else:
        dice5selected=False
        dice5_label.config(bg="white")

def cheat():
    global cheatSelected, dice1, dice2, dice3, dice4, dice5
    cheatSelected=True

def roll():
    global dice1, dice2, dice3, dice4, dice5, aces, twos, threes, fours, fives, sixes, totalValue, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected, cheatSelected
    if cheatSelected == True:
        dice1=random.randint(1,6)
        dice2=dice1
        dice3=dice1
        dice4=dice1
        dice5=dice1
        cheatSelected=False
        dice1_label.config(image=dice_images[dice1-1])
        dice2_label.config(image=dice_images[dice2-1])
        dice3_label.config(image=dice_images[dice3-1])
        dice4_label.config(image=dice_images[dice4-1])
        dice5_label.config(image=dice_images[dice5-1])
    elif diceRolled<=2:
        if dice1selected==False:
            dice1=random.randint(1,6)
        if dice2selected==False:
            dice2=random.randint(1,6)
        if dice3selected==False:
            dice3=random.randint(1,6)
        if dice4selected==False:
            dice4=random.randint(1,6)
        if dice5selected==False:
            dice5=random.randint(1,6)
        totalValue=dice1+dice2+dice3+dice4+dice5
        diceRolled+=1
      
        dice1_label.config(image=dice_images[dice1-1])
        dice2_label.config(image=dice_images[dice2-1])
        dice3_label.config(image=dice_images[dice3-1])
        dice4_label.config(image=dice_images[dice4-1])
        dice5_label.config(image=dice_images[dice5-1])
        return totalValue
    
def aces2():
    global aces, acesselected, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected, aces1
    if acesselected==False and diceRolled!=0:
        aces=0
        diceList = [dice1, dice2, dice3, dice4, dice5]
        for d in diceList:
            if d==1:
                aces+=1
            d+=1
        aces1=0
        aces1=aces*1
        acesselected=True
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
        return aces1

def twos3():
    global twos, twos2, twoselected, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected
    if twoselected==False and diceRolled!=0:
        twos=0
        diceList = [dice1, dice2, dice3, dice4, dice5]
        for d in diceList:
            if d==2:
                twos+=1
            d+=1
        twos2=0
        twos2=twos*2
        twoselected=True
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
        return twos2

def threes4():
    global threes, threes3, threesused, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected
    if threesused==False and diceRolled!=0:
        threes=0
        diceList = [dice1, dice2, dice3, dice4, dice5]
        for d in diceList:
            if d==3:
                threes+=1
        threes3=0
        threes3=threes*3
        threesused=True
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
        return threes3

def fours5():
    global fours, fours4, fourselected, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected
    if fourselected==False and diceRolled!=0:
        fours=0
        diceList = [dice1, dice2, dice3, dice4, dice5]
        for d in diceList:
            if d==4:
                fours+=1
        fours4=0
        fours4=fours*4
        fourselected=True
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
        return fours4

def fives6():
    global fives, fives5, fiveselected, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected
    if fiveselected==False and diceRolled!=0:
        fives=0
        diceList = [dice1, dice2, dice3, dice4, dice5]
        for d in diceList:
            if d==5:
                fives+=1
        fives5=0
        fives5=fives*5
        fiveselected=True
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
        return fives5

def sixes7():
    global sixes, sixes6, sixSelected, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected
    if sixSelected==False and diceRolled!=0:
        sixes=0
        diceList = [dice1, dice2, dice3, dice4, dice5]
        for d in diceList:
            if d==6:
                sixes+=1
        sixes6=0
        sixes6=sixes*6
        sixSelected=True
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
        return sixes6

def threeOfAKind():
    global dice1, dice2, dice3, dice4, dice5, aces, twos, threes, fours, fives, sixes, totalValue, threeOfAKindSelected, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected, threekind
    threekind = 0
    if threeOfAKindSelected==False and diceRolled!=0:
        aces=0
        twos=0
        threes=0
        fours=0
        fives=0
        sixes=0
        diceList = [dice1, dice2, dice3, dice4, dice5]
        for d in diceList:
            if d==1:
                aces+=1
        for d in diceList:
            if d==2:
                twos+=1
        for d in diceList:
            if d==3:
                threes+=1
        for d in diceList:
            if d==4:
                fours+=1
        for d in diceList:
            if d==5:
                fives+=1
        for d in diceList:
            if d==6:
                sixes+=1
        threekind=0
        if aces >=3 or twos >=3 or threes >=3 or fours >=3 or fives >=3 or sixes>=3:
            threekind = totalValue
        threeOfAKindSelected=True
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
    return threekind

def fourOfAKind():
    global dice1, dice2, dice3, dice4, dice5, aces, twos, threes, fours, fives, sixes, totalValue, fourOfAKindS, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected, fourkind
    fourkind = 0
    if fourOfAKindS==False and diceRolled!=0:
        aces=0
        twos=0
        threes=0
        fours=0
        fives=0
        sixes=0
        diceList = [dice1, dice2, dice3, dice4, dice5]
        for d in diceList:
            if d==1:
                aces+=1
        for d in diceList:
            if d==2:
                twos+=1
        for d in diceList:
            if d==3:
                threes+=1
        for d in diceList:
            if d==4:
                fours+=1
        for d in diceList:
            if d==5:
                fives+=1
        for d in diceList:
            if d==6:
                sixes+=1
        fourkind=0
        if aces>=4 or twos>=4 or threes>=4 or fours>=4 or fives>=4 or sixes>=4:
            fourkind=totalValue
        fourOfAKindS=True
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
    return fourkind

def fullHouse():
    global dice1, dice2, dice3, dice4, dice5, aces, twos, threes, fours, fives, sixes, totalValue, fullHouseSelected, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected, full
    full=0
    if fullHouseSelected==False and diceRolled!=0:
        full=0
        diceList = [dice1, dice2, dice3, dice4, dice5]
        for d in diceList:
            if d==1:
                aces+=1
            d+=1
        for d in diceList:
            if d==2:
                twos+=1
            d+=1
        for d in diceList:
            if d==3:
                threes+=1
            d+=1
        for d in diceList:
            if d==4:
                fours+=1
            d+=1
        for d in diceList:
            if d==5:
                fives+=1
            d+=1
        for d in diceList:
            if d==6:
                sixes+=1
        if (aces==3 or twos==3 or threes==3 or fours==3 or fives==3 or sixes==3) and (aces==2 or twos==2 or threes==2 or fours==2 or fives==2 or sixes==2):
            full=25
        fullHouseSelected=True
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
        return full  

def smStraight():
    global dice1, dice2, dice3, dice4, dice5, smStraightSelected, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected, sm
    sm=0
    if smStraightSelected==False and diceRolled!=0:
        sm=0
        if ((dice1==1 or dice2==1 or dice3==1 or dice4==1 or dice5==1) and (dice1==2 or dice2==2 or dice3==2 or dice4==2 or dice5==2) and(dice1==3 or dice2==3 or dice3==3 or dice4==3 or dice5==3) and(dice1==4 or dice2==4 or dice3==4 or dice4==4 or dice5==4)) or ((dice1==5 or dice2==5 or dice3==5 or dice4==5 or dice5==5) and (dice1==2 or dice2==2 or dice3==2 or dice4==2 or dice5==2) and(dice1==3 or dice2==3 or dice3==3 or dice4==3 or dice5==3) and(dice1==4 or dice2==4 or dice3==4 or dice4==4 or dice5==4)) or ((dice1==5 or dice2==5 or dice3==5 or dice4==5 or dice5==5) and (dice1==6 or dice2==6 or dice3==6 or dice4==6 or dice5==6) and(dice1==3 or dice2==3 or dice3==3 or dice4==3 or dice5==3) and(dice1==4 or dice2==4 or dice3==4 or dice4==4 or dice5==4)):
            sm=30
        smStraightSelected=True
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
    return sm

def lgStraight():
    global dice1, dice2, dice3, dice4, dice5, lgStraightSelected, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected, lg
    lg=0
    if lgStraightSelected==False and diceRolled!=0:
        lg=0
        if ((dice1==1 or dice2==1 or dice3==1 or dice4==1 or dice5==1)and(dice1==5 or dice2==5 or dice3==5 or dice4==5 or dice5==5) and (dice1==2 or dice2==2 or dice3==2 or dice4==2 or dice5==2) and(dice1==3 or dice2==3 or dice3==3 or dice4==3 or dice5==3) and(dice1==4 or dice2==4 or dice3==4 or dice4==4 or dice5==4)) or ((dice1==5 or dice2==5 or dice3==5 or dice4==5 or dice5==5) and (dice1==6 or dice2==6 or dice3==6 or dice4==6 or dice5==6) and(dice1==3 or dice2==3 or dice3==3 or dice4==3 or dice5==3) and(dice1==4 or dice2==4 or dice3==4 or dice4==4 or dice5==4)and(dice1==2 or dice2==2 or dice3==2 or dice4==2 or dice5==2)):
            lg=40
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
        lgStraightSelected=True
    return lg

def yahtzee():
    global dice1, dice2, dice3, dice4,dice5, yahtzeeSelected, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected, yahtz
    yahtz=0
    if yahtzeeSelected==False and diceRolled!=0:
        yahtz=0
        if dice1==dice2 and dice2==dice3 and dice3==dice4 and dice4==dice5:
            yahtz=50
        yahtzeeSelected=True
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
    return yahtz

def chance1():
    global dice1, dice2, dice3, dice4,dice5, chanceSelected, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected, chancee
    chancee=0
    if chanceSelected==False and diceRolled!=0:
        chancee=0
        chancee=dice1+dice2+dice3+dice4+dice5
        chanceSelected=True
        diceRolled=0
        dice1selected=False
        dice2selected=False
        dice3selected=False
        dice4selected=False
        dice5selected=False
        dice1_label.config(bg="white")
        dice2_label.config(bg="white")
        dice3_label.config(bg="white")
        dice4_label.config(bg="white")
        dice5_label.config(bg="white")
    return chancee
        

# Different pages available
def changePage(root, player1, player2, player3, player4):
    global page
    # Clear the textbox

    if page == player1:
        page = player2
        root.title("Player 2")
        label1.config(text="Player 2", bg="orange")
    elif page == player2:
        page = player3
        root.title("Player 3")
        label1.config(text="Player 3", bg="green")
    elif page == player3:
        page = player4
        root.title("Player 4")
        label1.config(text="Player 4", bg="purple")
    elif page == player4:
        page = player1
        root.title("Player 1")
        label1.config(text="Player 1", bg="pink")


def changePage2(root, player1, player2, player3, player4):
    global page
    # Clear the textbox

    if page == player1:
        page = player4
        root.title("Player 4")
        label1.config(text="Player 4", bg="purple")
    elif page == player2:
        page = player1
        root.title("Player 1")
        label1.config(text="Player 1", bg="pink")
    elif page == player3:
        page = player2
        root.title("Player 2")
        label1.config(text="Player 2", bg="orange")
    elif page == player4:
        page = player3
        root.title("player3")
        label1.config(text="Player 3", bg="green")


def exitpage(root, leave):
    if leave == leave:
        root.destroy()

def openrules():
    url = 'https://www.officialgamerules.org/yahtzee'
    webbrowser.open_new(url)

def hehe():
    url = 'https://www.youtube.com/shorts/SXHMnicI6Pg'
    webbrowser.open_new(url)

def Total():
    global totalSelected, total, totalValue, diceRolled, dice1selected, dice2selected, dice3selected, dice4selected, dice5selected, aces1, twos2, threes3, fours4, fives5, sixes6, threekind, fourkind, full, sm, lg, chancee
    total=aces1+twos2+threes3+fours4+fives5+sixes6+threekind+fourkind+sm+lg+yahtz+chancee+full
    return total

root = tk.Tk()

root.geometry("800x800")
player1 = tk.Frame(root, bg="pink")
player2 = tk.Frame(root, bg="green")
player3 = tk.Frame(root, bg="purple")
player4 = tk.Frame(root, bg="orange")

page = player1
root.title("Player 1")

buttonframe = tk.Frame(player1)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)
buttonframe.columnconfigure(4, weight=1)
buttonframe.columnconfigure(5, weight=1)
buttonframe.columnconfigure(6, weight=1)
buttonframe.configure(bg="red")

empty = tk.Label(buttonframe, bg="red")
empty.grid(row=0, column=1, sticky=tk.W+tk.E)
empty = tk.Label(buttonframe, bg="red")
empty.grid(row=2, column=1, sticky=tk.W+tk.E)
empty = tk.Label(buttonframe, bg="red")
empty.grid(row=12, column=1, sticky=tk.W+tk.E)
empty = tk.Label(buttonframe, bg="red")
empty.grid(row=14, column=1, sticky=tk.W+tk.E)
empty = tk.Label(buttonframe, bg="red")
empty.grid(row=14, column=6, sticky=tk.W+tk.E)


label = tk.Button(buttonframe, text="Yahtzee", command=lambda: cheat() , font=('Arial', 22, 'bold'), bg="yellow")
label.grid(row=1, column=2, sticky=tk.W+tk.E)

# First label
label1 = tk.Button(buttonframe, command=lambda: hehe(), height=1, font=('Arial', 16, 'bold', 'italic'))
label1.config(text="Player 1", bg="pink")
label1.grid(row=1, column=5, sticky=tk.W+tk.E)

roll_button = tk.Button(buttonframe, height=1, text="-----Roll-----", command=roll, font=('Arial', 16, 'bold', 'italic'), bg="blue")
roll_button.grid(row=12, column=1, sticky=tk.W+tk.E)

leave = tk.Button(buttonframe, height=1, command=lambda: exitpage(root, leave), text="------exit------", font=('Arial', 18))
leave.grid(row=4, column=3, sticky=tk.W+tk.E)

btnl = tk.Button(buttonframe, text="<---------------", command=lambda: changePage2(root, player1, player2, player3, player4), font=('Arial', 18))
btnl.grid(row=4, column=2, sticky=tk.W+tk.E)

btnr = tk.Button(buttonframe, text="--------------->", command=lambda: changePage(root, player1, player2, player3, player4), font=('Arial', 18))
btnr.grid(row=4, column=5, sticky=tk.W+tk.E)

rules = tk.Button(buttonframe, text="-----Rule-----", command=lambda: openrules(), font=('Arial', 18))
rules.grid(row=4, column=4, sticky=tk.W+tk.E)

number1 = tk.Button(buttonframe, text="aces", font=('Arial', 18))
number1.grid(row=5, column=2, sticky=tk.W+tk.E)
score1 = tk.Button(buttonframe, command=lambda: update_score1(), font=('Arial', 18), bg="white")
score1.grid(row=5, column=3, sticky=tk.W+tk.E)

number2 = tk.Button(buttonframe, text="twos", font=('Arial', 18))
number2.grid(row=6, column=2, sticky=tk.W+tk.E)
score2 = tk.Button(buttonframe, command=lambda: update_score2(), font=('Arial', 18), bg="white")
score2.grid(row=6, column=3, sticky=tk.W+tk.E)

number3 = tk.Button(buttonframe, text="threes", font=('Arial', 18))
number3.grid(row=7, column=2, sticky=tk.W+tk.E)
score3 = tk.Button(buttonframe, command=lambda: update_score3(), font=('Arial', 18), bg="white")
score3.grid(row=7, column=3, sticky=tk.W+tk.E)

number4 = tk.Button(buttonframe, text="fours", font=('Arial', 18))
number4.grid(row=8, column=2, sticky=tk.W+tk.E)
score4 = tk.Button(buttonframe, command=lambda: update_score4(), font=('Arial', 18), bg="white")
score4.grid(row=8, column=3, sticky=tk.W+tk.E)

number5 = tk.Button(buttonframe, text="fives", font=('Arial', 18))
number5.grid(row=9, column=2, sticky=tk.W+tk.E)
score5 = tk.Button(buttonframe, command=lambda: update_score5(), font=('Arial', 18), bg="white")
score5.grid(row=9, column=3, sticky=tk.W+tk.E)

number6 = tk.Button(buttonframe, text="sixes", font=('Arial', 18))
number6.grid(row=10, column=2, sticky=tk.W+tk.E)
score6 = tk.Button(buttonframe, command=lambda: update_score6(), font=('Arial', 18), bg="white")
score6.grid(row=10, column=3, sticky=tk.W+tk.E)

chance = tk.Button(buttonframe, text="Chance", font=('Arial', 18))
chance.grid(row=11, column=2, sticky=tk.W+tk.E)
score_chance = tk.Button(buttonframe, command=lambda: update_chance(), font=('Arial', 18), bg="white")
score_chance.grid(row=11, column=3, sticky=tk.W+tk.E)

number3s = tk.Button(buttonframe, text="3 of a kind", font=('Arial', 18))
number3s.grid(row=5, column=4, sticky=tk.W+tk.E)
score3s = tk.Button(buttonframe, command=lambda: update_3s(), font=('Arial', 18), bg="white")
score3s.grid(row=5, column=5, sticky=tk.W+tk.E)

number4s = tk.Button(buttonframe, text="4 of a kind", font=('Arial', 18))
number4s.grid(row=6, column=4, sticky=tk.W+tk.E)
score4s = tk.Button(buttonframe, command=lambda: update_4s(), font=('Arial', 18), bg="white")
score4s.grid(row=6, column=5, sticky=tk.W+tk.E)

full = tk.Button(buttonframe, text="Full house", font=('Arial', 18))
full.grid(row=7, column=4, sticky=tk.W+tk.E)
score_full = tk.Button(buttonframe, command=lambda: update_full(), font=('Arial', 18), bg="white")
score_full.grid(row=7, column=5, sticky=tk.W+tk.E)

small = tk.Button(buttonframe, text="Small straight", font=('Arial', 18))
small.grid(row=8, column=4, sticky=tk.W+tk.E)
score_small = tk.Button(buttonframe, command=lambda: update_small(), font=('Arial', 18), bg="white")
score_small.grid(row=8, column=5, sticky=tk.W+tk.E)

large = tk.Button(buttonframe, text="Large straight", font=('Arial', 18))
large.grid(row=9, column=4, sticky=tk.W+tk.E)
score_large = tk.Button(buttonframe, command=lambda: update_large(), font=('Arial', 18), bg="white")
score_large.grid(row=9, column=5, sticky=tk.W+tk.E)

Yahtzee = tk.Button(buttonframe, text="Yahtzee", font=('Arial', 18))
Yahtzee.grid(row=10, column=4, sticky=tk.W+tk.E)
score_yahtzee = tk.Button(buttonframe, command=lambda: update_yahtzee(), font=('Arial', 18), bg="white")
score_yahtzee.grid(row=10, column=5, sticky=tk.W+tk.E)

total = tk.Button(buttonframe, text="Total", font=('Arial', 18))
total.grid(row=11, column=4, sticky=tk.W+tk.E)
total1 = tk.Button(buttonframe, command=lambda: update_total(), font=('Arial', 18), bg="white")
total1.grid(row=11, column=5, sticky=tk.W+tk.E)


dice_images = [
    PhotoImage(file="C:/Users/iCan Student/Downloads/MicrosoftTeams-image (5).gif"),
    PhotoImage(file="C:/Users/iCan Student/Downloads/MicrosoftTeams-image (7).gif"),
    PhotoImage(file="C:/Users/iCan Student/Downloads/MicrosoftTeams-image (4).gif"),
    PhotoImage(file="C:/Users/iCan Student/Downloads/MicrosoftTeams-image (8).gif"),
    PhotoImage(file="C:/Users/iCan Student/Downloads/MicrosoftTeams-image (6).gif"),
    PhotoImage(file="C:/Users/iCan Student/Downloads/MicrosoftTeams-image (3).gif")
]


dice1_label = tk.Button(buttonframe, command=lambda: selectDice1(), image=dice_images[dice1-1], bg="white")
dice1_label.grid(row=13, column=1, sticky=tk.W+tk.E)

dice2_label = tk.Button(buttonframe, command=lambda: selectDice2(), image=dice_images[dice2-1], bg="white")
dice2_label.grid(row=13, column=2, sticky=tk.W+tk.E)

dice3_label = tk.Button(buttonframe, command=lambda: selectDice3(), image=dice_images[dice3-1], bg="white")
dice3_label.grid(row=13, column=3, sticky=tk.W+tk.E)

dice4_label = tk.Button(buttonframe, command=lambda: selectDice4(), image=dice_images[dice4-1], bg="white")
dice4_label.grid(row=13, column=4, sticky=tk.W+tk.E)

dice5_label = tk.Button(buttonframe, command=lambda: selectDice5(),image=dice_images[dice5-1], bg="white")
dice5_label.grid(row=13, column=5, sticky=tk.W+tk.E)

def update_score1():
    score1.config(text=aces2())

def update_score2():
    score2.config(text=twos3())

def update_score3():
    score3.config(text=threes4())

def update_score4():
    score4.config(text=fours5())

def update_score5():
    score5.config(text=fives6())

def update_score6():
    score6.config(text=sixes7())

def update_chance():
    score_chance.config(text=chance1())

def update_3s():
    score3s.config(text=threeOfAKind())

def update_4s():
    score4s.config(text=fourOfAKind())

def update_full():
    score_full.config(text=fullHouse())

def update_small():
    score_small.config(text=smStraight())

def update_large():
    score_large.config(text=lgStraight())

def update_yahtzee():
    score_yahtzee.config(text=yahtzee())

def update_total():
    total1.config(text=Total())
# Call this function after each roll or when the player selects a category.

buttonframe.grid(row=0, column=0, sticky=tk.W+tk.E)


# Pack all frames
player1.pack()
player2.pack()
player3.pack()
player4.pack()

root.mainloop()