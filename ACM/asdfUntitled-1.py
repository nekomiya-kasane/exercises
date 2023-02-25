if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))

    cnt = int(m / 400)
    
    mi = 0
    mx = 0
    for e in arr:
        if e <= cnt:
            if e < cnt:
                mi += 1
            mx += 1

    print(n - mx, ' ', n - mi)


if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))

    arr.sort()
    n = len(arr)
    res = 0
    while k > 0:
        if len(arr) <= k:
            break
        res += arr[-1] - arr[0]
        del arr[0]
        del arr[len(arr) - 1]
        k -= 1
    print(res)