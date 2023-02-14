
# # # import math

# # # if __name__ == "__main__":
# # #     # n, m, index = list(map(int, input().strip().split(' ')))

# # #     # rank = []
# # #     # for i in range(n):
# # #     #     rank.append([i] + [int(i) for i in list(map(int, input().strip().split(' ')))])
# # #     #mat = [[j] + [int(i) for i in list(map(int, input().strip().split(' ')))] for j in range(n)]

# # #     m = 3
# # #     n = 3
# # #     index = 2

# # #     rank = [[0, 80, 90, 100], [1, 80, 100, 90], [2, 80, 85, 85]]

# # #     bits = math.ceil(math.log2(m)) + 1

# # #     rank = sorted(rank, key=lambda x: (sum(x[1:m+1]) << bits) + n - x[0] - 1, reverse=True)

# # #     ans = 0
# # #     for i in range(n):
# # #         if rank[i][0] + 1 == index:
# # #             ans = i + 1
# # #             break
# # #     print(ans)




# # # # if __name__ == "__main__":
# # # #     mat = [[0 if i == '.' else 1 for i in input().strip()] for _ in range(3)]
# # # #     for i in range(len(mat)):
# # # #         for j in range(len(mat[0])):
# # # #             if mat[i][j]


# # if __name__ == "__main__":
# #     n, k = list(map(int, input().strip().split(' ')))

# #     arr = list(map(int, input().strip().split(' ')))

# #     #n, k = 3, 3
# #     #arr = [3, 2, 1]

# #     res = 0
# #     for i in range(len(arr)):
# #         for j in range(i + 1, len(arr)):
# #             if arr[i] * arr[j] >= k:
# #                 res += 2
# # # di
# #     print(res)

# # # import math

# # # def search_extend_path(l_node, tree, l_match, r_match, visited_set):
# # #     for r_node in tree[l_node]:
# # #         if r_node not in r_match.keys():
# # #             l_match[l_node] = r_node
# # #             r_match[r_node] = l_node
# # #             return True
# # #         else:
# # #             next_l_node = r_match[r_node]
# # #             if next_l_node not in visited_set:
# # #                 visited_set.add(next_l_node)
# # #                 if search_extend_path(next_l_node, tree, l_match, r_match, visited_set):
# # #                     l_match[l_node] = r_node
# # #                     r_match[r_node] = l_node
# # #                     return True
# # #                 return False

# # # def find_max_pairs(tree):
# # #     l_match, r_match = {}, {}
# # #     for i in tree.keys():
# # #         search_extend_path(i, tree, l_match, r_match, set())
# # #     return l_match

# # # if __name__ == "__main__":
# # #     # n = int(input())

# # #     # arr = list(map(int, input().strip().split(' ')))

# # #     n = 6
# # #     arr = [1,2,2,3,3]

# # #     tree = {}

# # #     for i in range(1, len(arr)):
# # #         if (arr[i - 1] - 1) not in tree:
# # #             tree[arr[i - 1] - 1] = [i]
# # #         else:
# # #             tree[arr[i - 1] - 1].append(i)

# # #     res = find_max_pairs(tree)
# # #     print(math.ceil(len(res) / 2))

# # def f(x, l):
# #     print(x[l - 1],end=" ")
# #     f(x, l - 1)
# # x=[11,12,13,14,15]
# # f(x,5)

# # def solution(L1):
# #     L2 = list(filter(lambda x: x>=100, L1))
# #     length = len(L2)
# #     L2.sort(reverse = True)
# #     maximum = max(L2)
# #     return (length, L2, maximum)

# # if __name__ == "__main__":
# #     print(solution([1,2,3,100,101]))

# def solution(A, B):
#     # C1 = [0 if i % 337 else (i / 337) for i in A]
#     # C2 = [0 if i % 337 else (i / 337) for i in B]
#     # res = 0
#     # for i in A:
#     #     for j in B:
#     #         a = i % 337
#     #         b = j % 337

#     #         if a and b:
#     #             continue

#     #         if not (a % 6) or not (b % 6) or (not (a % 2) and not (b % 3)) or (not (a % 3) and not (b % 2)):
#     #             res += 1

#     a2 = b2 = 0
#     a3 = b3 = 0
#     a6 = b6 = 0
#     a337 = b337 = 0
#     a337_2 = b337_2 = 0
#     a337_3 = b337_3 = 0
#     a337_6 = b337_6 = 0

