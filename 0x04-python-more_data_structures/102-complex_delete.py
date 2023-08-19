#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, value_dic in a_dictionary.items():
        if value_dic == value:
            del a_dictionary[key]
    return (a_dictionary)
