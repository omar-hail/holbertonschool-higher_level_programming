#!/usr/bin/python3
"""
Module: 1-my_list
Defines a class MyList that inherits from list and adds print_sorted().
"""


class MyList(list):
    """
    MyList inherits from list and adds a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Print the list in ascending order without modifying the original list.
        Assumes all elements are integers.
        """
        print(sorted(self))
