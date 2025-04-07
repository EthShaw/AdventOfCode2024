#!/bin/env python
import sys

with open(sys.argv[1]) as file:
    # Strip the trailing newline off all lines
    lines = [line.rstrip() for line in file.readlines()]

width = len(lines[0])
height = len(lines)

class Node():
    def __init__(self, plant, row, col):
        self.plant = plant
        self.row = row
        self.col = col
        self.connections = set()
        # Used when finding the regions
        self.marked = False

gardenGraph: list[list[Node]] = [[None] * width for _ in range(height)]

def nodeAt(row, col):
    if row < 0 or col < 0 or row >= height or col >= height:
        return None
    return gardenGraph[row][col]


# Initialize the garden graph from the lines
for row in range(height):
    for col in range(width):
        plant = lines[row][col]
        node = Node(plant, row, col)
        gardenGraph[row][col] = node
        # Check the row and column before to see if connection
        # is needed for the new node
        above = nodeAt(row - 1, col)
        left = nodeAt(row, col - 1)
        if above is not None and above.plant == node.plant:
            above.connections.add(node)
            node.connections.add(above)
        if left is not None and left.plant == node.plant:
            left.connections.add(node)
            node.connections.add(left)


def addConnected(plant: str, node: Node, region: list[Node]):
    if node is None or node.marked:
        # Past the border, or node already searched
        return
    if node.plant != plant:
        # Node is a different plant than the region being formed
        return
    node.marked = True
    region.append(node)
    # Add connected nodes in all directions
    addConnected(plant, nodeAt(node.row - 1, node.col), region)
    addConnected(plant, nodeAt(node.row, node.col - 1), region)
    addConnected(plant, nodeAt(node.row + 1, node.col), region)
    addConnected(plant, nodeAt(node.row, node.col + 1), region)


regions: list[list[Node]] = []

# Find all the regions
for row in range(height):
    for col in range(width):
        node = gardenGraph[row][col]
        if node.marked:
            continue
        region = []
        addConnected(node.plant, node, region)
        regions.append(region)

result = 0

# Compute area and perimiter of each region based on
# number of nodes and number of edges per node
for region in regions:
    area = len(region)
    # Compute the total number of "missing" edges (connections) - i.e.,
    # every node in the graph should have 4 edges except ones that
    # are on the parimeter.
    missingEdges = 0
    for node in region:
        missingEdges += 4 - len(node.connections)
    perimeter = missingEdges
    result += area * perimeter
    #print(f"Region {region[0].plant} area {area} perimeter {perimeter}")

print(f"Part 1 result: {result}")
