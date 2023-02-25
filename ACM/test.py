
def fill(matrix):
    m, n = len(matrix), len(matrix[0])
    total = [0]

    queue = []
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if matrix[i][j] == 1:
                queue.append([i,j])

    def enque(matrix, i, j, queue, total):
        if matrix[i][j] == 0 and (matrix[i - 1][j] != 1)and (matrix[i][j - 1] != 1) and (matrix[i + 1][j] != 1) and (matrix[i][j + 1] != 1):
            matrix[i][j] = 1
            queue.append([i, j])
            total[0] += 1
    
    while len(queue):
        next = queue[0]
        del queue[0]

        enque(matrix, next[0] - 1, next[1] - 1, queue, total)
        enque(matrix, next[0] + 1, next[1] - 1, queue, total)
        enque(matrix, next[0] - 1, next[1] + 1, queue, total)
        enque(matrix, next[0] + 1, next[1] + 1, queue, total)

    return total[0]


if __name__ == "__main__":
    m, n = list(map(int, input().strip().split()))
    matrix = [[-1 for _ in range(n + 2)]]
    matrix += [[-1] + list(map(int, input().strip().split())) + [-1] for _ in range(m)]
    matrix += [[-1 for _ in range(n + 2)]]

    # matrix = [[-1,-1,-1,-1,-1,-1,-1,-1],
    #     [-1,1,0,0,0,0,1,-1],
    #     [-1,0,0,0,0,0,0,-1],
    #     [-1,0,1,0,0,0,1,-1],
    #     [-1,0,0,0,0,0,0,-1],
    #     [-1,-1,-1,-1,-1,-1,-1,-1]]

    # print(fill(matrix))

    # matrix = [[-1,-1,-1,-1,-1,-1],[-1,1,0,0,0,-1], [-1,0,0,0,1,-1],[-1,-1,-1,-1,-1,-1]]

    print(fill(matrix))

def scan(arr, w, n, find_min = False):
    total = -2
    for i in range(len(arr) - w + 1):
        subarr = arr[i: i + w]
        tar = max(subarr)
        all = sum([tar - ele for ele in subarr])
        if all <= n:
            if not find_min:
                return -1
            if all < n:
                total = all
    if total == -2:
        return -2
    return w, n - total


def eval(arr, n):
    if len(arr) < 2:
        return len(arr), n
    arr.sort()
    last = -1
    for w in range(2, len(arr) + 1):
        if scan(arr, w, n, False) == -2:
            if last < 0:
                return 1, n
            return scan(arr, last, n, True)
        last = w
    return scan(arr, last, n, True)


if __name__ == "__main__":
    m = int(input())
    arr = [int(input()) for _ in range(m)]
    n = int(input())

    # m = 5
    # arr = [2, 9, 3, 1, 6]
    # n = 4

    # res = list(eval(arr, n))
    # print("{} {}".format(res[0], res[1]))

    # m = 3
    # arr = [5, 1, 20]
    # n = 2

    res = list(eval(arr, n))
    print("{} {}".format(res[0], res[1]))