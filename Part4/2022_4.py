#/usr/bin/env python3
input_txt = "2022_4.txt"

# Part 1
overlap_count = 0
with open(input_txt, 'r') as f:
    lines = f.readlines()
    for line in lines:
        sections = line.strip().split(',')
        first_sec = [int(i) for i in sections[0].split('-')]
        second_sec = [int(i) for i in sections[1].split('-')]
        
        # [2, 8] [3, 7]
        if first_sec[0] <= second_sec[0] and first_sec[1] >= second_sec[1]:
            print(f"Overlap: {first_sec}{second_sec}")
            overlap_count += 1
            continue
        # [6, 6] [4, 6]
        if second_sec[0] <= first_sec[0] and second_sec[1] >= first_sec[1]:
            print(f"Overlap: {first_sec}{second_sec}")
            overlap_count += 1
            continue
        print(f"No Overlap: {first_sec}{second_sec}")
print(overlap_count)
print()
# Part 2
overlap_count = 0
with open(input_txt, 'r') as f:
    lines = f.readlines()
    for line in lines:
        sections = line.strip().split(',')
        first_sec = [int(i) for i in sections[0].split('-')]
        second_sec = [int(i) for i in sections[1].split('-')]
        
        x = range(first_sec[0], first_sec[1] + 1)
        y = range(second_sec[0], second_sec[1] + 1)
        xs = set(x)
        overlaps = xs.intersection(y)
        if len(overlaps) > 0:
            print(f"Overlap: {first_sec}{second_sec}")
            overlap_count += 1
            continue
        
        print(f"No Overlap: {first_sec}{second_sec}")
print(overlap_count)