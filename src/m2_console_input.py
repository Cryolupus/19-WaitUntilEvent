"""
This module demonstrates lets you practice INPUT from the CONSOLE.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Kevin Chou.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math

def main():
    """ TESTs the functions in this module (by calling them). """
    double_a_float()
    print_an_integer_many_times()
    print_an_integer_many_times_on_one_row()
    input_it_all()


def double_a_float():
    potato = float(input('Input a float:'))
    print(potato * 2)

    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
       a. Prompts the user for and inputs a floating point number.
       b. Prints the input number, doubled (i.e., multiplied by 2).
    No input validation is required.  Nothing else should be printed.

    Example:
    Here is a sample run, where the user input is to the right
    of the colon:
         Enter a number: -3.14
         -6.28
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #   The testing code is already written for you (above).
    # ------------------------------------------------------------------


def print_an_integer_many_times():
    positive = int(input('Input positive number'))
    t = positive
    for k in range(positive):
        print(t*2)
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
       a. Prompts the user for and inputs a positive integer.
       b. Prints the input integer, doubled (i.e., multiplied by 2),
          the input number of times.  (See the example.)
    No input validation is required.  Nothing else should be printed.

    Example:
    Here are two sample runs, where the user input is to the right
    of the colon:
         Enter an integer: 3
         6
         6
         6

         Enter an integer: 5
         10
         10
         10
         10
         10
    """
    # ------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #   The testing code is already written for you (above).
    # ------------------------------------------------------------------


def print_an_integer_many_times_on_one_row():
    b = int(input('Input int'))
    empty = ''
    for k in range(b):
        empty = empty + str(b*2)
    print(empty)
    """
    Same as the previous problem, but print the numbers
    on a single line with no spaces in between them.

    Here are two sample runs, where the user input is to the right
    of the colon:
         Enter an integer: 3
         666

         Enter an integer: 5
         1010101010
    """
    # ------------------------------------------------------------------
    # Done: 4. Implement and test this function.
    #   The testing code is already written for you (above).
    #
    # HINT: One way to print on a SINGLE line is to build up a string
    #       and then print that (single) string.
    # ------------------------------------------------------------------


def input_it_all():
    potato = float(input('Input Float:'))
    potato2 = int(input('Input +Int:'))
    potato3 = input('Input String:')
    potatosqrt = math.sqrt(potato)
    for k in range(potato2):
        print(potatosqrt)
    for k in range(potato2):
        print(potato3)
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
      Prompts the user for and inputs:
        -- A positive floating point number
        -- A positive integer
        -- A string
      in that order (via three separate INPUT statements).
      Then prints, in this order, all on separate lines:
        a. The square root of the floating point number,
           repeated the input integer number of times.
        b. The string, repeated the input integer number of times.
      No input validation is required.  Nothing else should be printed.

    Example:
    Here is a sample run, where the user input is to the right
    of the colons:
         Enter a positive floating point number: 1.44
         Enter a positive integer: 4
         Enter a string: Peace & Love.
         1.2
         1.2
         1.2
         1.2
         Peace & Love.
         Peace & Love.
         Peace & Love.
         Peace & Love.
    """
    # ------------------------------------------------------------------
    # Done: 5. Implement and test this function.
    #   The testing code is already written for you (above).
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
