'''
Created on 04-Jun-2014

@author: brij
'''

myglob = 0

def myfun():
    print myglob

def modfun():
    global myglob
    myglob = myglob + 1
    
myfun()
modfun()
myfun()