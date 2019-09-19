# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:43:16 2019

@author: rosan2
"""
'''
The frontSpaceValue function calculates how many spaces are needed before the dimensions
and backcpaceValue calculates the same thing but after the word. These functions help center the 
dimesions inside the box.
'''

import math

def frontspaceValue(width, word):
    space = int((width - len(word) - 2) / 2)
    return space * " "

def backspaceValue(width, word):
    space = math.ceil((width - len(word) - 2) / 2)
    return space * " "

char = input("Enter frame character ==> ")
print(char)
height = int(input("Height of box ==> "))
print(height)
width = int(input("Width of box ==> "))
print("{}\n".format(width))

word = "{0}x{1}".format(width, height)

'''
Here the values are being printed and the box is formed.
'''
print("Box:")
print(char * width)
print(((char + " " * int((width - 2)) + char) + "\n") * int((height - 2 - 1) / 2), end="")
print(char + frontspaceValue(width, word) + word + backspaceValue(width, word) + char)
print(((char + " " * int((width - 2)) + char) + "\n") * math.ceil((height - 2 - 1) / 2), end="")
print(char * width)