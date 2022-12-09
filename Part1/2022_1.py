#!/usr/bin/env python3

input_txt = "2022_1.txt"

calories = 0
elf_id = 1
max_elf = 0
max_calories = 1e-7
calories_list = []

with open(input_txt) as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if '' == line:
            print(f"Elf {elf_id}: Calories: {calories}")
            print("---------------------------")
            
            calories_list.append(calories)
            if calories > max_calories:
                max_calories = calories
                max_elf = elf_id

            calories = 0
            elf_id += 1
            continue
        else:
            calories += int(line)
print(f"MaxCalories: {max_calories}")

calories_list.sort(reverse=True)
print(f"TopThreeCalories: {sum(calories_list[:3])}")