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
    out = []
    while True:
        head = input()
        if head.strip() == '' or head.strip() == '0':
            break
        n = int(head)
        lst = [[] * n for _ in range(n)]

        for i in range(n):
            s = input().strip()
            tars = list(map(int, s.split(' '))) if s != '' else []
            tars.sort()
            lst[i] = tars

        G = Graph(lst)
            # G.print_graph_list()
        a, b = G.bfs(1)

        out.append("{} {}".format(a,b))

    for o in out:
        print(o)
