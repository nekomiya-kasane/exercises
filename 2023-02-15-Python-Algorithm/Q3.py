from collections import defaultdict

def solve(arr: list[str]) -> bool:
    tree = defaultdict(dict)
    tree[0] = {}
    pool = 1
    for s in arr:
        id = 0
        for c in s:
            if id and '\0' in tree[id]:
                return False
            if c in tree[id]:
                id = tree[id][c]
            else:
                tree[id][c] = pool
                id = pool
                pool = pool + 1
        if '\0' in tree[id]:
            return False
        tree[id]['\0'] = pool
        pool = pool + 1
    
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

