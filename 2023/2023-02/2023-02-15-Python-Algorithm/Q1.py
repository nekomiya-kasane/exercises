def solve(N: int) -> int:
    r = N % 5
    if r == 0:
        return N // 5
    elif r == 1:
        return -1 if N < 6 else (N - 6) // 5 + 2
    elif r == 2:
        return -1 if N < 12 else (N - 12) // 5 + 4
    elif r == 3:
        return N // 5 + 1
    else: # r == 4
        return -1 if N < 9 else (N - 9) // 5 + 3

if __name__ == "__main__":
    N = int(input())
    print(solve(N))

# assert(solve(18) == 4)
# assert(solve(4) == -1)
# assert(solve(6) == 2)
# assert(solve(9) == 3)
# assert(solve(11) == 3)