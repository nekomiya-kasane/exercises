from collections import defaultdict

def solve(N, K):
    if N >= K:
        return N - K
    
    dp = defaultdict(lambda x: 0)

    for i in range(K + 1):
        dp[i] = abs(i - N)
    
    for i in range(N + 1, K + 1):
        if i & 0b1: # odd
            dp[i] = min(dp[i], dp[(i-1) // 2] + 2)
            dp[i] = min(dp[i], dp[i - 1] + 1)
            dp[i] = min(dp[i], dp[(i + 1) // 2] + 2)
        else: # even
            dp[i] = min(dp[i], dp[(i-1) // 2] + 2)
            dp[i] = min(dp[i], dp[i - 1] + 1)
            dp[i] = min(dp[i], dp[(i + 1) // 2] + 2)

    return dp[K]

if __name__ == "__main__":
    N, K = map(int, input().strip().split())
    print(solve(N, K))

# assert(solve(5, 17) == 4)