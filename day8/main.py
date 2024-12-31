#!/bin/env python
import sys

with open(sys.argv[1]) as file:
    # Strip the trailing newline off all lines
    lines = [line.rstrip() for line in file.readlines()]

row = 0
antennas = dict()
for line in lines:
    col = 0
    for ch in line:
        if ch != ".":
            if not ch in antennas:
                antennas[ch] = list()
            antennas[ch].append((row, col))
        col += 1
    row += 1

width = len(lines[0])
height = len(lines)
def isInBounds(antinode):
    return antinode[0] >= 0 and antinode[0] < height and antinode[1] >= 0 and antinode[1] < width

antinodes = set()
for type in antennas.keys():
    for ant1 in antennas[type]:
        for ant2 in antennas[type]:
            if ant1 == ant2:
                continue
            diff = ((ant1[0] - ant2[0]), (ant1[1] - ant2[1]))
            antinode = (ant1[0] + diff[0], ant1[1] + diff[1])
            if isInBounds(antinode):
                antinodes.add(antinode)

print(f"Part 1: {len(antinodes)}")

# Part 2
antinodes = set()
for type in antennas.keys():
    for ant1 in antennas[type]:
        for ant2 in antennas[type]:
            if ant1 == ant2:
                continue
            diff = ((ant1[0] - ant2[0]), (ant1[1] - ant2[1]))
            antinode = (ant1[0], ant1[1])
            while isInBounds(antinode):
                antinodes.add(antinode)
                antinode = (antinode[0] + diff[0], antinode[1] + diff[1])

print(f"Part 2: {len(antinodes)}")
