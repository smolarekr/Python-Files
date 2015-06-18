import random

def goguess():
    secret = random.randint(1, 20)
    print('I have an integer between 1 and 20.')
    guess = int(raw_input('Guess: '))
    while guess != secret:
        if guess < secret:
            print('Too low, guess again') 
        else:     
            print('Too high, guess again')
        guess = int(raw_input('Guess: ')) 
    print ('Right on! I was number', guess) 