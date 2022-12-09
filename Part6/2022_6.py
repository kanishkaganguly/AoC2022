#/usr/bin/env python3
from math import floor
input_txt = "2022_6.txt"

start_idx = 0
with open(input_txt, "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        for i in range(len(line)):
            window = line[start_idx:start_idx+4]
            print(window)
            start_idx += 1
        print(floor(start_idx/4))
        start_idx = 0
        
            