#     def cnt(L):
#         v2 = v3 = v6 = v3_0 = v3_2 = v3_3 = v3_6 = 0
#         for a in L:
#             s1 = s2 = False
#             if not (a % 3):
#                 v3 += 1
#                 s1 = True
#             if ((a >> 1) << 1) == a:
#                 v2 += 1
#                 s2 = True
#             if not (a % 337):
#                 if s1 and s2:
#                     v3_6 += 1
#                 elif s1:
#                     v3_3 += 1
#                 elif s2: 
#                     v3_2 += 1
#                 else:
#                     v3_0 += 1
#             if s1 and s2:
#                 v6 += 1
#         return (v2, v3, v6, v3_0, v3_2, v3_3, v3_6)
        
#     a2, a3, a6, a337, a337_2, a337_3, a337_6 = cnt(A)
#     b2, b3, b6, b337, b337_2, b337_3, b337_6 = cnt(B)

#     res = a2 * b337_3 + a3 * b337_2 + a6 * b337 + b2 * a337_3 + b3 * a337_2 + b6 * a337 + len(A) * b337_6 + len(B) * a337_6
#     res = res - a337_3 * b337_2 - a337_2 * b337_3 - a337_6 * b337_6 - a337_3 * b337_6 - a337_2 * b337_6 - b337_3 * a337_6 - b337_2 * a337_6 
#     res = res - a337 * b337_6 - b337 * b337_6

#     return res

# # import math
# # def solution(A, B):
# #     a = len(A)
# #     b = len(B)
# #     if not a or not b:
# #         return 0
# #     if a == 1 and b == 1:
# #         if not (A[0] * B[0] % 2022):
# #             return 1
# #         else:
# #             return 0
# #     mid_a = math.ceil(a / 2.)
# #     mid_b = math.ceil(b / 2.)
# #     return solution(A[0: mid_a], B[0: mid_b]) + solution(A[mid_a: a], B[0: mid_b]) + solution(A[0: mid_a], B[mid_b: b]) + solution(A[mid_a: a], B[mid_b: b])

# if __name__ == "__main__":
#     A = [2022, 2, 337]
#     B = [1, 2022, 1, 674]

#     print(solution(A, B))

#from turtle import position
# import sys


# def detect_coll(pt1, pt2):
#     [x01, y01], [x02, y02] = pt1[0], pt1[2]
#     [x11, y11], [x12, y12] = pt2[0], pt2[2]
#     lx = abs((x01 + x02) / 2 - (x11 + x12) / 2)
#     ly = abs((y01 + y02) / 2 - (y11 + y12) / 2)
#     sax = abs(x01 - x02)
#     sbx = abs(x11 - x12)
#     say = abs(y01 - y02)
#     sby = abs(y11 - y12)
#     if lx <= (sax + sbx) / 2 and ly <= (say + sby) / 2:
#         return True
#     else:
#         return False

# if __name__ == "__main__":
#     #vs = list(map(float(input().strip().split(' '))))
#     vs = [  0, 0, 0, 3, 3, 3, 3, 0, 1, 1, 1, 2, 2, 2, 2, 1]

#     pt1 = [[vs[2 * i], vs[2 * i + 1]] for i in range(4)]
#     pt2 = [[vs[2 * i + 8], vs[2 * i + 9]] for i in range(4)]

#     res = detect_coll(pt1, pt2)

#     print('TRUE' if res else 'FALSE')

#     vs = [1,1,1,0,0,0,0,1,2,1,3,1,3,0,2,0]

#     pt1 = [[vs[2 * i], vs[2 * i + 1]] for i in range(4)]
#     pt2 = [[vs[2 * i + 8], vs[2 * i + 9]] for i in range(4)]

#     res = detect_coll(pt1, pt2)

#     print('TRUE' if res else 'FALSE')

# def main(lines):
#     #for i, v in enumerate(lines):
#         #positions = map(int, v.strip().split())
#         positions = [  0, 0, 0, 3, 3, 3, 3, 0, 1, 1, 1, 2, 2, 2, 2, 1]
#         ax1, ay1, bx1, by1, cx1, cy1, dx1, dy1, ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2 = positions
        
#         width1 = abs(cx1 - ax1)
#         height1 = abs(cy1 - ay1)

