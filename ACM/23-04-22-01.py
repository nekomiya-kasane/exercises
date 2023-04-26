





if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))
    ts = list(map(int, input().strip().split()))
    As = list(map(int, input().strip().split()))
    Bs = list(map(int, input().strip().split()))
    ws = [Bs[i] - As[i] for i in range(len(As))]

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j < ts[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - ts[i - 1]] + ws[i - 1])

    print(dp[-1][-1])