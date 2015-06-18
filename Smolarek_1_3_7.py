import random
import matplotlib.pyplot as plt

def roll_hundred_pair():
    pairs = [] # Initialize an aggregator
	
    for counter in range(100):
        roll = random.choice([1,2,3,4,5,6]) + random.choice([1,2,3,4,5,6])
        pairs += [roll]
        '''return pairs for a aggregator list'''   
            
    plt.hist(pairs)
    plt.show()
        


def dice(n):
    ''' returns a random roll of n six sided dice'''
    total = 0 
    for die in range(n):
        total += random.choice([1, 2, 3, 4, 5, 6])
    return total
    
    
    
def matches(ticket, winner):
    '''returns two lists and returns integer that says how many numbers the two have in common'''
    score = 0
    for number in ticket:
        if number in winner:
            score += 1
    return score
    
    
    
def hangman_display(guessed, secret):
    '''return the string a hangman player would see after guessing'''
    revealed = ' '
    for letter in secret:
        if letter == ' ': 
            revealed += ' '          
        elif letter in guessed:
            revealed += letter       
        else:
            revealed += '_'         
    return revealed