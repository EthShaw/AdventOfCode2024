#!/bin/env python
import sys
import math

with open(sys.argv[1]) as file:
    # Strip any trailing newline off the line
    text = file.read().strip()

# This design does not preserve order, but we actually don't need to for the problem,
# even though it says their order is preserved.
def fillNext(stoneValue, stones: dict, count):
    newValues = []
    if stoneValue == 0:
        newValues.append(1)
    else:
        numDigits = math.floor(math.log10(stoneValue)) + 1
        if numDigits % 2 == 0:
            leftValue = stoneValue // (10**(numDigits / 2))
            rightValue = stoneValue - (leftValue * (10**(numDigits / 2)))
            stoneValue = leftValue
            newValues.append(stoneValue)
            newValues.append(rightValue)
        else:
            stoneValue *= 2024
            newValues.append(stoneValue)
    for val in newValues:
        if not val in stones:
            stones[val] = 0
        stones[val] += count

stonesText = text.split(" ")

def printStones(stones):
    for stone in stones:
        print(int(stone.value), end=" ")
    print("")

# Map stone number to the stones it produces so it only needs to be computed once
stoneBlinkMap = dict()

# All the stones stored as a map of stone # -> count of stone #
currStones = dict()

for stoneText in stonesText:
    stoneInt = int(stoneText)
    if not stoneInt in currStones:
        currStones[stoneInt] = 0
    currStones[stoneInt] += 1

for i in range(75):
    newStones = dict()
    for stone, count in currStones.items():
        fillNext(stone, newStones, count)
    currStones = newStones
    print(i)

result = sum(currStones.values())
print(f"Part 2: {result}")
