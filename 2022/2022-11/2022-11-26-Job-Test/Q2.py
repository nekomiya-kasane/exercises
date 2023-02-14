

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if len(a) < len(b):
        tmp = a
        a = b
        b = tmp

    k = -1
    N = len(a)
    tmp = [-1] * (N + 1)
    next = 0

    for i in range(1, N + 1):
        tmp[k] = a[k] + (b[k] if i <= len(b) else 0) + next
        next = tmp[k] // (i + 1)
        if next:
            tmp[k] = tmp[k] % (i + 1)
        k -= 1

    if next:
        tmp[k] = next
    else:
        del tmp[k]
    
    print(' '.join(map(str,tmp)))