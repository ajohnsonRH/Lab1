"""
The   **** Blackjack **** PRACTICE for your Python Capstone Project.

CSSE 120 - Introduction to Software Development (Robotics).
Winter term, 2012-2013.

This module contains the global data SHARED by the entire project.
"""

import m1  # @UnusedImport
import m2  # @UnusedImport
import m3  # @UnusedImport
import m4  # @UnusedImport

def main():
    """ Runs the MAIN PROGRAM. """
    # Intended to be used when running the main (entire) program.
    print('Integration Testing of the MAIN PROGRAM:\n')
    m2.game()
class Data():
    def __init__(self):
        self.project_name = "BLACKJACK"
        
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
