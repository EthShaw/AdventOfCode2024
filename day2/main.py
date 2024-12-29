#!/bin/env python
import sys

with open(sys.argv[1]) as file:
    lines = file.readlines()

safeCount = 0

for line in lines:
    safe = True
    nums = [int(num) for num in line.split()]
    lastSign = None
    for index in range(len(nums) - 1):
        diff = nums[index] - nums[index + 1]
        diffabs = abs(diff)
        if diffabs < 1 or diffabs > 3:
            safe = False
            break
        diffSign = diff / diffabs
        if lastSign is not None and lastSign != diffSign:
            safe = False
            break
        lastSign = diffSign
    if safe:
        safeCount += 1

print(f"Part 1: {safeCount}")

# We'll just do this the brute force way
# We assume lines contains no blank lines
safeCount = len(lines)

def isSafe(report):
    safe = True
    lastSign = None
    for index in range(len(nums) - 1):
        diff = nums[index] - nums[index + 1]
        diffabs = abs(diff)
        if diffabs < 1 or diffabs > 3:
            safe = False
            break
        diffSign = diff / diffabs
        if lastSign is not None and lastSign != diffSign:
            safe = False
            break
        lastSign = diffSign
    return safe

for line in lines:
    nums = [int(num) for num in line.split()]
    if isSafe(nums):
        continue
    toRemove = 0
    safe = False
    while toRemove < len(nums):
        removed = nums.pop(toRemove)
        if isSafe(nums):
            safe = True
            break
        nums.insert(toRemove, removed)
        toRemove = toRemove + 1
    if not safe:
        safeCount -= 1

print(f"Part 2: {safeCount}")