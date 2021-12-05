'''
Day 1 Program
Sonar Puzzle
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

#for i in range(len(puzzle_list)):
#    if puzzle_list[0] == puzzle_list[i]:
#        print(puzzle_list[i], " (N/A - no previous measurement)")
#    elif puzzle_list[i] > puzzle_list[i - 1]:
#        print(puzzle_list[i], " (Increase)")
#        count += 1
#    else:
#        print(puzzle_list[i], " (Decrease)")

#print(count)

with open('puzzle_answer.txt', 'x') as pa:
    for i in range(len(puzzle_list)):
        if puzzle_list[0] == puzzle_list[i] and count2 == 0:
            pa.write(str(puzzle_list[i]) + " (N/A - no previous measurement)\n")
            count2 += 1
        elif puzzle_list[i] >= puzzle_list[i - 1]:
            pa.write(str(puzzle_list[i]) + " (Increase)\n")
            count += 1
        else:
            pa.write(str(puzzle_list[i]) + " (Decrease)\n")
    pa.write(str(count))
