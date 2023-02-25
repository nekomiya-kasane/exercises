 
from collections import deque, defaultdict
from email.policy import default
import math

def find_max(graph, src):
    q = deque()
 
    vs = set([src])
    q.append((src, 0, vs))
 
    mx = -1
    while q:
        v, w, vs = q.popleft()

        mx = max(mx, w)
        for j, tw in graph[v].items():
            if not j in vs:
                s = set(vs)
                s.add(j)
                q.append((j, w + tw, s))
 
    return mx

if __name__ == "__main__":
    # int(input())
    # takaras = list(map(int, input().strip().split(' ')))
    # ws = list(map(int, input().strip().split(' ')))

    takaras = [2,3,4,5]
    ws = [2,5,2,4]

    n = max(takaras)

    graph = defaultdict(lambda: defaultdict(int))

    for i in range(int((n + 1) / 2) + 1):
        graph[i][2 * i] = ws[takaras.index(2 * i)] if 2 * i in takaras else 0
        graph[i][2 * i + 1] = ws[takaras.index(2 * i + 1)] if 2 * i + 1 in takaras else 0

    print(find_max(graph, 1))
