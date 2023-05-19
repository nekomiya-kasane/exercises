class Graph:
    def __init__(self, lst):
        self.size = len(lst)
        self.graph_list = lst

    def bfs(self, node):
        if self.size < 2:
            return 0, 0
        
        dists = {i: None for i in range(self.size)}
        dist = 0
        last = set([node])
        visited = set([node])
        while len(last):
            new = set()
            for e in last:
                dists[e] = dist
                new |= set(self.graph_list[e])
            new -= visited
            last = new
            visited |= last
            dist += 1
        
        return dist - 1, max([k for k, v in dists.items() if v == dist - 1])
 
if __name__ == "__main__":
    n = int(input())
    lst = [[] * n for _ in range(n)]

    i = 0
    while True:
        s = input().strip()
        tars = list(map(int, s.split(' '))) if s != '' else []
        if i < n:
            tars.sort()
            lst[i] = tars
        if len(tars) == 1 and tars[0] == 0:
            break
        i += 1

    G = Graph(lst)
    # G.print_graph_list()
    a, b = G.bfs(1)

    #print("{} {}".format(G.countBack, G.countCross))
    print("{} {}".format(a, b))