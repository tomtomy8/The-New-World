##Character Class for 'The New World'

from tkinter import *
from PIL import ImageTk, Image
import os

class Char:
    
    #### constructor
    def __init__(self, imageLeft, imageLeftLeft, imageLeftRight, imageRight,
                 imageRightLeft, imageRightRight, imageUp, imageUpLeft, imageUpRight,
                 imageDown, imageDownRight, imageDownLeft, frame, firstImage="Down",
                 isChar=False):
        ###Long list of varibles(Good God...)
        self.imageLeft = imageLeft
        self.imageLeftLeft = imageLeftLeft
        self.imageLeftRight = imageLeftRight
        self.imageRight = imageRight
        self.imageRightLeft = imageRightLeft
        self.imageRightRight = imageRightRight
        self.imageUp = imageUp
        self.imageUpLeft = imageUpLeft
        self.imageUpRight = imageUpRight
        self.imageDown = imageDown
        self.imageDownLeft = imageDownLeft
        self.imageDownRight = imageDownRight
        self.isChar = isChar
        self.firstImage = firstImage
        self.frame = frame

        ###Work out which way the character is first facing
        if self.firstImage == "Down":
            self.currentImage = self.imageDown
        if self.firstImage == "Up":
            self.currentImage = self.imageUp
        if self.firstImage == "Left":
            self.currentImage = self.imageLeft
        if self.firstImage == "Right":
            self.currentImage = self.imageRight

        ###Make sure its facing the right way to avoid glitches
        self.direction = self.firstImage

        ##Draw image
        self.draw()

    ####Note to self - add in movement when bothered to ######

    ####Move forward
    def moveForward(self, nextImg):
        self.currentImage = nextImg
        self.draw()

    ####Move backward
    def moveBackward(self, nextImg):
        self.currentImage = nextImg
        self.draw()

    ####Move left
    def moveLeft(self, nextImg):
        self.currentImage = nextImg
        self.draw()

    ####Move right
    def moveRight(self, nextImg):
        self.currentImage = nextImg
        self.draw()

    ###Draw the character sprite
    def draw(self):
        self.img = Label(self.frame, image=self.currentImage)
        self.img.pack(side = "bottom", fill = "both", expand = "no")
