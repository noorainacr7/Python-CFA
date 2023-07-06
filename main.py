#!/usr/bin/env python

import random

def main():
    """Start a music genre guessing game"""
print("guess the music genre!")
    
music = ["neon", "kpop", "rock", "classical", "funk", "disco"]
    
x = random.choice(music)
guess = None
    
while x != guess: 
        
    guess = str(input("pick a music genre between neon, kpop, rock, classical, disco or funk:"))
        
    if x == guess:
        print("very genius!")
        break
    else:    
        print ("try again!!!")

main()