#!/bin/env python
import sys

with open(sys.argv[1]) as file:
    # Strip the trailing newline off all lines
    lines = [line.rstrip() for line in file.readlines()]

blocks = set()
startingPos = None
width = len(lines[0])
height = len(lines)

row = 0
col = 0
for line in lines:
    col = 0
    for char in line:
        if char == "#":
            blocks.add((row, col))
        elif char == "^":
            startingPos = (row, col)
        col += 1
    row += 1

path = []

def getNextPos(obstacles, currPos, currDir):
    nextPos = (currPos[0] + currDir[0], currPos[1] + currDir[1])
    if not nextPos in obstacles:
        return (nextPos, currDir)
    # Rotate 90 degrees right
    nextDir = (currDir[1], -currDir[0])
    return getNextPos(obstacles, currPos, nextDir)

direc = (-1, 0)
guardPos = startingPos
while guardPos[0] >= 0 and guardPos[0] < width and guardPos[1] >= 0 and guardPos[1] < height:
    path.append(guardPos)
    (guardPos, direc) = getNextPos(blocks, guardPos, direc)

distinctPositions = set(path)

for pos in distinctPositions:
    lines[pos[0]] = lines[pos[0]][:pos[1]] + "X" + lines[pos[0]][pos[1]+1:]

# 5177
print(f"Part 1: {len(distinctPositions)}")

# Part 2
def mapHasLoop(obstacles, startingPos):
    visitedVectors = set()
    direc = (-1, 0)
    guardPos = startingPos
    while guardPos[0] >= 0 and guardPos[0] < width and guardPos[1] >= 0 and guardPos[1] < height:
        visitedVectors.add((guardPos, direc))
        (guardPos, direc) = getNextPos(obstacles, guardPos, direc)
        if (guardPos, direc) in visitedVectors:
            return True
    return False

possibleBlocksCount = 0

# There's probably a more efficient algorithm to compute loops. Probably involves
# looking at the path without any obstacles added and only adding obstacles along
# that path.
for row in range(height):
    for col in range(width):
        if row == startingPos[0] and col == startingPos[1]:
            continue
        newBlocks = blocks.copy()
        newBlocks.add((row, col))
        if mapHasLoop(newBlocks, startingPos):
            # print((row, col))
            possibleBlocksCount += 1

# 1686
print(f"Part 2: {possibleBlocksCount}")