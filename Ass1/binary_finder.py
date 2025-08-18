""" Your docstring should go here
Along with your name and email address
"""

import classes
import math
from stats import StatCounter
from classes import *



def binary_stolen_plate_finder(stolen_plates, sighted_plates):
    """ Takes two lists of NumberPlates, returns a list and an integer.
    You can assume the stolen list will be in ascending order.
    You must assume that the sighted list is unsorted.

    The returned list contains stolen number plates that were sighted,
    in the same order as they appeared in the sighted list.
    The integer is the number of NumberPlate comparisons that
    were made.

    You can assume that each input list contains only unique plates,
    ie, neither list will contain more than one copy of any given plate.
    This fact will be very helpful in some special cases - you should
    think about when you can stop searching.    

    Note: you shouldn't alter either of the provided lists and you
    shouldn't make copies of either provided list. 
    """
    result_list = []
    total_comparisons = 0
    # ---start student section---
    
    for sighted_plate in sighted_plates:
        if(len(stolen_plates) == len(result_list)):
            print("lets end this early")
            break

        begin_i = 0
        end_i = len(stolen_plates) - 1

        while begin_i <= end_i:
            mid_i = begin_i + (end_i - begin_i) // 2

            mid_val = stolen_plates[mid_i]

            total_comparisons +=1
            if(sighted_plate == mid_val):
                result_list.append(sighted_plate)
                break
            elif(sighted_plate < mid_val):
                total_comparisons += 1
                end_i = mid_i - 1
            else:
                total_comparisons += 1
                begin_i = mid_i + 1

    # ===end student section===
    return result_list, total_comparisons


# ------------------------------------------------
# Extra stuff for your personal testing regime
# You can leave this stuff out of your submission


def run_tests():
    """ Use this function to run some simple tests 
    to help with developing your awesome answer code.
    You should leave this out of your submission """
    my_numberplate1 = NumberPlate('ABC123')
    my_numberplate2 = NumberPlate('XYZ789')
    #stolen_plates = [my_numberplate1, my_numberplate2]
    stolen_plates = [
    NumberPlate('ABC123'),
    NumberPlate('BCD234'),
    NumberPlate('CDE345'),
    NumberPlate('DEF456'),
    NumberPlate('EFG567'),
    NumberPlate('FGH678'),
    NumberPlate('GHI789'),
    NumberPlate('HIJ890'),
    NumberPlate('IJK901'),
    NumberPlate('JKL012')
    ]
    sighted_plates = [
    NumberPlate('DEF456'),
    NumberPlate('ABC123'),
    NumberPlate('GHI789'),
    NumberPlate('BCD234'),
    NumberPlate('JKL012')
    ]

    thing = binary_stolen_plate_finder(stolen_plates, sighted_plates)
    print(thing)
    print('Tests are fun!')
    print(StatCounter.get_comparisons())


if __name__ == '__main__':
    # This won't run when your module is imported from.
    # Use run_tests to try out some of your own simple tests.

    run_tests()
