#!/bin/python3


import math
import os
import random
import re
import sys

#
# Complete the 'FibonacciIterator' class below.
#
# The class is expected to have a constructor with a single argument and iterable object.
#

class FibonacciIterator:
    # Write your code here
    def __init__(self, n):
        self.n = n
        self.index = 0
        self.current_value = 0
        self.sequence = []
       
       
    def __iter__(self):
        return self


    def __next__(self): # Python 2: def next(self)
        if self.index <= 1:
            self.sequence.append(self.index)
            self.current_value = self.index
        else:
            sequence_item_one = self.sequence[self.index-1]
            sequence_item_two = self.sequence[self.index-2]
            self.sequence.append(sequence_item_one + sequence_item_two)
            self.current_value = sequence_item_one + sequence_item_two
       
        self.index += 1
       
        if self.index <= self.n:
            return self.current_value
        raise StopIteration
       

# This is where the code runs
# This is a list of values for the variable N
test_cases_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]    
   
for n in test_cases_n:
    result = FibonacciIterator(n)
    result_string = ""

    for num in result:
        result_string += " " + str(num)

    print("The Fibonacci result for N =", n, "is:")
    print(result_string)   
 
