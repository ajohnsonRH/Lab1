"""
The   **** Blackjack **** PRACTICE for your Python Capstone Project.

CSSE 120 - Introduction to Software Development (Robotics).
Winter term, 2012-2013.
"""

import m0  # @UnusedImport
import m1  # @UnusedImport
import m2  # @UnusedImport
import m4  # @UnusedImport
import time
import random
def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('Testing functions in module m3:\n')
    
# TODO:  (READ THIS)
#   This is a THROW-AWAY, PRACTICE project.
#   Its goal is to help you see how to:
#     a. TOGETHER, AS A TEAM: break a project into parts.
#     b. SEPARATELY, implement your part.
#     c. TOGETHER, AS A TEAM: integrate your separately-implemented parts.
#
# So here is what you do:
#
#  a. AS A TEAM, divide the task -- implementing a Blackjack program --
#       into 3 parts (or 4, if you are a 4-person team).
#
#     Note: If you have NOT already done this division into 3 parts,
#     here is one way to do so:
#         -- Person 1: Implements the dealer's actions.
#         -- Person 2: Implements the player's actions.
#         -- Person 3: Implements everything else, which might be:
#                        -- Deal the cards.
#                        -- Decide who wins.
#    If you are a 4-person team, Person 4 could also implement the
#    dealer's actions (so you will end up with 2 implementations
#    from which you will later choose 1, no problem).
#
#    Decide which of you will do what part -- it doesn't matter,
#    just decide.
#
# b. Implement YOUR part in the appropriate file in this project:
#      -- m1.py for Person 1's code
#      -- m2.py for Person 2's code
#      -- m3.py for Person 3's code
#      -- m4.py for Person 4's code (for 4-person teams)
#
#    Ignore m0.py.  Ignore m4.py unless you are a 4-person team.
#
#    When implementing:
#      -- You must NOT communicate with teammates in any way.
#           The whole point is to help you see how to implement
#           your work SEPARATELY from teammates.
#      -- MAKE ANY ASSUMPTIONS you need to make.
#      -- Do your best to write correct code,
#         but spend NO MORE THAN 60 MINUTES on your implementation.
#      -- Attempt to test your code, as best you can.
#
#   This is a THROW-AWAY project.  It is PURPOSEFUL that the project
#   not work yet (or ever).
#
# c. IN-CLASS, we will do a follow-up exercise to integrate your
#    code with your teammates' code.  Do NOT attempt to do that
#    yourself.  Wait for class to INTEGRATE your team's code.
#
def dealCard(hearts, diamonds, clubs, spades):
    suitNum = random.randrange(3)
    cardNum = random.randrange(12)
    if suitNum == 0:
        card = hearts[cardNum]
        
    elif suitNum == 1:
        card = diamonds[cardNum]
        
    elif suitNum == 2:
        card = clubs[cardNum]
        
    elif suitNum == 3:
        card = spades[cardNum]
        
    return card


def dealerDecision(total, hand):
    check = False
    if total > 21:
        return False
    for k in range(len(hand)):
        if hand[k] == 'A':
            check = True
    if total < 17:
        return True
    
    elif total == 17 and check == True:
        return True
    
    elif total >= 17 and check == False:
        return False
    
def ifDealerBust(total):
    if total > 21:
        print("Dealer busts!")
        return True 
    
    else:
        return False       


#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
