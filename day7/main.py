#!/bin/env python
import sys

with open(sys.argv[1]) as file:
    # Strip the trailing newline off all lines
    lines = [line.rstrip() for line in file.readlines()]

def getEqnValue(coefs, runningSum=None):
    if len(coefs) == 0:
        yield runningSum
        return
    if runningSum is None:
        yield from getEqnValue(coefs[1:], coefs[0])
    else:
        yield from getEqnValue(coefs[1:], coefs[0] + runningSum)
        yield from getEqnValue(coefs[1:], coefs[0] * runningSum)

validCount = 0
validSum = 0
for line in lines:
    pair = line.split(": ")
    calRes = int(pair[0])
    coefs = [int(num) for num in pair[1].split(" ")]
    
    for val in getEqnValue(coefs):
        if val == calRes:
            validCount += 1
            validSum += calRes
            break

print(f"Part 1: {validSum}")

# Part 2
def concat(a, b):
    tempB = b
    while tempB > 0:
        tempB = tempB // 10
        a *= 10
    return a + b

def getEqnValue2(coefs, resVal, runningSum=None):
    if len(coefs) == 0:
        yield runningSum
        return
    if runningSum is None:
        yield from getEqnValue2(coefs[1:], resVal, coefs[0])
        return
    if runningSum > resVal:
        # Prune this branch because it already failed
        yield runningSum
        return

    yield from getEqnValue2(coefs[1:], resVal, coefs[0] * runningSum)
    yield from getEqnValue2(coefs[1:], resVal, coefs[0] + runningSum)
    yield from getEqnValue2(coefs[1:], resVal, concat(runningSum, coefs[0]))

validCount2 = 0
validSum2 = 0
for line in lines:
    pair = line.split(": ")
    calRes = int(pair[0])
    coefs = [int(num) for num in pair[1].split(" ")]
    
    for val in getEqnValue2(coefs, calRes):
        if val == calRes:
            validCount2 += 1
            validSum2 += calRes
            break

print(f"Part 2: {validSum2}")