""" 
COMP20008 Semester 2
Assignment 1 Task 2
"""

# Task 2 - Data Cleaning (2 marks)
def task2(dataset_filename, output_filename):
    # Implement Task 2 here
    lines = []
    head = ''
    with open(dataset_filename, 'r', encoding='utf8') as f:
        head = f.readline().strip()
        lines = f.readlines()
    
    def resolve_line(line):
        if len(line) != 3:
            line = [','.join(line[:-2]), line[-2], line[-1]]
        line[1] = str(int(eval(line[1].replace('k', '*1000').replace('K', '*1000').replace('m', '*1000000').replace('M', '*1000000')[:-5])))
        tri = line[2].split(' ')
        time = int(tri[0])
        if tri[1].lower()[:4] == 'hour':
            time = time * 60
        elif tri[1].lower()[:3] == 'day':
            time = time * 60 * 24
        elif tri[1].lower()[:5] == 'month':
            time = time * 60 * 24 * 30
        elif tri[1].lower()[:4] == 'year':
            time = time * 60 * 24 * 365
        elif tri[1].lower()[:4] == 'week':
            time = time * 60 * 24 * 7
        line[2] = str(time)
        return line

    lines = list(map(lambda x: resolve_line(x.strip().split(',')), lines))

    with open(output_filename, 'w') as f:
        f.write(head + '\n')
        for line in lines:
            print(line[0] + "," + line[1] + "," + line[2] + "\n")
            f.write(line[0] + "," + line[1] + "," + line[2] + "\n")
