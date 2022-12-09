#/usr/bin/env python3
input_txt = "2022_8.txt"


'''
30373
25512
65332
33549
35390
'''
import numpy as np

forest = np.array([[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2],
                   [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]])

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

top_arr = [forest[(3 - x)][3] for x in range(1, 4)]
print(top_arr)
bottom_arr = [forest[(3 + x)][3] for x in range(3, w)]

# for i in range(1, w_inner):
# 	for j in range(1, h_inner):
# 		top_arr = [forest[i - x][j] for x in range(0, i)]
# 		bottom_arr = [forest[i + x][j] for x in range(i, w)]
# 		print(f"{forest[i][j]}: {top_arr} {bottom_arr}")
# if any([x < forest[i][j] for x in dirs]):
# 	print(f"{forest[i][j]}: {top}{bottom}{left}{right} [VISIBLE]")
# else:
# 	print(f"{forest[i][j]}: {top}{bottom}{left}{right} [NOT VISIBLE]")
