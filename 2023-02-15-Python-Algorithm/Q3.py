from collections import defaultdict

def solve(arr: list[str]) -> bool:
    arr = sorted(arr)
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1][:len(arr[i])]:
            return False
    
    return True

if __name__ == "__main__":
    N = int(input())
    res = [False] * N
    for i in range(N):
        M = int(input())
        arr = [input().strip() for _ in range(M)]
        res[i] = solve(arr)
    
    for r in res:
        print("YES" if r else "NO")

