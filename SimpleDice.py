# https://pythonprogramming.net/monte-carlo-simulator-python/

'''
so now we've got a bettor, he's working, and we've seen some basic outcomes
but now we want to see some longer-term outcomes, so first let's do that. 
'''

import random

# let us go ahead and change this to return a simple win/loss
def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        #print( roll,'roll was 100, you lose. What are the odds?! Play again!')
        return False
    elif roll <= 50:
        #print( roll,'roll was 1-50, you lose.')
        return False
    elif 100 > roll >= 50:
        #print( roll,'roll was 51-99, you win! *pretty lights flash* (play more!)')
        return True

def simpleDiceRoller():
   # Now, just to test our dice, let's roll the dice 100 times. 
   x = 0
   while x < 100:
       result = rollDice()
       print(result)
       x+=1

'''
Simple bettor, betting the same amount each time.
'''
def simple_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager

    currentWager = 0

    while currentWager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager

        currentWager += 1
        print( 'Funds:', value )


# lots of wagers now....
x = 0

while x < 100:
   simple_bettor(10000,100,100)      
   x += 1