'''
Day 3.5 Program
Oxygen / CO2 Puzzle
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
puzzle_list2 = []



# For every line set to a int and then append to puzzle_list
for line in content:
    #line = int(line)
    puzzle_list.append(line)
    puzzle_list2.append(line)




count_list = []

# Number 1 winner
number_1 = []

deleted_list = []


for i in range(0,12): # count columns from 1 to 12
    count1 = 0
    count2 = 0
    print("*************************************")
    print("Puzzle list length: ",len(puzzle_list))
    print("*************************************")
    for j in puzzle_list: # For ever element in puzzle_list
        if j[i] == '1': # If element with the index of i is equal to '1' add 1 to count1
            count1 += 1
        else:           # Else add 1 to count2
            count2 += 1
    
    if count1 > count2:
        number_1.append('1') # If total count of 1's is more than or equal to 0's count append to number_1 list EX : ['1']
    elif count1 == count2:
        number_1.append('1')
    else:
        number_1.append('0') # Else 0's count is more than 1's append to number_1 list EX : ['0']
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Count 1:", count1)
    print("Count 2:", count2)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("List of winning number: ", number_1)
    for k in puzzle_list: # For every element in puzzle_list
        if k[i] != number_1[i]:
            deleted_list.append(k)
            puzzle_list.remove(k)

    print(len(deleted_list))
            
       # elif k[i] != number_1[i]: #Element with the index of m is not equal to number_1 index of m
          #  puzzle_list.remove(k)  # Remove that element from puzzle_list
'''
print(puzzle_list)

print("--------------------------------")
print(number_1)


print("--------------------------------")
print("--------------------------------")

number_2 = []
for i in range(0,12): # count columns from 1 to 12
    count1 = 0
    count2 = 0
    print("*************************************")
    print("Puzzle list length: ",len(puzzle_list2))
    print("*************************************")    
    for j in puzzle_list2: # For ever element in puzzle_list
        if j[i] == '1': # If element with the index of i is equal to '1' add 1 to count1
            count1 += 1
        else:           # Else add 1 to count2
            count2 += 1
    
    if count1 > count2:
        number_2.append('0') # If total count of 1's is more than or equal to 0's count append to number_1 list EX : ['1']
    elif count1 == count2:
        number_2.append('0')
    else:
        number_2.append('1') # Else 0's count is more than 1's append to number_1 list EX : ['0']
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Count 1:", count1)
    print("Count 2:", count2)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("List of winning number: ", number_2)

    for k in puzzle_list2: # For every element in puzzle_list
        if k[i] != number_2[i]: #Element with the index of m is not equal to number_1 index of m
            puzzle_list2.remove(k)  # Remove that element from puzzle_list


print(puzzle_list2)
'''




'''
print(number_2)

print("----------------------------")
print("----------------------------")
print("----------------------------")

binarycode1 = "".join(number_1)
binarycode2 = "".join(number_2)
print("----------------------------")
print("----------------------------")
print("----------------------------")
print(binarycode1)
print(binarycode2)


#Converts binary to Decimal
def binaryToDecimal(n):
    return int(n,2)
 
print("----------------------------")
print("----------------------------")
print("----------------------------")
print("THis is the numbers i get from the binary code:")
print(binaryToDecimal(binarycode1))
print(binaryToDecimal(binarycode2))

print("----------------------------")
print("----------------------------")
print("----------------------------")
alpha = binaryToDecimal(binarycode1)
beta = binaryToDecimal(binarycode2)

answer = alpha * beta

print(answer)
'''