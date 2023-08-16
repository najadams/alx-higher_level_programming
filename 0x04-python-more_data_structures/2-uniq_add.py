#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = list(filter(lambda x: my_list.count(x) == 1, my_list))
    total = sum(uniq)
    return (total)
