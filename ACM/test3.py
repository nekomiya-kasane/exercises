

# # def solution(S):
# #     n = len(S) >> 1
# #     max = 0

# #     def validate(B):
# #         dic = {}
# #         for c in B:
# #             if c in dic:
# #                 dic[c] += 1
# #             else:
# #                 dic[c] = 1
# #         for v in dic.values():
# #             if v % 2:
# #                 return False
# #         return True

# #     for i in range(1, n + 1):
# #         w = i * 2
# #         for j in range(len(S) - w + 1):
# #             if validate(S[j: j + w]):
# #                 max = w
# #                 break
# #     return max

# # if __name__ == "__main__":
# #     print(solution("zthtzh"))
# #     print(solution("abacb"))
# #     print(solution("bdaaadadb"))
# #     print(solution("abcdee"))

# # def insert(sorted_arr, ele):
# #     if (not len(sorted_arr)) or ele > sorted_arr[-1]:
# #         sorted_arr.append(ele)
# #         return
# #     if ele < sorted_arr[0]:
# #         sorted_arr.insert(0, ele)
# #         return

# #     lf = 0
# #     rt = n = len(sorted_arr) - 1
# #     mid = int((lf + rt) / 2)

# #     while rt - lf > 1:
# #         if ele > sorted_arr[mid]:
# #             lf = mid
# #             mid = int((lf + rt) / 2)
# #         elif ele < sorted_arr[mid]:
# #             rt = mid
# #             mid = int((lf + rt) / 2)
# #         else:
# #             break

# #     sorted_arr.insert(rt, ele)

# # def solution(A, B):
# #     assert(len(A) == len(B))
# #     arr = []
# #     for i in range(len(A)):
# #         a = A[i]
# #         b = B[i]
# #         if a == b:
# #             insert(arr, a)
# #             continue
# #         insert(arr, a if a > b else b)

# #     if arr[0] > 1:
# #         return 1
# #     for i in range(len(arr) - 1):
# #         if arr[i + 1] - arr[i] > 1:
# #             return arr[i] + 1
# #     return arr[-1] + 1

# # from bisect import bisect_left as bl

# # def solution(A, B):
# #     arr = []

# #     for i in range(len(A)):
# #         a = A[i]
# #         b = B[i]

# #         arr.insert(bl(arr, a), a if a > b else b)

# #     if arr[0] > 1:
# #         return 1
# #     for i in range(len(arr) - 1):
# #         if arr[i + 1] - arr[i] > 1:
# #             return arr[i] + 1
# #     return arr[-1] + 1


# # if __name__ == "__main__":
# #     print(solution([1, 2], [1, 2]))
# #     print(solution([1, 2, 4, 3], [1, 3, 2, 3]))
# #     print(solution([3, 2, 1, 6, 5], [4, 2, 1, 3, 3]))


# # def solution(A, B):
# #     C = [max(A[i], B[i]) for i in range(len(A))]
# #     C.sort()
# #     if C[0] > 1:
# #         return 1
# #     for i in range(len(C) - 1):
# #         if C[i + 1] - C[i] > 1:
# #             return C[i] + 1
# #     return C[-1] + 1

# # if __name__ == "__main__":
# #     print(solution([1, 2], [1, 2]))
# #     print(solution([1, 2, 4, 3], [1, 3, 2, 3]))
# #     print(solution([3, 2, 1, 6, 5], [4, 2, 1, 3, 3]))

# # def solution(A, M):
# #     pass


# def solution(array, m) :
#     modulos = {}
#     for element in array:
#         results = element % m
#         if results not in modulos:
#             modulos[results] = []
#         modulos[results].append(element)
#     results = map(lambda x: len(x), modulos.values())
#     return max(results)

#     # for nums in mods.values():
#     #     length = len(nums)
#     #     if length > max:
#     #         max = length

#     # return max

     
# if __name__ == '__main__':
#     arr = [-3, -2, 1, 0, 8, 7, 1]
#     m = 3
#     arr2 = [7, 1, 11, 8, 4, 10]
#     m2 = 8 
#     print(solution(arr, m))
#     print(solution(arr2, m2))


# # def solution(s):
# #     ind = {0: -1}
# #     mask = 0
# #     res = 0
# #     for i in range(len(s)):
# #         val = ord(s[i]) - ord('a') + 1
# #         mask ^= 1 << val
# #         if mask in ind:
# #             res = max(res, i - ind[mask])
# #         else:
# #             ind[mask] = i
# #     return res


# # if __name__ == "__main__":
# #     print(solution("cbdaaadadb"))
# #     print(solution("abacb"))
# #     print(solution("zthtzh"))
# #     print(solution("abcdee"))
