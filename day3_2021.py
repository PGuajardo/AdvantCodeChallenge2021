'''
Day 3 Program
Gamma / Epsilon Puzzle
By Paige Guajardo
'''
import os 

# my pythonanywhere username isn't the same as my local username. so paths arent' the same
# Relative paths are so convenient! I don't want to run different code on my machine

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
puzzle_input_file = os.path.join(THIS_FOLDER, "input3.txt")


# Open file
with open(puzzle_input_file, 'r') as puzzle_input:
    content = puzzle_input.readlines()


# Create List
puzzle_list = []

# For every line set to a int and then append to puzzle_list
for line in content:
    #line = int(line)
    puzzle_list.append(line)

#print(puzzle_list)
first_half = []
second_half = []



for i in puzzle_list:
    first_half.append(i[:len(i)//2])
    
for i in puzzle_list:
    second_half.append(i[len(i)//2:])


'''
print(puzzle_list)
print("-----------------------------")
print("-----------------------------")
print(first_half)
print("-----------------------------")
print("-----------------------------")
print(second_half)
'''

for i in first_half:
    i = int(i)

for k in second_half:
    k = int(k)

#count1 = 0
#count2 = 0


count_list = []

# Number 1 winner
number_1 = []
number_2 = []

#print(first_half[0][0] == '1')
for i in range(0,len(puzzle_list[0]) - 1): #firsthalf at first
    count1 = 0
    count2 = 0
    for j in puzzle_list:
        if j[i] == '1':
            count1 += 1
        else:
            count2 += 1
    
    if count1 > count2:
        number_1.append(str(i + 1) + ": Index of 1") #First Index 1, this though pastes the winner 
    else:
        number_1.append(str(i + 1) + ": Index of 0")

    #count_list.append("Count of 1's.) " + str(count1) + "-- Count of 2's.) " + str(count2))

#if count1 > count2:


print(number_1)

binary_list = []
for i in number_1:
    binary_list.append(i[-1])


print("----------------------------")
print("----------------------------")
print("----------------------------")
print(binary_list)

binarycode = "".join(binary_list)

print("----------------------------")
print("----------------------------")
print("----------------------------")
print(binarycode)


#Converts binary to Decimal
def binaryToDecimal(n):
    return int(n,2)
 
print("----------------------------")
print("----------------------------")
print("----------------------------") 
# Driver code

print(binaryToDecimal(binarycode))

first_value = binaryToDecimal(binarycode)

second_binary_list = []
# Getting the opposite of binary code
for i in binary_list:
    if i == '1':
        second_binary_list.append("0")
    else:
        second_binary_list.append("1")

mirror_binary = "".join(second_binary_list)
print("----------------------------")
print("----------------------------")
print("----------------------------") 
print(mirror_binary)

print("----------------------------")
print("----------------------------")
print("----------------------------") 
print(binaryToDecimal(mirror_binary))

second_value = binaryToDecimal(mirror_binary)

answer = first_value * second_value

print("----------------------------")
print("----------------------------")
print("----------------------------") 
print(answer)

