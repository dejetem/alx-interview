#!/usr/bin/python3
"""
To determine which boxes can be opened
"""


def canUnlockAll(boxes):
    x = len(boxes)
    stack = [0]
    unlocked = [1] + [0] * (x - 1)
    i = 0
    if x == 0:
        return True
    while stack:
        y = stack.pop()
        for index in boxes[y]:
            if index > 0 and index < x and unlocked[index] == 0:
                unlocked[index] = 1
                stack.append(index)
        i = i + 1
    if 0 in unlocked:
        return False
    return True
