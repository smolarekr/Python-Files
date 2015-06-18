from __future__ import print_function


def how_eligible(essay):
    '''paragraph needs a ? " , !'''
    count=0
    if '?' in essay:
        count +=1
    if '!' in essay:
        count +=1
    if '"' in essay:
        count +=1
    if ',' in essay:
        count +=1
    print ('Yes, your count is' ,count,)
    