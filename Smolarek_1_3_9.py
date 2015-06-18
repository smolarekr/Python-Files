from __future__ import print_function # use Python 3.0 printing 

def hint(color, secret):
    '''is the color in the string?'''
    secret = ['red','red','yellow','yellow','black']
    if color in secret:
        print ('The color', color, 'is in the sequence.')
    else:
        print ('The color'. color, 'is NOT in the sequence.')
    