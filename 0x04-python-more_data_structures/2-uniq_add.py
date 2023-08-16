#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = list(filter(lambda x: my_list.count(x) == 1, my_list))
    for x in my_list:
        if x not in uniq  and isinstance(x,(int,float)):
            uniq.append(x)
    total = sum(uniq)
    return (total)
