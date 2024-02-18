""" 
COMP20008 Semester 2
Assignment 1 Task 5
"""
from collections import defaultdict
import json, math
import matplotlib.pyplot as plt

# Task 5 - Preliminary Analysis (1 mark)
def task5(dataset_filename, json_output_filename, plot_output_filename):
    # Implement Task 5 here
    data = []

    with open(dataset_filename, 'r', encoding='utf8') as f:
        f.readline().strip()
        data = list(map(lambda x: x.strip().split('['), f.readlines()))
    data = [[x[0].split(','), eval('[' + x[1])] for x in data]
    data = [[''.join(x[0][:-3]), x[0][-3], x[0][-2], x[1]] for x in data]

    counts = defaultdict(int)
    views = defaultdict(int)
    for i in range(len(data)):
        added = set()
        for word in data[i][-1]:
            if word not in added:
                counts[word] += 1
                views[word] += int(data[i][-3])
                added.add(word)
               
    for k, v in counts.items():
        if v >= 5:
            views[k] = int(round(float(views[k]) / v))
        else:
            del views[k]
    
    with open(json_output_filename, "w") as f:
        json.dump(views, f, indent=2)

    most = [[k, v] for k, v in views.items()]
    most.sort(key=lambda x: x[1], reverse=True)
    most = most[:5]

    fig = plt.figure(figsize = (8, 8))
    names = [e[0] for e in most]
    values = [e[1] for e in most]

    plt.bar(range(len(most)), values, tick_label=names)
    plt.xlabel("Word")
    plt.ylabel("Average Views")
    plt.title("Keyword that results in the highest views")
    plt.savefig(plot_output_filename)

    



