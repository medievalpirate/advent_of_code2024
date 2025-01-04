#Advent of Code 2024 day 1 part 2
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
l3=[]
for i in range(len(l1)):
    x = l1[i]
    count = l2.count(x)
    l3.append(count)
print(l3)
l4 = []
for i in range(len(l1)):
    x = l1[i]*l3[i]
    l4.append(x)
print(l4)
dist=0
for j in range(len(l4)):
    dist+=l4[j]
print("the total distance is", dist)
