#/usr/bin/env python3
import numpy as np
from typing import Tuple
input_txt = "Part9/2022_9.txt"

'''
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''

def show(grid: np.ndarray)->None:
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            print(f"{grid[i,j]} ", end=' ')
        print()
    print()

def update(grid:np.ndarray, H:tuple, T:tuple)->np.ndarray:
    grid[np.where(grid == 'H')] = '.'
    grid[np.where(grid == 'T')] = '.'

    grid[H] = 'H'
    grid[T] = 'T'

    return grid

def HT_distance(H: tuple, T: tuple)->Tuple[int, int]:
    return ((H[0]-T[0]),(H[1]-T[1]))

def is_neighbor(H: tuple, T: tuple)->bool:
    '''
    Everything is relative to the head

    . H .
    H T H
    . H .

    H . H
    . T .
    H . H
    '''
    # check top left
    if H[0]+1 == T[0] and H[1]+1 == T[1]:
        print(f"H is top left of T")
        return True
    # check top right
    elif H[0]+1 == T[0] and H[1]-1 == T[1]:
        print(f"H is top right of T")
        return True
    # check bottom left
    elif H[0]-1 == T[0] and H[1]+1 == T[1]:
        print(f"H is bottom left of T")
        return True
    # check bottom right
    elif H[0]-1 == T[0] and H[1]-1 == T[1]:
        print(f"H is bottom right of T")
        return True
    # check top
    elif H[0]+1 == T[0] and H[1] == T[1]:
        print(f"H is top of T")
        return True
    # check bottom
    elif H[0]-1 == T[0] and H[1] == T[1]:
        print(f"H is bottom of T")
        return True
    # check left
    elif H[0] == T[0] and H[1]+1 == T[1]:
        print(f"H is left of T")
        return True
    # check right
    elif H[0] == T[0] and H[1]-1 == T[1]:
        print(f"H is right of T")
        return True
    
    return False

grid = np.full((5,6), '.', dtype=str)
H = (4,0)
T = (4,0)
grid[H] = 'H'
print("== Initial State ==")
show(grid)

with open(input_txt, 'r') as f:
    lines = f.readlines()
    for line in lines[0:4]:
        move = line.strip(' \n').split(' ')
        direction = move[0]
        distance = int(move[1])
        print(f"== {direction} {distance} ==") 

        for _ in range(distance):
            # Move head 
            if direction == 'R':
                H = (H[0], H[1]+1)
                grid = update(grid, H, T)
                show(grid)
            elif direction == 'U':
                H = (H[0]-1, H[1])
                grid = update(grid, H, T)
                show(grid)
            elif direction == 'D':
                H = (H[0]+1, H[1])
                grid = update(grid, H, T)
                show(grid)
            elif direction == 'L':
                H = (H[0], H[1]-1)
                grid = update(grid, H, T)
                show(grid)
            
            # Move tail
            if not is_neighbor(H, T):

                diff = HT_distance(H, T)
                T = (T[0]+diff[0], T[1]+diff[1])
                grid = update(grid, H, T)

            