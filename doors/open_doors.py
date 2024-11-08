'''A simple solution to the 100 Doors problem.'''
from math import sqrt

# initial state of the doors
num_doors = 100
doors = [False] * num_doors

# the algorithm I used
for i in range(0,num_doors):
    for j in range(i,num_doors,i+1):
        doors[j] = not doors[j]

# quick print of open doors
print("\n\nFinal State of Doors:\n")
open_doors = []
for index,door in enumerate(doors):
    if door:
        open_doors.append(index + 1)

print(open_doors)

# A horrific implementation:
# initial state of the doors
num_doors = 100
doors = list(range(1, 101)) # Open all the doors, pass 1

# function to toggle doors
def open_doors(step, open_doors_list):
    for i in range(1, 101): # Door to toggle
        if i % step == 0:
            if i in open_doors_list:
                open_doors_list.remove(i)
            else:
                open_doors_list.append(i)

    return open_doors_list

# Skip pass 1, start from pass 2 and open doors
for i in range(2, 101):
    doors = open_doors(i, doors)

print("Final State of Doors")
print(doors)




