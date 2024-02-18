""" 
COMP20008 Semester 2
Assignment 1 Task 4
"""

import regex as re

# Task 4 - Text Preprocessing (1 mark)
def task4(dataset_filename, output_filename):
    # Implement Task 4 here
    data = []
    head = ''

    with open(dataset_filename, 'r', encoding='utf8') as f:
        head = f.readline().strip()
        data = list(map(lambda x: x.strip().split(','), f.readlines()))

    data = [[','.join(x[:-2]), x[-2], x[-1]] for x in data]
    for i in range(len(data)):
        title = data[i][0]
        new_title = ''
        for e in title:
            if e.isalpha() or e == ' ':
                new_title += e
        data[i].append(str(re.sub(' +', ' ', new_title.lower()).split(' ')))

    with open(output_filename, 'w') as f:
        f.write(head + ",words\n")
        for e in data:
            f.write(','.join(e) + "\n")

            
        
    return
