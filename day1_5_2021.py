'''
Day 1.5 Program
Sliding Puzzle
By Paige Guajardo
'''
import os 

# my pythonanywhere username isn't the same as my local username. so paths arent' the same
# Relative paths are so convenient! I don't want to run different code on my machine

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
puzzle_input_file = os.path.join(THIS_FOLDER, "input.txt")


# Open file
with open(puzzle_input_file, 'r') as puzzle_input:
    content = puzzle_input.readlines()

# Create List
puzzle_list = []

# For every line set to a int and then append to puzzle_list
for line in content:
    line = int(line)
    puzzle_list.append(line)

count = 0
count2 = 0


with open('puzzle_answer2.txt', 'w') as pa:
    for i in range(len(puzzle_list)):
        if puzzle_list[0] == puzzle_list[i] and count2 == 0:
            pa.write(str(puzzle_list[i] + puzzle_list[i+1] + puzzle_list[i+2]) + " (N/A - no previous measurement)\n")
            count2 += 1
        elif puzzle_list[-2] == puzzle_list[i]:
            pa.write(str(puzzle_list[i] + puzzle_list[i+1]) + " (Decrease)\n")
        elif puzzle_list[-1] == puzzle_list[i]:
            pa.write(str(puzzle_list[i]) + " (Last Value)\n")
        elif (puzzle_list[i] + puzzle_list[i + 1] + puzzle_list[i + 2]) > (puzzle_list[i - 1] + puzzle_list[i] + puzzle_list[i + 1]):
            pa.write(str(puzzle_list[i] + puzzle_list[i+1] + puzzle_list[i + 2]) + " (Increase)\n")
            count += 1
        elif (puzzle_list[i] + puzzle_list[i + 1] + puzzle_list[i + 2]) == (puzzle_list[i - 1] + puzzle_list[i] + puzzle_list[i + 1]):
            pa.write(str(puzzle_list[i] + puzzle_list[i + 1] + puzzle_list[i + 2]) + " (no change)\n")
        else:
            pa.write(str(puzzle_list[i] + puzzle_list[i + 1] + puzzle_list[i + 2]) + " (Decrease)\n")
    pa.write(str(count))