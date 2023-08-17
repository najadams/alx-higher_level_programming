#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    list_of_keys = list(a_dictionary.values())
    convert = list(map(lambda x: x * 2, list_of_keys))
    for i, value in a_dictionary.values():
        a_dictionary.value(value) = convert[i]
    return (a_dictionary)
