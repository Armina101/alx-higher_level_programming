#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    org_list = len(my_list)
    if idx < 0:
        return(my_list)
    if idx > (org_list - 1):
        return(my_list)
    my_list[idx] = element
    return(my_list)