#         width2 = abs(cx2 - ax2)
#         height2 = abs(cy2 - ay2)

#         print(ax1 + width1 >= ax2 and  ax1 <= ax2 + width2 and ay1 + width1 >= ay2 and ay1 <= ay2 + width2)

#         if (abs(ax2 - ax1) < width1 / 2 + width2 / 2) and (abs(ay2 - ay1) < height1 / 2 + height2 / 2):
#             print('TRUE')
#         else:
#             print('FALSE')

# if __name__ == "__main__":
#     # lines = []
#     # for l in sys.stdin:
#     #     lines.append(l.rstrip('\r\n'))

#     # print(lines)
#     main(None)

# [  0, 0, 0, 3, 3, 3, 3, 0, 1, 1, 1, 2, 2, 2, 2, 1]

# import math,sys

# def main(lines):
#     for i, v in enumerate(lines):
#         w, h, b = list(map(int, v.strip().split(' ')))
#         #w, h, b = 50, 180, 20
#         bmi = 10000. * w / h / h
#         delta_bmi = bmi - b
#         delta_w = delta_bmi * h * h / 10000.
#         if delta_w < 0:
#             delta_w = 0
#         print(math.ceil(delta_w))

# if __name__ == "__main__":
#     lines = []
#     for l in sys.stdin:
#         lines.append(l.rstrip('\r\n'))

#     #print(lines)
#     main(lines)

# import math,sys

# def main(lines):
#     #for i, v in enumerate(lines):
#         #w, h, b = list(map(int, v.strip().split(' ')))
#         w, h, b = 50, 180, 20
#         bmi = 10000. * w / h / h
#         delta_bmi = bmi - b
#         delta_w = delta_bmi * h * h / 10000.
#         if delta_w < 0:
#             delta_w = 0
#         print(math.ceil(delta_w))

# if __name__ == "__main__":
#     lines = []
#     #for l in sys.stdin:
#     #    lines.append(l.rstrip('\r\n'))

#     #print(lines)
#     main(lines)

# from collections import defaultdict

# def build_tree(m, n):
#     dict = defaultdict(list)
#     for i in range(m):
#         for j in range(n):
#             if i == 0 and j == 0:
#                 dict[(i, j)].append((i + 1, j))
#                 dict[(i, j)].append((i, j + 1))
#             elif i == 0 and j == n - 1:
#                 dict[(i, j)].append((i + 1, j))
#                 dict[(i, j)].append((i, j - 1))
#             elif i == m - 1 and j == 0:

import sys

def build_mat(m, n):
    mat = [[0 for _ in range(n + 2)] for _ in range(m + 2)]
    for i in range(n + 2):
        mat[0][i] = mat[-1][i] = -1
    for i in range(m + 2):
        mat[i][0] = mat[i][-1] = -1
    return mat

def count(mat, start, visited, num_vert):
    x = start[0]
    y = start[1]
    if (mat[x][y] < 0):
        return 0
    res = 0
    mat[x][y] = 1 # visted 
    visited[0] += 1
    max_depth = True
    if not mat[x - 1][y]: # up
        max_depth = False
        res += count(mat, [x - 1, y], visited, num_vert)
    if not mat[x + 1][y]: # down
        max_depth = False
        res += count(mat, [x + 1, y], visited, num_vert)
    if not mat[x][y - 1]: # left
        max_depth = False
        res += count(mat, [x, y - 1], visited, num_vert)
    if not mat[x][y + 1]: # right
        max_depth = False
        res += count(mat, [x, y + 1], visited, num_vert)
    if max_depth:
        res = 0 if visited[0] < num_vert else 1
    mat[x][y] = 0
    visited[0] -= 1
    return res

if __name__ == "__main__":
    m, n = 2, 2
    mat = build_mat(m, n)
    res = 0 
    # for i in range(1, m + 1):
    #     for j in range(1, n + 1):
    #         matp = mat.copy()
    res += count(mat, [1, 1], [0], m * n)
    print(res)


def main(lines):
    for i, v in enumerate(lines):
        m, n = list(map(int, v.strip().split(' ')))
        mat = build_mat(m, n)
        res = count(mat, [1, 1], [0], m * n)
        print(res)


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
       lines.append(l.rstrip('\r\n'))
    main(lines)