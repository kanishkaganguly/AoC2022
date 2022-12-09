#!/usr/bin/env python3

input_txt = "2022_1.txt"

'''
Rock    Paper   Scissors
A       B       C
X       Y       Z
'''
p1 = ['A', 'B', 'C']
p2 = ['X', 'Y', 'Z']

win_conditions = ['AY', 'BZ', 'CX']
draw_conditions = ['AX', 'BY', 'CZ']

selection_points = {'X':1, 'Y':2, 'Z':3}
win_points = {'L':0, 'D':3, 'W':6}

total = 0

with open('2022_2.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        player1, player2 = line.split(' ')
        print(f"Player1: {player1} | Player2: {player2}")


        if f"{player1}{player2}" in draw_conditions:
            print(f"Draw Points: {selection_points[player2]} + {win_points['D']}")
            total += selection_points[player2] + win_points['D']
        elif f"{player1}{player2}" in win_conditions:
            print(f"WIN Points: {selection_points[player2]} + {win_points['W']}")
            total += selection_points[player2] + win_points['W']
        else:
            print(f"LOSS Points: {selection_points[player2]} + {win_points['L']}")
            total += selection_points[player2] + win_points['L']
        print("-----------------")
print(f"Total: {total}")

print("\n#################\n")

total = 0
with open('2022_2.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        player1, game_condition = line.split(' ')
        print(f"Player1: {player1} | GameCondition: {game_condition}")

        if game_condition == 'X':
            # Force a loss
            x = p2[(p1.index(player1)-1) % 3]
            total += selection_points[x] + win_points['L']
            print(f"ForceLoss:{x}")
        elif game_condition == 'Y':
            # Force a draw
            x = p2[p1.index(player1)]
            total += selection_points[x] + win_points['D']
            print(f"ForceDraw:{x}")
        elif game_condition == 'Z':
            # Force a win
            x = p2[(p1.index(player1)+1) % 3]
            total += selection_points[x] + win_points['W']
            print(f"ForceWin:{x}")
        print("-----------------")
print(f"Total: {total}")