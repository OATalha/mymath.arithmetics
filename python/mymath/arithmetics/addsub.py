"""
Contains the class AddSub
"""


class AddSub:
    "Collection of subtraction and addition operations"
    def __init__(self):
        '''This is the __init__ function'''
        pass

    @staticmethod
    def add(x, y):
        """This module adds two numbers

        :param x: first number
        :type x: int
        :param y: second number
        :type y: int

        :return: sum of two numbers
        """
        return x+y

    @staticmethod
    def subtract(x, y):
        """This module subtracts two numbers

        :param x: first number
        :type x: int
        :param y: second number
        :type y: int

        :return: difference between the two numbers
        """
        return x-y

