# if __name__ == "__main__":
#     #arr = list(map(int, input().strip().split(',')))
#     arr = [100,180, 310, 40, 535, 695]
#     res = 0
#     last = arr[0]
#     cur = []
#     for i in arr[1:]:
#         if i <= last:
#             cur.append(i - last)
#         else:
#             res += sum(cur)
#             cur = []
#         last = i
#     res += sum(cur)
#     print(-res)

def dfs(mat, ms, st):
    total = 1
    ms.remove(st)

    if mat[st[0]][st[1] - 1]:
        mat[st[0]][st[1] - 1] = 0
        total += dfs(mat, ms, (st[0], st[1] - 1))
    if mat[st[0]][st[1] + 1]:
        mat[st[0]][st[1] + 1] = 0
        total += dfs(mat, ms, (st[0], st[1] + 1))
    if mat[st[0] - 1][st[1]]:
        mat[st[0] - 1][st[1]] = 0
        total += dfs(mat, ms, (st[0] - 1, st[1]))
    if mat[st[0] + 1][st[1]]:
        mat[st[0] + 1][st[1]] = 0
        total += dfs(mat, ms, (st[0] + 1, st[1]))
    return total

if __name__ == '__main__':
    n, m = list(map(int, input().strip().split(',')))

    ms = set()

    mat = [[0 for _ in range(m + 2)]]
    for i in range(1, n + 1):
        mat += [[0] + list(map(int, input().strip().split(','))) + [0]]
        for j in range(m + 2):
            if mat[i][j]:
                ms.add((i,j))
    mat += [[0 for _ in range(m + 2)]]

    maxi = 0
    while len(ms):
        start = ms.pop()
        ms.add(start)
        mat[start[0]][start[1]] = 0
        #print(dfs(mat, ms, start))
        maxi = max(maxi, dfs(mat, ms, start))

    print(maxi)