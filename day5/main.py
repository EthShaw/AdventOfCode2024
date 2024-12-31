#!/bin/env python
import sys

with open(sys.argv[1]) as file:
    # Strip the trailing newline off all lines
    lines = [line.rstrip() for line in file.readlines()]

rulesText = lines[0:lines.index("") - 1]
ordersText = lines[lines.index("") + 1:]

# Map the first page in a pair to the second
rules = dict()
for ruleTxt in rulesText:
    pair = ruleTxt.split("|")
    # There can be multiple rules with the same left-hand page
    if not pair[0] in rules:
        rules[pair[0]] = []
    rules[pair[0]].append(pair[1])

middleSum = 0
wrongOrders = []
for orderTxt in ordersText:
    order = orderTxt.split(",")
    passedPages = set()
    succeed = True
    for leftPage in order:
        # If this page must come before some other page, but that page
        # has already been passed, that is a violation
        if leftPage in rules:
            for rightPage in rules[leftPage]:
                if rightPage in passedPages:
                    succeed = False
                    break
        passedPages.add(leftPage)
    if succeed:
        middlePage = order[len(order) // 2]
        middleSum += int(middlePage)
    else:
        wrongOrders.append(order)

print(f"Part 1: {middleSum}")

fixedMiddleSum = 0

for order in wrongOrders:
    order: list
    # The rules that affect this order
    effectiveRules = dict()
    effectiveInverseRules = dict()
    for leftPage in order:
        if leftPage in rules:
            effectiveRules[leftPage] = rules[leftPage]
            for rightPage in rules[leftPage]:
                if not rightPage in effectiveInverseRules:
                    effectiveInverseRules[rightPage] = []
                effectiveInverseRules[rightPage].append(leftPage)

    newOrder = []
    while len(order) > 0:
        for page in order:
            if page in effectiveInverseRules:
                mustBeBefore = effectiveInverseRules[page]
                skip = False
                for beforePage in mustBeBefore:
                    # If a page that must go before this one has not been added yet,
                    # we cannot continue with the current page
                    if beforePage in order:
                        skip = True
                        break
                if skip:
                    continue
            order.remove(page)
            newOrder.append(page)
            break
    fixedMiddleSum += int(newOrder[len(newOrder) // 2])

print(f"Part 2: {fixedMiddleSum}")