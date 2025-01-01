#!/bin/env python
import sys

with open(sys.argv[1]) as file:
    # Strip any trailing newline off the line
    text = file.read().strip()

isFreeSpace = False
fileId = 0
blocks = []
for ch in text:
    if isFreeSpace:
        for i in range(int(ch)):
            blocks.append(-1)
    else:
        for i in range(int(ch)):
            blocks.append(fileId)
        fileId += 1
    isFreeSpace = not isFreeSpace

def printBlocks(blocks):
    strArr = []
    for num in blocks:
        if num == -1:
            strArr.append(".")
        else:
            strArr.append(str(num))

    print(str.join('', strArr))

rightPtr = len(blocks) - 1
leftPtr = 0
while leftPtr < rightPtr:
    if blocks[rightPtr] == -1:
        rightPtr -= 1
        continue
    if blocks[leftPtr] == -1:
        blocks[leftPtr] = blocks[rightPtr]
        blocks[rightPtr] = -1
        rightPtr -= 1
    leftPtr += 1

def checksum(data):
    chksum = 0
    for i in range(len(data)):
        if data[i] == -1:
            continue
        chksum += i * data[i]
    return chksum

print(checksum(blocks))
