# import sys

# res = sys.maxsize
 
# def calc(a, n, k, ind, sum, mxs):
#     global res
#     if k == 1:
#         mxs = max(mxs, sum)
#         sum = 0
#         for i in range(ind, n):
#             sum += a[i]
 
#         mxs = max(mxs, sum)
#         res = min(res, mxs)
#         return res

#     sum = 0
#     for i in range(ind, n):
#         sum += a[i]
#         mxs = max(mxs, sum)
         
#         calc(a, n, k - 1, i + 1, sum, mxs)

#     return res
     
# if __name__ == '__main__':
#     n, k = list(map(int, input().strip().split()))
#     arr = list(map(int, input().strip().split()))
#     print(calc(arr, n, k, 0, 0, 0))

import sys

if __name__ == '__main__':
    m, n, t = list(map(int, input().strip().split()))

    mat = [[-1] * (n + 2)] 
    for _ in range(m):
        mat += [[-1] + list(map(int, input().strip().split())) + [sys.maxsize]]
    mat += [[sys.maxsize] * (n + 2)] 
    mat[-1][0] = -1

    res = False
    for i in range(1, min(m + 2, n + 2)):
        if mat[i][i] < t:
            continue
        if mat[i][i] == t:
            res = True
            break
        tmp = i - 1
        for j in range(i, n + 2):
            if mat[tmp][j] >= t:
                if mat[tmp][j] == t:
                    res = True
                break
        for j in range(i, m + 2):
            if mat[j][tmp] >= t:
                if mat[tmp][j] == t:
                res = True
                break
    print("TRUE" if res else "FALSE")

        