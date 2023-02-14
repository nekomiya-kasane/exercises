

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))

    arr.sort()

    mi = 99999999999
    for i in range(m):
        if len(arr) < 2:
            print(0)
            exit(0)
        if arr[1] - arr[0] > arr[-1] - arr[-2]:
            

    print(mi)