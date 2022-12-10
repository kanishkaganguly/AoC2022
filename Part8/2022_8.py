#/usr/bin/env python3
input_txt = "Part8/2022_8.txt"

import numpy as np

forest_test = np.array([[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2],
                   [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]])

with open(input_txt) as f:
	forest = np.array([list(map(int, line.strip())) for line in f])
print(forest)

w, h = np.shape(forest)

forest_inner = forest[1:-1, 1:-1]
w_inner = w - 1
h_inner = h - 1
print("Forest")
print(forest)
print("------------------")
print("Inner Forest")
for i in range(1, w_inner):
	for j in range(1, h_inner):
		print(f"{forest[i][j]}", end=' ')
	print()
print("------------------")

interior = 0
exterior = 0
exterior = w*2 + (h-2)*2
max_scenic_score = 0

for i in range(1, w_inner):
	for j in range(1, h_inner):
		column = forest[:, j]
		row = forest[i, :]	
		top = list(reversed(column[:i]))
		bottom = column[i+1:]
		left = list(reversed(row[:j]))
		right = row[j+1:]
		visible = any(
			[all(x < forest[i][j] for x in top),
			all(x < forest[i][j] for x in bottom),
			all(x < forest[i][j] for x in left),
			all(x < forest[i][j] for x in right)]
		)
		if visible:
			interior += 1

		score_top, score_bottom, score_left, score_right = 0, 0, 0, 0
		for x in top:
			if x < forest[i][j]:
				score_top += 1
			else:
				score_top += 1
				break
		for x in bottom:
			if x < forest[i][j]:
				score_bottom += 1
			else:
				score_bottom += 1
				break
		for x in left:
			if x < forest[i][j]:
				score_left += 1
			else:
				score_left += 1
				break
		for x in right:
			if x < forest[i][j]:
				score_right += 1
			else:
				score_right += 1
				break

		scenic_score = score_top * score_bottom * score_left * score_right 
		max_scenic_score = scenic_score if scenic_score > max_scenic_score else max_scenic_score


print(f"Part1: {interior + exterior}")
print(f"Part2: {max_scenic_score}")