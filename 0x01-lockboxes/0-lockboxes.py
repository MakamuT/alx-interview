#!/usr/bin/python3
"""
method that determines if all the boxes can be opened
"""
def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]

    while keys:
        key = keys.pop()
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])
    
    return all(unlocked)
