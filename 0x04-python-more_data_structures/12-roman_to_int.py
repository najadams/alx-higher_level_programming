#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = last_rom = 0
    list_num = [0]
    for ch in roman_string:
        if ch in rom_n:
            if rom_n[ch] <= last_rom:
                max_list = max(list_num)
                num += max_list - sum(n for n in list_num if max_list > n)
                list_num = [rom_n[ch]]
            else:
                list_num.append(rom_n[ch])
            
            last_rom = rom_n[ch]

    max_list = max(list_num)
    num += max_list - sum(n for n in list_num if max_list > n)
    return num
