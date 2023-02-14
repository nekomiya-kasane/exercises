import math

if __name__ == "__main__":
    n = int(input())
    res = [0] * n
    for i in range(n):
        s = int(input())
        k = math.floor((-3 + math.sqrt(9 - 8 * (1 - s))) / 4)
        m = (1 + k) * (1 + 2 * k)
        if s - m < 2:
            res[i] = 0
        elif s - m - 1 <= k + 1:
            res[i] = s - m - 1
        elif s < (m + 4 + 3 * k):
            res[i] = k + 1 - (s - m - 2 - k)
        else:
            res[i] = -k - 1 + (s - m - 4 - 3 * k)

    for re in res:
        print(re)

