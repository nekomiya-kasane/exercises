import math
# # def find_num_tri(arr: list):
# #     if len(arr) < 3:
# #         return 0

# #     total = 0
# #     for i in range(len(arr) - 2):
# #         cur = 0
# #         for j in range(i + 1, len(arr)):
# #             if arr[i] == arr[j]:
# #                 total = total + cur
# #             if arr[j] < arr[i]:
# #                 cur = cur + 1
    
# #     return total


# # if __name__ == '__main__':
# #     n = int(input().strip())
# #     arr = list(map(int, input().strip().split()))

# #     res = find_num_tri(arr)
    
# #     print(res)

# # def modify_count(s: str):
# #     def continous_e(s: str):
# #         res = []
# #         pairs = []
# #         for i in range(len(s)):
# #             if s[i] != 'e':
# #                 continue
# #             for j in range(i + 1, len(s)):
# #                 if j != 'e':
# #                     res.append(j - i)
# #                     pairs.append([i - 1, j])
# #                     break
# #         return res, pairs

# #     strips, pairs = continous_e(s)

# #     boundary = []
# #     for i in range(len(pairs) - 1):
# #         cur = [pairs[i][0], pairs[i][1]]
# #         end = pairs[i][1]
# #         for j in range(i + 1, len(pairs)):
# #             if pairs[j][0] == end:
# #                 cur.append(pairs[j][1])
# #             else:
# #                 break
# #         boundary.append(cur)
    
# #     total = 0
# #     cur = 0
# #     for i in range(len(boundary)):
# #         k = len(boundary[i]) - 1
# #         for j in range(k):
# #             c = strips[cur]
# #             if c % 2 == 0:
# #                 total = total + c / 2
# #             else:

# def modify_count(s: str):
#     if len(s) % 2: # odd
#         res = 0
#         n = int((len(s) - 1) / 2)
#         for i in range(n):
#             if s[2 * i + 1] != 'e':
#                 res = res + 1
#         rc = 0
#         dc = 0
#         for i in range(n + 1):
#             c = s[2 * i]
#             if c == 'r':
#                 rc = rc + 1
#             elif c == 'd':
#                 dc = dc + 1
#             else:
#                 res = res + 1
#         res = res + int((max(rc, dc) - min(rc, dc)) / 2)
#         return res
#     else:
#         n = int(len(s) / 2)

#         count = [0, 0, 0, 0, 0, 0]





#         return min(res2, res1) - 1


# if __name__ == '__main__':
#     i = input().strip()
    
#     res = modify_count(i)

#     print(res)


# n = int(input().strip())
# a = list(map(int,input().strip().split(' ')))

# mx1 = 0
# mx2 = 0

# for i in range(n):
#     if i % 2 == 0:
#         mx1 = max(mx1, a[i])
#     else:
#         mx2 = max(mx2, a[i])

# ans = 0
# for i in range(n):
#     if i % 2 == 0:
#         ans = ans + mx1 - a[i]
#     else:
#         ans = ans + mx2 - a[i]
    
# if (n >= 2) and (mx1 == mx2):
#     ans = ans + int(n / 2) - (n % 2)

# print(ans)


# if __name__ == '__main__':
#     a, b, n = list(map(int,(input().strip().split(' '))))

#     lf, rt = [a, b]
#     for i in range(n - 2):
#         temp = lf * rt
#         lf = rt
#         rt = (temp * temp) % (10 ** 9 + 7)
    
#     print(rt)

# def resolve(a):
#     res = 0
#     if len(a) == 1:
#         return a, 0

#     if len(a) == 2:
#         if a[0] > a[1]:
#             res = int((a[0] - a[1]) / 2) + 1
#         a[0] = a[0] - res
#         a[1] = a[1] + res
#         return a, res

#     mid = int(len(a) / 2)
#     a[0 : mid], l = resolve(a[0 : mid])
#     a[mid : len(a)], r = resolve(a[mid : len(a)])
#     res = res + l + r

#     if a[mid - 1]     return a, res
    


# if __name__ == '__main__':
#     n = int(input().strip())
#     a = list(map(int,(input().strip().split(' '))))

#     temp = -1
#     res = 0
#     while temp != 0:
#         a, temp = to_subarr(a)
#         res = res + temp

#     print(res)

if __name__ == '__main__':
    res = []
    for i in range(1, 51):
        n = 2 * i
        ind = False
        for j in range(1, math.floor(math.sqrt(n)) + 1):
            if j > math.sqrt(n):
                break
            if (n % j == 0) and (int(n / j) % 2 == 0) and (j % 2 == 0) and (j * j != n):
                if ind:
                    ind = False
                    break
                ind = True
        if ind:
            res.append(n)
    print(res)