# def findPasswordStrength(password):
#     vowels = ['a', 'e', 'i', 'o', 'u']

#     ptr = 1
#     v = password[0] in vowels
#     c = not v
#     res = 0

#     while ptr != len(password):
#         is_vowel = password[ptr] in vowels
#         if (v and not is_vowel) or (c and is_vowel):
#             v = c = False
#             res = res + 1
#         elif not (v or c):
#             v = is_vowel
#             c = not v
#         ptr = ptr + 1
    
#     return res

# def predictDays(days, k):
#     if len(days) < 2 * k + 1:
#         print([])
#         return []

#     acending = []
#     decending = []

#     def transverse(days, reversed):
#         out = []
#         if not len(days):
#             return 

#         count = 0
#         last = days[0] if not reversed else days[-1]
#         out = [0]

#         n = len(days)
#         for i in (range(n - 2, -1, -1) if reversed else range(1, n)):
#             count = count + 1 if days[i] <= last else 0
#             last = days[i]
#             out.append(count if count else out[-1])
#         return out

#     decending = transverse(days, False)
#     acending = transverse(days, True)

#     n = len(days)
#     res = []
#     for i in range(k, n - k):
#         if (decending[i] >= k) and (acending[n - i - 1] >= k):
#             res.append(i + 1)

#     print(res)
#     return res

# if __name__ == '__main__':
#     # res = findPasswordStrength('hackerrank')
#     # print(res)
#     # res = findPasswordStrength('thisisbeautiful')
#     # print(res)
#     # res = findPasswordStrength('rhythm')
#     # print(res)
#     predictDays([1,1,1,1,1,1,1], 2)
#     predictDays([3,2,1,1,1,5,6,2,1,0,0,-1,1,0,1], 3)
#     predictDays([3,2,1,1,1,5,6,2,1,0,0,-1,1,0,1], 2)
#     predictDays([1,0,1,0,1], 1)


# if __name__ == "__main__":
#     s = input()
#     arr = s.split('0')

#     print(arr)

# import sys

# if __name__ == "__main__":
#     n = input()
#     s = input()

#     cnts = [sys.maxsize, 0, 0, 0, 0]

#     dic = {'p': 1, 'o': 2, 'n': 3, 'y': 4 }

#     for c in s:
#         cnts[dic[c]] = min(cnts[dic[c] - 1], cnts[dic[c]] + 1)

#     print(min(cnts))

# def findminind(arr):
#     ind = 0
#     mi = arr[0]
#     for i in range(len(arr)):
#         if arr[i] < mi:
#             mi = arr[i]
#             ind = i
#     return ind

# def findmin(arr, k, base):
#     if k < len(arr):
#         return -1
#     if k == len(arr):
#         return min(arr) - base
#     miind = findminind(arr)
#     lf = findmin(arr[:miind])
#     rt = findmin(arr[miind + 1:])
#     if lf == -1 and rt == -1:
#         return arr[miind] - base + 1
    
def find_min(arr):
    min_ind = 0
    mi = arr[0]
    for i in range(len(arr)):
        if arr[i] <= mi:
            mi = arr[i]
            min_ind = i
    return min_ind, mi

def find_max_ops(arr, k):
    ind = 0
    total = 0

    if len(arr) < k:
        return 0
    if len(arr) == k:
        return min(arr)

    while ind <= len(arr) - k:
        min_ind, mi = find_min(arr[ind: ind + k])
        min_ind += ind
        total += mi

        for i in range(min_ind + 1, ind + k):
            arr[i] -= mi

        ind = min_ind + 1
        
    return total


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    ind = 0
    sps = []
    tmp = []
    while True:
        if arr[ind] == 0:
            if len(tmp):
                sps.append(tmp)
            tmp = []
        else:
            tmp.append(arr[ind])
        ind += 1
        if ind >= len(arr):
            if len(tmp):
                sps.append(tmp)
            break
    
    sm = 0
    for e in sps:
        sm += find_max_ops(e, m)

    print(sum(arr) - sm * m)

