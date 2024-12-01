#!/bin/env python
import sys

with open(sys.argv[1]) as file:
    lines = file.readlines()

lines = [line.split(' ', 1) for line in lines if line.strip() != ""]

list1 = [int(line[0].strip()) for line in lines]
list2 = [int(line[1].strip()) for line in lines]

list1.sort()
list2.sort()
sum = 0

for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(f"Part 1: {sum}")

# Part 2 - there's definitely easier (but maybe less efficient)
# ways to do this, but this was fun
list1Idx = 0
list2Idx = 0
# The sum of all similarity scores
result = 0

while list1Idx < len(list1):
    num = list1[list1Idx]
    list1Idx += 1

    # There may be some duplicates which must be accounted for
    list1Count = 1
    while list1Idx < len(list1) and list1[list1Idx] == num:
        list1Count += 1
        list1Idx += 1
        continue

    # The number of times num (from the first list) appears in the second list
    list2Count = 0
    # Skip anything that doesn't exist in the first list at all
    while list2[list2Idx] < num:
        list2Idx += 1
    # Count number of times num appears (if any)
    while list2[list2Idx] == num:
        list2Idx += 1
        list2Count += 1

    # The similarity score
    score = num * list1Count * list2Count
    result += score

print(f"Part 2: {result}")