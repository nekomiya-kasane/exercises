from email.policy import default


from collections import defaultdict

rs = set()

#dp = []

# def gen_dp(m):
#     global dp, rs
#     dp = [-1 for _ in range(m)]
#     dp[0] = 0
#     for e in rs:
#         if e:
#             dp[e] = 1
    
#     while True:
#         last = dp.count(-1)
#         inds = [i for i, x in enumerate(dp) if x != -1]
#         for i in range(len(inds)):
#             for j in range(i + 1, len(inds)):
#                 dp[(i + j) % m] = min(dp[(i + j) % m], dp[i] + dp[j] + 1)
#         tmp = last
#         last = dp.count(-1)
#         if not last or tmp == last:
#             break

import bisect

def popmin(qu):
    lowest = 1000
    kl = None
    for key in qu:
        if qu[key] < lowest:
            lowest = qu[key]
            kl = key
    del qu[kl]
    return kl

def dijkstra(graph, st):
    qu = {}
    d = {}
    for v in graph:
        d[v] = 1000
    d[st] = 0
    for v in graph:
        qu[v] = d[v] 

    while qu:
        u = popmin(qu) 
        for v in graph[u].keys():
            w = graph[u][v]
            newd = d[u] + w
            if (newd < d[v]):
                qu[v] = newd
                d[v] = newd
    
    return d

def gen_graph(m):
    #global dp, rs
    global rs
    graph = defaultdict(lambda: defaultdict(int))

    for i in range(m):
        for j in rs:
            if not j:
                continue
            graph[i][(i + j) % m] = 1
    
    return graph



if __name__ == "__main__":
    while True:
        n, m = list(map(int, input().strip().split(' ')))

        rs = set()

        for i in range(10):
            rs.add((10 ** i) % m)
        
        rs = list(rs)

        arr = list(map(int, input().strip().split(' ')))
        #arr = [0, 1, 2, 3]

        graph = gen_graph(m)

        pt = []
        res = {}

        for e in arr:
            if e % m in res:
                pt.append(str(res[e % m]))
            else:
                mi = dijkstra(graph, e % m)
                pt.append(str(mi[0]))
                res[e % m] = mi[0]

        print(' '.join(pt))
    

    #gen_dp(m)

    # res = []
    # for e in arr:
    #     res.append(str(mi[e]))
    #     #res.append(str(dp[e]))

    #print(' '.join(res))


    
