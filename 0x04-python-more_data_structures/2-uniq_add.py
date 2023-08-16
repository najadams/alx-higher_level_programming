#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = list(filter(lambda x: my_list.count(x) == 1, my_list))
    for x in uniq:
        if x not in my_lis  and isinstance(x,(int,float)):
            uniq.append(x)
    total = sum(uniq)
    return (total)
