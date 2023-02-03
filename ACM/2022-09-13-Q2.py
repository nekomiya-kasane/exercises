
# SA, SB, NON = 1, 2, 0

# def calc(A, B, this) -> int:
#     if (len(A) == 1):
#         return max(A[0] if this != SA else 0, B[0] if this != SB else 0)
#     if this == SA:
#         return A[0] + max(calc(A[1:], B[1:], SB), calc(A[1:], B[1:], NON))
#     elif this == SB:
#         return B[0] + max(calc(A[1:], B[1:], SA), calc(A[1:], B[1:], NON))
#     else:
#         return max(calc(A[1:], B[1:], SA), calc(A[1:], B[1:], SB))
    
    

# if __name__ == '__main__':
#     n = int(input())
#     A = list(reversed(list(map(int, input().strip().split(' ')))))
#     B = list(reversed(list(map(int, input().strip().split(' ')))))

#     res = max(calc(A, B, SA), calc(A, B, SB))
#     print(res)

# if __name__ == '__main__':
#     n = int(input())
#     A = list(map(int, input().strip().split(' ')))
#     B = list(map(int, input().strip().split(' ')))

#     for i in range(len(A) - 2):

if __name__ == "__main__":
    n, m, t = list(map(int, input().strip().split(' ')))
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))

    if A[0] > t:
        if B[0] > t:
            print(0)
            exit()
        C = A
        A = B
        B = C

    total = 0
    ai = 0
    bi = 0

    width = 1
    while ai < len(A):
        if (total + A[ai] > t):
            break
        total += A[ai]
        ai += 1
    while bi < len(B):
        if (total + B[bi] > t - total):
            break
        total += B[bi]
        bi += 1
    
    res = ai + bi

    t = t - total
    while ai > 0:
        t += A[ai - 1]
        total -= A[ai - 1]
        ai -= 1
        while bi < len(B):
            if (B[bi] > t):
                break
            total += B[bi]
            t -= B[bi]
            bi += 1
        res = max(res, ai + bi)
        if bi == len(B):
            break
        

    print(res)
    