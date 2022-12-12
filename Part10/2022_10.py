#/usr/bin/env python3
import numpy as np
from typing import List
input_txt = "Part10/2022_10.txt"

regX:int = 1
cycles:int = 1
iter:int = 0
val:int = 0
signal_strength:int = 0
signal_iter:List[int] = [20, 60, 100, 140, 180, 220]
signal_strength_sum:int = 0

''' PART 1 
with open(input_txt) as f:
    lines = f.readlines()
    for cmd in lines:
        cmd = cmd.strip()

        print(f"CMD: {cmd}")
        if "noop" in cmd:
            iter = 1
            val = 0
        elif "addx" in cmd:
            iter = 2
            val = int(cmd.split(" ")[1])
        
        for _ in range(cycles, (iter + cycles)):
            print(f"Cycle {cycles} Start")
            signal_strength = regX * cycles
            if cycles in signal_iter:
                print(f"REGX: {regX} Signal Strength: {signal_strength}")
                signal_strength_sum += signal_strength
            print(f"Cycle {cycles} End")
            cycles += 1
        
        regX += val
        print(f"REGX: {regX}")


        print()
print(signal_strength_sum)
print()
'''

def show(grid: np.ndarray)->None:
    print("Sprite position: ")
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            print(f"{grid[i,j]} ", end=' ')
        print()
    print()

crt_w, crt_h = 40, 6
sprite = np.full((3,), '#', dtype=str)
crt = np.full((crt_h, crt_w), '.', dtype=str)

crt[0, :3] = sprite
show(crt)

crt_index = 0
with open(input_txt) as f:
    lines = f.readlines()
    for cmd in lines:
        cmd = cmd.strip()

        print(f"CMD: {cmd}")
        if "noop" in cmd:
            iter = 1
            val = 0
        elif "addx" in cmd:
            iter = 2
            val = int(cmd.split(" ")[1])
        
        for _ in range(cycles, (iter + cycles)):
            print(f"Cycle {cycles} Start")
            signal_strength = regX * cycles
            if cycles in signal_iter:
                print(f"REGX: {regX} Signal Strength: {signal_strength}")
                signal_strength_sum += signal_strength
            print(f"Cycle {cycles} End")
            cycles += 1
        
        regX += val
        print(f"REGX: {regX}")


        print()