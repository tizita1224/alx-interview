#!/usr/bin/python3
'''
The code that checks if all boxes can be opened
'''
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened with the available keys.

    Args:
        boxes (list of list): A list where each element is a list of keys
                               corresponding to a box. The index of the
                               outer list represents the box number.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Initialize a set to keep track of opened boxes
    opened_boxes = set()
    # Initialize a list (queue) to keep track of boxes to check, starting with
    # box 0
    queue = [0]

    while queue:
        # Pop the first box from the queue
        current_box = queue.pop(0)

        # If this box has not been opened yet, open it
        if current_box not in opened_boxes:
            opened_boxes.add(current_box)  # Mark the box as opened
            # Get the keys in the current box
            keys = boxes[current_box]
            # Add keys to the queue if they lead to unopened boxes
            for key in keys:
                if key < len(boxes) and key not in opened_boxes:
                    queue.append(key)  # Add the unopened box to the queue

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)