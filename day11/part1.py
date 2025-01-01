#!/bin/env python
import sys
import math

with open(sys.argv[1]) as file:
    # Strip any trailing newline off the line
    text = file.read().strip()

class Stone:
    def __init__(self, value):
        self.value = value
    # Put the next stone in the sequence into the given array.
    # The stone may reuse itself and modify its value.
    def fillNext(self, array: list):
        if self.value == 0:
            self.value = 1
            array.append(self)
        else:
            numDigits = math.floor(math.log10(self.value)) + 1
            if numDigits % 2 == 0:
                leftValue = self.value // (10**(numDigits / 2))
                rightValue = self.value - (leftValue * (10**(numDigits / 2)))
                self.value = leftValue
                array.append(self)
                array.append(Stone(rightValue))
            else:
                self.value *= 2024
                array.append(self)

stonesText = text.split(" ")

stones = []
for stoneText in stonesText:
    stones.append(Stone(int(stoneText)))

def printStones(stones):
    for stone in stones:
        print(int(stone.value), end=" ")
    print("")

#printStones(stones)

for i in range(25):
    newStones = []
    for stone in stones:
        stone.fillNext(newStones)
    stones = newStones
    print(i)
    #printStones(stones)

print(f"Part 1: {len(stones)}")