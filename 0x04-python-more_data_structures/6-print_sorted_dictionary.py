#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    container = list(a_dictionary.keys())
    container.sort()
    for i in container:
        print("{}: {}".format(i, a_dictionary.get(i)))
