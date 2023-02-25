# def max_ascending(A):
#     dp = [1 for _ in A]
#     last = A[0]
#     max = 1
#     for i in range(1, len(A)):
#         dp[i] = dp[i - 1] + 1 if A[i] > last else 1
#         if dp[i] > max:
#             max = dp[i]        
#         last = A[i]

#     return max

def max_ascending(A):
    lf = 0
    rt = 1

if __name__ == "__main__":
    # n = int(input().strip())
    # arr = list(map(int, input().strip().split(' ')))

    n = 5
    arr = [3, 1, 2, 4, 6]

    print(max_ascending(arr))