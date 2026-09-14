# ANSWER KEY - Python Review 5 (Linear Search and Binary Search)
# Do not put this file in the students' repository.

# Exercise 1 -----------------------------------------------------------------
# Linear search. Do NOT stop at the first match - keep going to the end.

def find_all_positions(data, target):
    positions = []
    for i in range(len(data)):
        if data[i] == target:
            positions.append(i)
    return positions


# Exercise 2 -----------------------------------------------------------------
# Linear search on records. Each record is [id, name, score].
# The list is not sorted by id, so binary search is impossible here.

def find_student_by_id(records, student_id):
    for i in range(len(records)):
        record = records[i]
        if record[0] == student_id:
            return record[1]        # the name
    return None                     # checked everything, not found


# Exercise 3 -----------------------------------------------------------------
# Standard binary search, plus a counter for how many middles we looked at.

def binary_search_steps(data, target):
    low = 0
    high = len(data) - 1
    steps = 0

    while low <= high:
        steps = steps + 1
        mid = (low + high) // 2

        if data[mid] == target:
            return [mid, steps]
        elif data[mid] < target:
            low = mid + 1           # target must be to the RIGHT
        else:
            high = mid - 1          # target must be to the LEFT

    return [-1, steps]              # range became empty


# Exercise 4 -----------------------------------------------------------------
# Binary search for the leftmost position where value fits.
# Two differences from Exercise 3:
#   1. high starts at len(data), not len(data) - 1  (answer can be "past the end")
#   2. we never test for ==, we just narrow until low and high meet

def find_insert_position(data, value):
    low = 0
    high = len(data)

    while low < high:
        mid = (low + high) // 2
        if data[mid] < value:
            low = mid + 1           # value belongs to the right of mid
        else:
            high = mid              # mid itself might be the answer - keep it

    return low                      # low == high, that is the spot


# Exercise 5 -----------------------------------------------------------------
# Two binary searches.
# When we find a match we do NOT stop - we record it and keep searching
# left (for the first) or right (for the last).

def first_and_last_position(data, target):
    # --- search 1: leftmost ---
    first = -1
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            first = mid
            high = mid - 1          # found one, but look further LEFT
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if first == -1:                 # not in the list at all
        return [-1, -1]

    # --- search 2: rightmost ---
    last = -1
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            last = mid
            low = mid + 1           # found one, but look further RIGHT
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return [first, last]
