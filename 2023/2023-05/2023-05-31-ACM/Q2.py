import math
from collections import defaultdict
from sys import stdin

dist = lambda a, b: math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

if __name__ == "__main__":
    results = []
    for line in stdin:
        if not(len(line.strip())):
            break
        ins = list(map(float, line.strip().split(',')))

        nodes = []
        for i in range(1, len(ins), 2):
            nodes.append([(0.,0.), 0])
            nodes[-1][1] = float('inf')
            nodes[-1][0] = ins[i], ins[i + 1]
        nodes[0][1] = 0
        
        graph = defaultdict(dict)
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                d = dist(nodes[i][0], nodes[j][0])
                if d <= 100:
                    graph[i][j] = d
                    graph[j][i] = d

        unvisited = set(list(range(len(nodes))))
        while unvisited:
            m = -1
            for n in unvisited:
                if m < 0 or nodes[n][1] < nodes[m][1]:
                    m = n
            unvisited.remove(m)

            for adj, d in graph[m].items():
                new = d + nodes[m][1]
                if nodes[adj][1] > new:
                    nodes[adj][1] = new
        
        if nodes[-1][1] == float('inf'):
            results.append(-1)
        else:
            results.append(nodes[-1][1])
        
    print('\n'.join(map(lambda x: ("{:.2f}".format(x) if x > 0 else str(x)), results))) 