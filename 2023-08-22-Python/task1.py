""" 
COMP20008 Semester 2
Assignment 1 Task 1
"""

# Task 1 - Summary Statistics (1 mark)
def task1(dataset_filename):
    # Implement Task 1 here
    lines = []
    with open(dataset_filename, 'r', encoding='utf8') as f:
        head = f.readline()
        lines = f.readlines()

    c, r = 0, 0
    lines = list(map(lambda x: x.strip(), lines))
    for line in lines:
        c = max(len(line), c)
    r = len(lines)

    return [f"Number of rows: {r}", f"Number of columns: {len(head.split(','))}"]
