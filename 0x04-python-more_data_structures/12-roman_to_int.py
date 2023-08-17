#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev_value = 0
    for ch in reversed(roman_string):
        value = rom_n.get(ch, 0)
        if value >= prev_value:
            num += value
        else:
            num -= value
        prev_value = value
    return num
