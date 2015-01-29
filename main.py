#####Main Class for The New World

from tkinter import *
from PIL import ImageTk, Image
import os, character

###Inital Frame Setup
frame = Tk()




###Setup characters

###Felix
FelixUpLeft = ImageTk.PhotoImage(Image.open("Chars/Felix/UpLeft.png"))
FelixUp = ImageTk.PhotoImage(Image.open("Chars/Felix/Up.png"))
FelixUpRight = ImageTk.PhotoImage(Image.open("Chars/Felix/UpRight.png"))                                

Felix = character.Char(FelixUp, FelixUpLeft, FelixUpRight,
                  FelixUp, FelixUpLeft, FelixUpRight,
                  FelixUp, FelixUpLeft, FelixUpRight,
                  FelixUp, FelixUpLeft, FelixUpRight,
                  frame=frame, firstImage="Up", isChar=True);


