#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        full_int = my_list[0]
        for n in range(len(my_list)):
            if my_list[n] > full_int:
                full_int = full_list[n]
        return full_int
