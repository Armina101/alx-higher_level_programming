#!/usr/bin/python3
"""
Class Module to prevents dynamic attribute

"""
class LockedClass():
    """Class to prevent dynamic attribute"""
    __slots__ = ['first_name']

    def __init__(self):
        pass
