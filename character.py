##Character Class for 'The New World'

from tkinter import *
from PIL import ImageTk, Image
import os

class Char:
    
    #### constructor
    def __init__(self, imageLeft, imageRight, imageUp, imageDown, firstImage="Down", isChar=False):
        self.imageLeft = imageLeft
        self.imageRight = imageRight
        self.imageUp = imageUp
        self.imageDown = imageDown
        self.isChar = isChar

        ### check first image
        #switch(firstImage):
        #    case("Down"):
        #        self.currentImage = self.imageDown
        #    case("Up"):
        #        self.currentImage = self.imageUp
        #    case("Left"):
        #        self.currentImage = self.imageLeft
        #    case("Right"):
        #        self.currentImage = self.imageRight
        ####Note to self- remove when worked out how to use switch
