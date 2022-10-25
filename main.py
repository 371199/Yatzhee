import tkinter as tk
from PIL import ImageTk, Image
import os
import random
import time
roll1 = None
window = tk.Tk()
d1 = tk.IntVar()
def roll():
    global d1
    global roll1,roll2,roll3,roll4,roll5
    if d1.get()==0:
        roll1 = random.choice([die1,die2,die3,die4,die5,die6])
    #roll1 = random.choice([die1,die2,die3,die4,die5,die6])
    roll2 = random.choice([die1,die2,die3,die4,die5,die6])
    roll3 = random.choice([die1,die2,die3,die4,die5,die6])
    roll4 = random.choice([die1,die2,die3,die4,die5,die6])
    roll5 = random.choice([die1,die2,die3,die4,die5,die6])
    spot1 = tk.Label(image = roll1)
    spot1.grid(row=1,column=0)

    spot2 = tk.Label(image = roll2)
    spot2.grid(row=1,column=1)

    spot3 = tk.Label(image = roll3)
    spot3.grid(row=1,column=2)

    spot4 = tk.Label(image = roll4)
    spot4.grid(row=1,column=3)

    spot5 = tk.Label(image = roll5)
    spot5.grid(row=1,column=4)

#################Dice Images#################
#################Dice Images#################
#################Dice Images#################
#################Dice Images#################
die1 = ImageTk.PhotoImage(Image.open("Die_1.png"))
die2 = ImageTk.PhotoImage(Image.open("Die_2.png"))
die3 = ImageTk.PhotoImage(Image.open("Die_3.png"))
die4 = ImageTk.PhotoImage(Image.open("Die_4.png"))
die5 = ImageTk.PhotoImage(Image.open("Die_5.png"))
die6 = ImageTk.PhotoImage(Image.open("Die_6.png"))

def toggleHold():
    global d1
    global roll1
    if d1.get()==0:
        roll1 = random.choice([die1,die2,die3,die4,die5,die6])



#roll1 = random.choice([die1,die2,die3,die4,die5,die6])

spot0 = tk.Label(text= "Yahtzee", bd=20, font = 25)
spot0.grid(row=0,column=0, columnspan=3)



rollButton = tk.Button(text="Roll!", command = roll)
rollButton.grid(row=3,column=0)

spot1 = tk.Checkbutton(text= "Keep", variable = d1, onvalue=1, offvalue=0)
spot1.grid(row=2,column=0)

spot2 = tk.Checkbutton(text= "Keep")
spot2.grid(row=2,column=1)

spot3 = tk.Checkbutton(text= "Keep")
spot3.grid(row=2,column=2)

spot4 = tk.Checkbutton(text= "Keep")
spot4.grid(row=2,column=3)

spot5 = tk.Checkbutton(text= "Keep")
spot5.grid(row=2,column=4)

window.mainloop()