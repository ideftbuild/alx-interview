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
    size = len(boxes)
    if size == 1:
        return True
    unlocked_boxes = {0}
    check_boxes(0, boxes, size, unlocked_boxes)
    return len(unlocked_boxes) == size


def check_boxes(current_box, boxes, size, unlocked_boxes):
    """
    Recursively checks and unlocks boxes using available keys.

    Args:
        current_box (int): The index of the current box being unlocked.
        boxes (list of lists): A list of boxes where each box contains keys
                            to other boxes.
        size (int): Total number of boxes
        unlocked_boxes (set): A set of box indices that have been unlocked.
    """
    keys_to_use = boxes[current_box]
    for next_box in keys_to_use:
        if next_box not in unlocked_boxes and next_box < size:
            unlocked_boxes.add(next_box)
            check_boxes(next_box, boxes, size, unlocked_boxes)
