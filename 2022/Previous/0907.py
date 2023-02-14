# def solution(S):

#     def get_dec(arr, reverse = False):
#         cnt = 0
#         res = [0]
#         last = arr[-1] if reverse else arr[0]
#         fst = True
#         for i in (reversed(arr) if reverse else arr):
#             if fst:
#                 fst = False
#                 continue
#             if i <= last:
#                 cnt += 1
#             else:
#                 cnt = 0
#             last = i
#             res.append(cnt)
#         return res

#     lf_dec = get_dec(S)
#     rt_dec = get_dec(S, reverse=True)

#     mx = lf_dec[0] + rt_dec[-1]
#     for i in range(1, len(S)):
#         mx = max(mx, lf_dec[i] + rt_dec[-(i + 1)])

#     return mx + 1


# print(solution([2,6,8,5]))
# print(solution([1,5,5,2,4]))
# print(solution([1,1]))

from collections import defaultdict

def solution(S):
    dic = defaultdict(int)
    cnt = 0
    for c in S:
        if dic[c] > 0:
            cnt += 1
            dic = defaultdict(int)
        dic[c] += 1
    return cnt + 1

print(solution('world'))
print(solution('dddd'))
print(solution('cycle'))
print(solution('abba'))
