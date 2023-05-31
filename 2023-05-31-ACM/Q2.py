import math
from collections import defaultdict
from sys import stdin

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

class Node:
    weight = 0
    loc = (0., 0.)

if __name__ == "__main__":
    #m = int(input())

    res = []
    #for _ in range(m):
    for line in stdin:
        #nums = list(map(float, input().strip().split(',')))
        if line == '\n':
            break
        nums = list(map(float, line.strip().split(',')))
        nodes = []
        for i in range(1, len(nums), 2):
            nodes.append(Node())
            nodes[-1].weight = float('inf')
            nodes[-1].loc = nums[i], nums[i + 1]
        nodes[0].weight = 0
        
        # Set up graph
        G = defaultdict(dict)
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                d = dist(nodes[i].loc, nodes[j].loc)
                if d <= 100:
                    G[i][j] = d
                    G[j][i] = d
        
        # Dijkstra’s
        unvisited = set([i for i in range(len(nodes))])
        while unvisited:
            mi = -1
            for n in unvisited:
                if mi < 0 or nodes[n].weight < nodes[mi].weight:
                    mi = n
            unvisited.remove(mi)

            for neighbor, d in G[mi].items():
                newDist = d + nodes[mi].weight
                if nodes[neighbor].weight > newDist:
                    nodes[neighbor].weight = newDist
        
        res.append(-1 if nodes[-1].weight == float('inf') else nodes[-1].weight)
        
    print('\n'.join(map(lambda x: ("{:.2f}".format(x) if x > 0 else str(x)), res))) # type: ignore