# import math

# # def is_even(n):
# #     return not (n % 2)

# if __name__ == "__main__":
#     k = int(input())
#     res = []
#     for _ in range(k):
#         n = int(input())
#         start = math.ceil(math.sqrt(n))
#         if start * start == n:
#             start += 1
#         while n % start:
#             start += 1
#         res.append(start)
#     for e in res:
#         print(e)

# import math

# def fill_dp(m):
#     dp = [-1 for _ in range(m + 1)]
#     dp[0] = dp[1] = 0
#     dp[2] = 1
#     for i in range(3, m + 1):
#         mi = dp[i - 1] + 1
#         for j in range(2, int(math.sqrt(i)) + 1):
#             if i % j: # not factor
#                 continue
#             tmp = dp[j] + dp[int(i / j)] + 1
#             if tmp < mi:
#                 mi = tmp
#         dp[i] = mi
#     return dp

# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int, input().strip().split(' ')))

#     # n = 2
#     # arr = [2, 6]
    
#     dp = fill_dp(max(arr))

#     # dp = fill_dp(10)
    
#     res = 0
#     for e in arr:
#         res += dp[e]
    
#     print(res)


# def find_len(s):
#     lf = rt = 0
#     for c in s:
#         if c == '(':
#             lf += 1
#         elif lf > 0:
#             lf -= 1
#             rt += 1
#     # print(rt * 2)
#     return rt * 2

# def calc(s):
#     res = 0
#     for i in range(len(s) - 2):
#         for j in range(i + 2, len(s) + 1):
#             res += find_len(s[i: j])
#     return res

# if __name__ == "__main__":
#     s = input().strip()
#     print(find_len(s))

    #print(calc('())())'))

# def fill(s):
#     mt = []

#     ht = 0
#     mxht = 0
#     st = end = -1
#     ind = 0
#     cnt = 0
#     for c in s:
#         if c == '(':
#             if not ht:
#                 st = ind
#             ht += 1
#         elif ht > 0:
#             mxht = max(mxht, ht)
#             ht -= 1
#             if not ht:
#                 end = ind
#         cnt += 1
#         if not ht and st > -1: # fumoto
#             if len(mt):
#                 mt[-1][4] = cnt
#             mt.append([st, end, mxht, cnt, 0])
#             st = end = -1
#             mxht = cnt = 0
#         ind += 1
#     if cnt:
#         mt[-1][4] = cnt
    
#     mt.insert(0, [0, 0, 0, 0, mt[0][0]])
#     mt.append([len(s), len(s), 0, len(s) - mt[-1][1] - 1, 0])

#     total = 0
#     for step in range(1, len(mt) - 1):
#         for i in range(1, len(mt) - step):
#             ht = 0
#             for k in range(i, i + step + 1):
#                 ht += mt[k][2]
#             total += ht * (mt[i][-2] + 1) * (mt[i + step][-1] + 1)

#     for m in mt:
#         total += m[2] * m[-1] * m[-2]

#     return total
    
    # res = 0
    # if len(mt) == 1:
    #     res = 2 ** (mt[0][0] + len(s) - mt[0][1] - 1)
    # else:
    #     for step in range(1, len(mt) + 1):
    #         for i in range(len(mt) - step + 1):
    #             if not i and (i == len(mt) - step):
    #                 res += (len(s) - mt[i][1] - 1) 
    #             elif not i: # first one
    #                 res += (mt[i][0] * (mt[i + step][0] - mt[i][1] - 1) + 1) * mt[i][2] * 2
    #             elif i == len(mt) - step:
    #                 res += ((mt[i][0] - mt[i - step][1] - 1) * (len(s) - mt[i][1] - 1) + 1) * mt[i][2] * 2
    #             else:
    #                 res += ((mt[i][0] - mt[i - step][1] - 1) * (mt[i + step][0] - mt[i][1] - 1) + 1) * mt[i][2] * 2
    

# if __name__ == "__main__":
#     print(fill('())())'))
    
import bisect

def mxcnt(arr, k):
    _sum = 0
    cnt = 0
    maxcnt = 0
     
    for i in range(len(arr)):
        if (_sum + arr[i]) <= k:
            _sum += arr[i]
            cnt += 1
        elif sum != 0:
            _sum = _sum - arr[i - cnt] + arr[i]
        maxcnt = max(cnt, maxcnt)
    return maxcnt

if __name__ == "__main__":
    n, k = list(map(int, input().strip().split(' ')))
    arr = list(map(int, input().strip().split(' ')))

    pp = [[ e / i / k for e in arr ] for i in range(1, len(arr) + 1)]
    tar = [mxcnt( 1)]
  
    a = [1, 3, 2, 5, 4] 
    n = len(a)

    q = [4, 2, 1, 5] 
    m = len(q)
 
    longestSubsequence(a, n, q, m)