from __future__ import print_function # use Python 3.0 printing 

def report_grade(percent):
   '''mastery if percent is 80 or more'''
   '''Step 6b if-else'''
   SCORE = 80
   if percent < SCORE:
        print ('A grade of' ,percent, 'does not indicate mastery. Seek extra practice or help.')
   else:
        print ('A grade of' ,percent, 'percent indicates mastery. Keep up the good work!')