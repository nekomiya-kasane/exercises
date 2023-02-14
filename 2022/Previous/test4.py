def total_time(arr):
    scanner = 0
    max = 999999999
    max_index = 0
    res = 0
    while len(arr) > 1:
        for scanner in range(len(arr) - 1):
            temp = sum(arr[scanner: scanner + 2])
            if temp < max:
                max = temp
                max_index = scanner
        res += max
        arr[max_index] = max
        del arr[max_index + 1]

        scanner = 0
        max_index = 0
        max = 9999999999

    return res
    

if __name__ == "__main__":
    #n = int(input())
    #liquids = [int(input()) for _ in range(n)]
    #assert(len(liquids) == n)

    liquids = [1,1,2,2,3,3,4,4]
    print(total_time(liquids))

# def count(mass):
#     res = mass
#     digits = []
#     while res > 0:
#         digits.append(res % 3)
#         res = int(res / 3)
#     for i in range(len(digits)):
#         if digits[i] > 1:
#             digits[i] -= 3
#             if i != len(digits) - 1:
#                 digits[i + 1] += 1
#             else:
#                 digits.append(1)
#     return len(digits) - digits.count(0)
    

# if __name__ == "__main__":
#     #mass = int(input())
#     mass = 8
#     print(count(mass))

# if __name__ == "__main__":
#     n = int(input().strip())
#     mat = []
#     for _ in range(n):
#         mat += list(map(int, input().strip().split(' ')))
#     print(sum(mat))