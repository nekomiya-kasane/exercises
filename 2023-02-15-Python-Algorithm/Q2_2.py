from queue import Queue

def solve(N, K):
    M = 100001
    times = [-1] * M

    qu = Queue()
    qu.put(N)

    times[N] = 0

    while not qu.empty():
        e = qu.get()

        if e == K:
            return times[K]
        
        if e < M - 1 and e >= 0 and times[e + 1] == -1:
            times[e + 1] = times[e] + 1
            if e + 1 == K:
                return times[e + 1] 
            qu.put(e + 1)
        if e < M and e > 0 and times[e - 1] == -1:
            times[e - 1] = times[e] + 1
            if e - 1 == K:
                return times[e - 1] 
            qu.put(e - 1)
        if e > 0 and 2 * e < M and times[2 * e] == -1:
            times[2 * e] = times[e] + 1
            if 2 * e == K:
                return times[2 * e] 
            qu.put(2 * e)
        
        qu.put(e)

    return times[K]

# if __name__ == "__main__":
#     N, K = map(int, input().strip().split())
#     print(solve(N, K))

assert(solve(5, 17) == 4)