#!/bin/env python
import sys

with open(sys.argv[1]) as file:
    # Strip the trailing newline off all lines
    lines = [line.rstrip() for line in file.readlines()]

def getCharAt(row, col):
    if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
        return None
    return lines[row][col]

xmasCount = 0

searchDirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
for row in range(len(lines)):
    for col in range(len(lines[0])):
        for dir in searchDirs:
            if (getCharAt(row, col) == "X" and
                getCharAt(row + dir[0], col + dir[1]) == "M" and
                getCharAt(row + dir[0] * 2, col + dir[1] * 2) == "A" and
                getCharAt(row + dir[0] * 3, col + dir[1] * 3) == "S"):
                xmasCount += 1

print(f"Part 1 Christmas count: {xmasCount}")

# For part 2, there's basically 4 configurations the X can be in, so we just check
# them manually.
crossingMasCount = 0
for row in range(len(lines)):
    for col in range(len(lines[0])):
        # This is such an ugly set of conditions
        if getCharAt(row, col) == "A":
            if ((getCharAt(row - 1, col - 1) == "M" and
                 getCharAt(row + 1, col + 1) == "S") or
                (getCharAt(row - 1, col - 1) == "S" and
                 getCharAt(row + 1, col + 1) == "M")):
                if ((getCharAt(row - 1, col + 1) == "M" and
                     getCharAt(row + 1, col - 1) == "S") or
                    (getCharAt(row - 1, col + 1) == "S" and
                     getCharAt(row + 1, col - 1) == "M")):
                    crossingMasCount += 1

print(f"Part 2 Crossing MAS count: {crossingMasCount}")
