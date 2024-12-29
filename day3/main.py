#!/bin/env python
import sys
import re

with open(sys.argv[1]) as file:
    text = file.read()

def getPairs(txt):
    return re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", txt)
multPairs = getPairs(text)

sum = 0
for pair in multPairs:
    sum += int(pair[0]) * int(pair[1])

print(sum)

# Part 2
pieces = text.split("don't()")
print(len(pieces))

newText = pieces[0]
for piece in pieces[1:]:
    dontAndDo = piece.split('do()', 1)
    if len(dontAndDo) > 1:
        newText += "do()" + dontAndDo[1]

multPairs = getPairs(newText)
sum = 0
for pair in multPairs:
    sum += int(pair[0]) * int(pair[1])

print(sum)
