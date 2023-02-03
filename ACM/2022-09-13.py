# # # from collections import defaultdict

# # # vow = ['a', 'e', 'i', 'o', 'u']

# # # # def init(s, dic):
# # # #     for i in range(5):
# # # #         dic[s[i]] += 1

# # # # def check(dic):
# # # #     for _, v in dic.items():
# # # #         if v > 1:
# # # #             return False
# # # #     return True

# # # if __name__ == "__main__":
# # #     #
# # #     s = input().strip()

# # #     #s = "baiduoxiaojiabankanjiaran"

# # #     if len(s) < 5:
# # #         print(0)
# # #         exit()
# # #     dic = defaultdict(int)
# # #     lf = 0
# # #     rt = 4
# # #     res = 0
# # #     #init(s, dic)
# # #     while True:
# # #         if (s[lf] != s[lf + 3]) and (s[lf + 1] != s[lf + 2]) and (s[lf + 1] != s[rt]) \
# # #             and (s[rt] != s[lf + 2]) and \
# # #             (s[lf] not in vow) and (s[lf + 3] not in vow) and \
# # #             (s[lf + 1] in vow) and (s[lf + 2] in vow) and (s[rt] in vow):
# # #             res += 1
# # #         lf += 1
# # #         rt += 1
# # #         if rt >= len(s):
# # #             break
# # #     print(res)

# if __name__ == "__main__":
#     size = int(input())

#     #size = 3
#     #ss = ["101", "1111", "1011"]
    
#     res = [False] * size
#     for i in range(size):
#         s = input().strip()
#         #s = ss[i]
#         m = s.count('0')
#         n = s.count('1')
#         if (not n) or (not m) or (m % 2 == 0) or (n % 2 == 0):
#             res[i] = True
#     for e in res:
#         print("Yes" if e else "No")

# # MASK_VOW = 1 | (1 << (ord('e') - ord('a') + 1)) | (1 << (ord('i') - ord('a') + 1))\
# #     | (1 << (ord('e') - ord('a') + 1)) | (1 << (ord('i') - ord('a') + 1))

R, E, D = 2, 3, 4

def toint(c) -> int:
    if c == 'r':
        return R # for transversed afterwards
    if c == 'e':
        return E
    if c == 'd':
        return D
    return -1

def least_time(mat, st, last: int):
    if (mat[st[0]][st[1]] == D and last == R) \
        or (mat[st[0]][st[1]] == R and last == E) \
        or (mat[st[0]][st[1]] == E and last == D) \
        or (mat[st[0]][st[1]] < 0) \
        or (mat[st[0]][st[1]] == 1):
        return -1
    elif (st[0] == len(mat) - 2) and (st[1] == len(mat[1]) - 2):
        return 0

    this = mat[st[0]][st[1]]
    mat[st[0]][st[1]] = 1

    cnt = 999999999
    tmp = least_time(mat, (st[0] - 1, st[1]), this)
    if tmp != -1:
        cnt = min(cnt, tmp + 1)

    tmp = least_time(mat, (st[0] + 1, st[1]), this)
    if tmp != -1:
        cnt = min(cnt, tmp + 1)   

    tmp = least_time(mat, (st[0], st[1] - 1), this)
    if tmp != -1:
        cnt = min(cnt, tmp + 1)

    tmp = least_time(mat, (st[0], st[1] + 1), this)
    if tmp != -1:
        cnt = min(cnt, tmp + 1)   
        
    if cnt == 999999999:
        cnt = -1

    mat[st[0]][st[1]] = this
    return cnt


if __name__ == '__main__':
    m, n = list(map(int, input().strip().split(' ')))
    m += 2
    n += 2

    mat = [[-1 for _ in range(n)]]
    for i in range(1, m - 1):
        mat.append([-1] + list(map(toint, input().strip())) + [-1])
    mat += [[-1 for _ in range(n)]]

    time = least_time(mat, (1, 1), mat[1][1])  # type: ignore
    print(time)

# vow = ['a', 'e', 'i', 'o', 'u']

# if __name__ == "__main__":
#     s = input().strip()
#     #s = "baiduoxiaojiabankanjiaran"

#     def check(s):
#         if (s[0] not in vow) \
#             and (s[1] in vow) \
#             and (s[2] in vow) \
#             and (s[3] not in vow) \
#             and (s[4] in vow) \
#             and (s[0] != s[3]) \
#             and (s[1] != s[2]) \
#             and (s[2] != s[4]) \
#             and (s[1] != s[4]):
#             return True
#         return False

#     res = 0
#     for i in range(len(s) - 5):
#         if check(s[i: i + 5]):
#             res += 1
#     print(res)