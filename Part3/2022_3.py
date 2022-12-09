#/usr/bin/env python3
import string

input_txt = "2022_3.txt"

priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)

priority_sum = 0
with open(input_txt, "r") as f:
    lines = f.readlines()
    for line in lines:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        
        first_set = set(first_half)
        second_set = set(second_half)

        common_priorities = [(priorities.index(x)+1) for x in list(first_set.intersection(second_set))]
        priority_sum += sum(common_priorities)
        print(f"Common: {common_priorities[0]}")
print(f"CommonSum:{priority_sum}")

print("###########################")

group = []
group_idx = 0
priority_sum = 0
with open(input_txt, "r") as f:
    lines = f.readlines()
    for line in lines:
        group.append(line.strip())
        group_idx+=1
        
        if group_idx == 3:
            set_list = [set(x) for x in group]
            set_intersection = [(priorities.index(x)+1) for x in list(set_list[0].intersection(*set_list))]
            priority_sum += sum(set_intersection)

            group_idx = 0                        
            group = []
            continue
print(f"CommonSum:{priority_sum}")