#!/usr/bin/python3
"""
Module: 0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each index represents a box,
                               and the value at each index is a list of keys
                               to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    unlocked_boxes = set()
    size = len(boxes)
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in unlocked_boxes and current_box < size:
            unlocked_boxes.add(current_box)
            for key in boxes[current_box]:
                if key not in unlocked_boxes:
                    stack.append(key)
    return len(unlocked_boxes) == size
