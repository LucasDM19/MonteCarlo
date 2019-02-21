# https://pythonprogramming.net/monte-carlo-simulator-python/

'''
so now we've got a bettor, he's working, and we've seen some basic outcomes
but now we want to see some longer-term outcomes, so first let's do that. 
'''

import random
import matplotlib
import matplotlib.pyplot as plt
#
import time

# let us go ahead and change this to return a simple win/loss
def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
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

    # wager X
    wX = []

    #value Y
    vY = []

    # change to 1, to avoid confusion so we start @ wager 1
    # instead of wager 0 and end at 100. 
    currentWager = 1

    #           change this to, less or equal.
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            # append #
            wX.append(currentWager)
            vY.append(value)
            
        else:
            value -= wager
            # append #
            wX.append(currentWager)
            vY.append(value)

        currentWager += 1
        
        print( 'Funds:', value )
    plt.plot(wX,vY)

def doubler_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1

    # since we'll be betting based on previous bet outcome #
    previousWager = 'win'

    # since we'll be doubling #
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            print( 'we won the last wager, yay!' )
            if rollDice():
                value += wager
                print( value )
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager  
                previousWager = 'loss'
                print( value )
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    print( 'went broke after',currentWager,'bets' )
                    currentWager += 10000000000000000
        elif previousWager == 'loss':
            print( 'we lost the last one, so we will be super smart & double up!' )
            if rollDice():
                wager = previousWagerAmount * 2
                print( 'we won',wager )
                value += wager
                print( value )
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                print( 'we lost',wager )
                value -= wager
                if value < 0:
                    print( 'went broke after',currentWager,'bets' )
                    currentWager += 10000000000000000
                print( value )
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    print( 'went broke after',currentWager,'bets' )
                    currentWager += 10000000000000000

        currentWager += 1

    print( value )
    plt.plot(wX,vY)
    
doubler_bettor(10000,100,100)
plt.show()
time.sleep(555)    
    
# lots of wagers now....
x = 0

# start this off @ 1, then add, and increase 50 to 500, then 1000
while x < 100:
    simple_bettor(funds=10000,initial_wager=100,wager_count=1000)
    x += 1


plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()