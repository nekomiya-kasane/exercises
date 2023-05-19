class Graph:
    def __init__(self, lst):
        self.time = 0
        #self.traversal = []
        self.size = len(lst)
        self.graph_list = lst

        self.countCross = 0
        self.countBack = 0
    
    def print_graph_list(self):
        print("Adjacency List Representation:")
        for i in range(self.size):
            print(i, "-->", *self.graph_list[i])
        print()
    
    def dfs(self):
        self.visited = [False]*self.size
        self.visitedTime = [0]*self.size
        self.end_time = [0]*self.size
 
        for node in range(self.size):
            if not self.visited[node]:
                self.traverse_dfs(node)
        #print()
        #print("DFS Traversal: ", self.traversal)
        #print()
 
    def traverse_dfs(self, node):
        self.visited[node] = True
        #self.traversal.append(node)
        self.visitedTime[node] = self.time
        self.time += 1

        for neighbor in self.graph_list[node]:
            if not self.visited[neighbor]:
                self.traverse_dfs(neighbor)
            else:
                if self.visitedTime[node] > self.visitedTime[neighbor] and self.end_time[neighbor] == 0:
                    self.countBack += 1
                    # print('Back Edge:', str(node)+'-->'+str(neighbor))
                elif self.visitedTime[node] > self.visitedTime[neighbor] and self.end_time[neighbor]:
                    self.countCross += 1
                    # print('Cross Edge:', str(node)+'-->'+str(neighbor))
            self.time += 1
        self.end_time[node] = self.time
 
 
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
    G.dfs()

    print("{} {}".format(G.countBack, G.countCross))