'''
Day 2.5 Program
Aim Puzzle
By Paige Guajardo
'''
import os 

# my pythonanywhere username isn't the same as my local username. so paths arent' the same
# Relative paths are so convenient! I don't want to run different code on my machine

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
puzzle_input_file = os.path.join(THIS_FOLDER, "input2.txt")


# Open file
with open(puzzle_input_file, 'r') as puzzle_input:
    content = puzzle_input.readlines()

# Create List
puzzle_list = []

# For every line set to a int and then append to puzzle_list
for line in content:
    puzzle_list.append(line)

#seperate_list_num = []
#seperate_list_str = []
new_list = []

horizontal = 0
depth = 0
aim = 0

for index, i in enumerate(puzzle_list):
    x, y = i.rsplit(" ", 1)

    #seperate_list_num.append(y)
    #seperate_list_str.append(x)

    y = int(y)

    if x == 'forward':
        horizontal += y
        depth += y*aim
    elif x == 'up':
        #depth = depth - y
        aim = aim - y
    else:
        #depth += y
        aim += y

print(horizontal, " ", depth)

print(depth* horizontal)