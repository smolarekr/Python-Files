from __future__ import print_function # must be first in file 
import random

def guess_once():
    secret = random.randint(1, 4)
    print('I have an integer between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess < secret:
        print('Too low, my number is', secret) 
    else:     
        if guess > secret:
            print('Too high, my number is', secret)
        else:
            print('Right on! I was number', secret) 
        