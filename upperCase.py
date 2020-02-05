#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:14:49 2020

@author: Olympus
"""

def upperCase():
    letter = ord(input("What letter?: "))
    if letter >= 97:
        letter = letter - 32;
    else:
        letter=letter
    
    print('Your letter is: ' + str(chr(letter)))
    

while True:
    upperCase();
