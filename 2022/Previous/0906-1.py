def try_min(e: int, m: int, a: int, last: int | None = None):
    if not last:
        return 0 if (e - a < 0) or (m - e <= a) else e - a
    if (last - e >= 0 and last - e <= a) or ((e + a > m) and (e + a - m >= last)):
        return 0
    return e - last

def verify(arr: list[int], m: int, a: int) -> bool:
    last = try_min(arr[0], m, a)
    for i in range(1, len(arr)):
        inc = try_min(arr[i], m, a, last)
        last += inc
        if last >= m or inc < 0:
            return False
    return True

def bisearch(arr: list[int], m: int) -> int:
    lf = 0
    rt = m
    mid = int((lf + rt) / 2)
    while rt > lf:
        if verify(arr, m, mid):
            rt = mid
        else:
            if lf == mid:
                return rt
            lf = mid
        mid = int((lf + rt) / 2)
    return rt

if __name__ == "__main__":
    m = 7
    arr = [0,6,1,3,2]

    print(bisearch(arr, m))
