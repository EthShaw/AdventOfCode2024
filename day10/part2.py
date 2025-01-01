#!/bin/env python
import sys

with open(sys.argv[1]) as file:
    # Strip the trailing newline off all lines
    lines = [line.rstrip() for line in file.readlines()]

# Convert grid into a graph
class Node:
    def __init__(self, value):
        self.value = value
        # Parents are adjacent nodes with values less than self
        self.parents = set()
        # Children are adjacent nodes with values greater than self
        self.children = set()

width = len(lines[0])
height = len(lines)

def getValueAt(row, col):
    if row < 0 or row >= height or col < 0 or col >= width:
        return None
    return int(lines[row][col])

nodes = []

# Generate all nodes
for row in range(height):
    rowArray = []
    nodes.append(rowArray)
    for col in range(width):
        rowArray.append(Node(getValueAt(row, col)))

def getNodeAt(row, col):
    if row < 0 or row >= height or col < 0 or col >= width:
        return None
    return nodes[row][col]

# Compute parents / children of nodes based on values.
for row in range(height):
    for col in range(width):
        # Only need to check for children and fill in self as parent
        # since every node will do this
        adjacents = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
        node: Node = getNodeAt(row, col)
        for (childRow, childCol) in adjacents:
            adjNode: Node = getNodeAt(childRow, childCol)
            if adjNode is None:
                continue
            # Children are nodes with values greater by exactly 1
            if node.value + 1 == adjNode.value:
                node.children.add(adjNode)
                adjNode.parents.add(node)

# Find the total number of unique paths from the node to a
# node with value 9, which is what I accidently at one point
# during my development of part 1.
def computeRating(node: Node):
    if node.value == 9:
        return 1
    sum = 0
    for child in node.children:
        sum += computeRating(child)
    return sum

totalSum = 0
# Find all the trailheads and compute score of each
for row in range(height):
    for col in range(width):
        node = nodes[row][col]
        if node.value != 0:
            continue
        score = computeRating(nodes[row][col])
        totalSum += score

print(f"Part 1: {totalSum}")
