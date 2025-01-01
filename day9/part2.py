#!/bin/env python
import sys

with open(sys.argv[1]) as file:
    # Strip any trailing newline off the line
    text = file.read().strip()

class FreeSpace:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    def __str__(self):
        return f"(pos:{self.pos},size:{self.size})"

class FileRecord:
    def __init__(self, pos, size, fileId):
        self.pos = pos
        self.size = size
        self.fileId = fileId

    def __str__(self):
        return f"(pos:{self.pos},size:{self.size},id:{self.fileId})"


def printBlocks(blocks):
    strArr = []
    for num in blocks:
        if num == -1:
            strArr.append(".")
        else:
            strArr.append(str(num))

    print(str.join('', strArr))

def toBlocks(fileList):
    filesSorted = sorted(fileList, key=lambda file : file.pos)

    blocks = []
    currIdx = 0
    for file in filesSorted:
        while file.pos > currIdx:
            blocks.append(-1)
            currIdx += 1
        for i in range(file.size):
            blocks.append(file.fileId)
            currIdx += 1
    return blocks

isFreeSpace = False
fileId = 0
# Tuples (startIndex, length)
freeList = []
# Tuples (startIndex, length, fileId)
fileList = []
pos = 0
for ch in text:
    if isFreeSpace:
        freeList.append(FreeSpace(pos, int(ch)))
    else:
        fileList.append(FileRecord(pos, int(ch), fileId))
        fileId += 1
    pos += int(ch)
    isFreeSpace = not isFreeSpace

# Loop from back to front of the file list
fileList.reverse()
for file in fileList:
    for space in freeList:
        # Only check spaces to the left of the file
        if space.pos > file.pos:
            break
        if space.size >= file.size:
            file.pos = space.pos
            space.size -= file.size
            space.pos += file.size
            break

blocks = toBlocks(fileList)
# printBlocks(blocks)

def checksum(data):
    chksum = 0
    for i in range(len(data)):
        if data[i] == -1:
            continue
        chksum += i * data[i]
    return chksum

print(checksum(blocks))
