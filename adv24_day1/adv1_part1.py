#Advent of Code 2024 day 1 part 1

def read_lines_to_list(filename):
    # Open the file and read all lines
    with open(filename, 'r') as file:
        # Read lines and strip the newline character at the end of each line
        lines = [line.strip()[:5] for line in file.readlines()]
    return lines
def read_lines_to_list2(filename):
    # Open the file and read all lines
    with open(filename, 'r') as file:
        # Read lines and strip the newline character at the end of each line
        lines2 = [line.strip()[-5:] for line in file.readlines()]
    return lines2
filename = 'adv_day1_numbers.txt'  # Replace with your text file path
list1 = read_lines_to_list(filename)
list2 = read_lines_to_list2(filename)
l1 = [int(x) for x in list1]
l2 = [int(y) for y in list2]
print(l1)
print(l2)
l1.sort() #sort list 1
l2.sort() #sort list 2
print(l1)
print(l2)
l3=[]
for i in range(len(l1)): #create list 3 by sub element by element from l1 & l2
    x = abs(l1[i] - l2[i])
    l3.append(x)
print(l3)
dist=0
for j in range(len(l3)): #add elements of list 3
    dist+=l3[j]
print("the total distance is", dist)
