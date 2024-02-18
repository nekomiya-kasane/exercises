def solve(arr):
    arr.sort(key=lambda x : (x[1], x[0]))
        
    cnt = 0
    end = -1
    for e in arr:
        if e[0] < end:
            continue
        cnt += 1
        end = e[1]

    return cnt

if __name__ == '__main__':
    N = int(input())
    print(solve([tuple(map(int, input().strip().split())) for _ in range(N)]))