# from pkg_resources import find_distributions

import time

# def solve(s, k):
#     mxs = []
#     pairs = {}

#     def find_min_and_insert(mxs, c, k):
#         if not len(mxs) or ord(c) < mxs[0]:
#             mxs.insert(0, ord(c) - min(k, ord(s[0]) - ord('a')))
#             return min(k, ord(s[0]) - ord('a'))
#         for i in range(1, len(mxs) - 1):
#             if ord(c) < mxs[i + 1] and ord(c) > mxs[i]:
#                 mxs.insert(i + 1, ord(c) - min(k, ord(s[0]) - mxs[i]))
#                 return min(k, ord(s[0]) - mxs[i])
#             elif ord(c) == mxs[i]:
#                 return 0
#         mxs.append(ord(c) - min(k, ord(s[0]) - mxs[-1]))
#         return min(k, ord(s[0]) - mxs[-1])

#     ind = 0
#     while k >= 0 and ind < len(s):
#         diff = find_min_and_insert(mxs, s[ind], k)
#         k -= diff
#         pairs[s[ind]] = chr(ord(s[ind]) - diff)
#         ind += 1

#     # replace
#     pairs = {k: v for k, v in sorted(pairs.items(), key=lambda item: item[1], reverse=True)}
#     for k, v in pairs.items():
#         s.replace(k, v)
    
#     return s

# def found(x, p):
#     if p[x] != x :
#         p[x] = found(p[x], p)
#     return p[x]

# def get_ind(c):
#     return ord(c) - ord('a') + 1

# def solve(s, k):
#     p = [chr(i + ord('a')) for i in range(26)]

#     i = 1
#     s = 'a' + s
#     mx = ord('a')
#     while i <= len(s) - 1 and k > 0:
#         if ord(s[i]) > mx:
#             if ord(s[i]) - mx <= k:
#                 k-= ord(s[i]) - mx
#                 for j in reversed(range(0, ord(s[i]) - ord('a') + 1)):
#                     p[j] = 'a'
#             else:
#                 for j in reversed(range(ord(s[i]) - k - ord('a'), ord(s[i]) - ord('a') + 1)):
#                     p[j] = chr(ord(s[i]) - k)
#                 k = 0
#             mx = ord(s[i])
#         i += 1
#     res = ""
#     for a in s:
#         res += p[ord(a) - ord('a')]
#     return res[1:]

# if __name__ == "__main__":
#     n = int(input().strip())
#     for _ in range(n):
#         l, k = list(map(int, input().strip().split(' ')))
#         s = input().strip()
#         print(solve(s, k))

#     print(solve("cba", 2))
#     print(solve("fgde", 5))
#     print(solve("gndcafb", 5))
#     print(solve("ekyv", 19))

def solve(arr): 
    res = {}

    for i in range(len(arr)):
        visited = set()
        cnt = 0
        ind = i
        over = False
        last = 0
        while ind >= 0 and ind < len(arr):
            ind += arr[ind][0] * arr[ind][1]
            cnt += 1
            visited.add(ind)
            if len(visited) == last:
                if not over:
                    over = True
                else:
                    res[i] = -1
                    break
            last = len(visited)
        if not over:
            res[i] = cnt
    return res.values()

def solve2(arr):
    visited = [0 for _ in range(len(arr))]

    for i in range(len(arr)):
        if visited[i]:
            continue
        visited[i] = -1
        tmp = [i]
        i += arr[i][0] * arr[i][1] # next
        base = 0
        while i >= 0 and i < len(arr):
            if visited[i]:
                base = visited[i]
                break
            visited[i] = -1
            tmp.append(i)
            i += arr[i][0] * arr[i][1] # next
        offset = 1
        for e in reversed(tmp):
            visited[e] = -1 if base < 0 else base + offset
            offset += 1
    return visited
        

if __name__ == "__main__":
    # n = int(input())
    # arr = []
    # for _ in range(n):
    #     m = int(input())
    #     tmp = []
    #     for _ in range(m):
    #         e = input().strip().split(' ')
    #         tmp.append([-1 if e[0] == 'L' else 1, int(e[1])])
    #     arr.append(tmp)

    arr = [
        # [[-1, 1], [-1, 1], [1, 1]],
        # [[1, 1], [-1, 1], [-1, 1], [1, 100]],
        # [[1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [1, 2], [-1, 1], [-1, 1]],
        [[1, 1], [1, 1], [1, 2], [-1, 1], [1, 2], [1, 2], [-1, 1], [1, 1]] 
        for _ in range(10000)
    ]

    for f in [solve, solve2]:
        s = time.time()
        for e in arr:
            t = f(e)
            pr = ""
            for i in t:
                pr += str(i) + " "
            pr = pr[:-1]
        e = time.time()
        print(e - s)