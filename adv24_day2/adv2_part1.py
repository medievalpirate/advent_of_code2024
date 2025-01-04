#Advent of Code 2024 day 2 part 1
def read_lines_to_list(filename):
    # Open the file and read all lines
    with open(filename, 'r') as file:
        # Read lines and strip the newline character at the end of each line
        lines = [line.strip() for line in file.readlines()]
    return lines
filename = 'adv_day2_numbers.txt' #text file path
masterlist = read_lines_to_list(filename)
print(masterlist)
new_lists = []
for item in masterlist:
    # Split each item by space and convert each element to an integer
    new_list = [int(x) for x in item.split()]
    new_lists.append(new_list)
print("2D Array:")
print(new_lists)
safe_rep=0
unsafe_rep=0
a=' '
def is_sorted(list):
    for item in range(len(list) - 1):
        num1 = list[item]
        num2 = list[item + 1]
        if num1 < num2:
            checker = True
        else:
            return False
    return True

def is_backward_sorted(list):
    for item in range(len(list)-1,0,-1):
        num1 = list[item]
        num2 = list[item-1]
        if num1 < num2:
            checker = True
        else:
            return False
    return True

for row in range(len(new_lists)):
    if (is_sorted(new_lists[row]) == True) or (is_backward_sorted(new_lists[row]) == True):
        for element in range(len(new_lists[row])-1):
            x = new_lists[row][element]
            x1 = new_lists[row][element+1]
            x2 = abs(x - x1)
            if (x2 > 0) and (x2 < 4):
                a ='safe'
            else:
                a='unsafe'
                break
        if a == 'safe':
            safe_rep+=1
        else:
            unsafe_rep+=1
    elif (is_sorted(new_lists[row]) == False) and (is_backward_sorted(new_lists[row]) == False):
        unsafe_rep += 1
print('safe reports:', safe_rep)
print('unsafe reports:', unsafe_rep)
