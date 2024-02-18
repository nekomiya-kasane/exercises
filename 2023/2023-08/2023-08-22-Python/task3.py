""" 
COMP20008 Semester 2
Assignment 1 Task 3
"""

import matplotlib.pyplot as plt

# Task 3 - Preliminary Visualisation (1 mark)
def task3(dataset_filename, output_filename):
    # Implement Task 3 here
    data = []
    with open(dataset_filename, 'r', encoding='utf8') as f:
        f.readline()
        data = list(map(lambda x: list(map(int, x.strip().split(',')[-2:])), f.readlines()))
    fig = plt.figure(figsize=(8,8))
    plt.scatter([x[1] for x in data], [x[0] for x in data])
    plt.xlabel('Number of minutes ago')
    plt.ylabel('Number of views')
    plt.title('Views w.r.t. time')
    plt.savefig(output_filename)
