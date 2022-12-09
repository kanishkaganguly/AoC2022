#/usr/bin/env python3
import re
input_txt = "2022_5.txt"

'''
    [B]             [B] [S]        
    [M]             [P] [L] [B] [J]
    [D]     [R]     [V] [D] [Q] [D]
    [T] [R] [Z]     [H] [H] [G] [C]
    [P] [W] [J] [B] [J] [F] [J] [S]
[N] [S] [Z] [V] [M] [N] [Z] [F] [M]
[W] [Z] [H] [D] [H] [G] [Q] [S] [W]
[B] [L] [Q] [W] [S] [L] [J] [W] [Z]
 1   2   3   4   5   6   7   8   9 
'''
stacks = [
    ['NWB'],
    ['BMDTPSZL'],
    ['RWZHQ'],
    ['RZJVDW'],
    ['BMHS'],
    ['BPVHJNGL'],
    ['SLDHFZQJ'],
    ['BQGJFSW'],
    ['JDCSMWZ']
]
for idx, stack in enumerate(stacks):
    stacks[idx] = list(reversed([str(i) for i in stack[0]]))

part = 1
part = 2

print("Start Stacks")
for stack in stacks:
    print(stack)
print()

with open(input_txt,'r') as f:
    lines = f.readlines()
    for line in lines:
        nums = re.findall(r'\d+',line.strip())
        move_count = int(nums[0])
        from_id = int(nums[1])-1
        to_id = int(nums[2])-1
        print(f"Move {move_count} items {from_id} to {to_id}")

        if part == 1:
            for _ in range(move_count):
                stacks[to_id].append(stacks[from_id].pop())
        if part == 2:
            stacks[to_id].extend(stacks[from_id][-move_count:])
            del(stacks[from_id][-move_count:])

        for stack in stacks:
            print(stack)
        print()

result = []
for stack in stacks:
    if stack:
        result.append(stack[-1])
result = "".join(result)
print(result)