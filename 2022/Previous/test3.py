dic = {'.': 0, 'L': 1, 'R': 2, 'U': 3, 'D': 4, 'O': 5}
E, L, R, U, D, S, B = 5, 1, 2, 3, 4, 0, -1

def add_node(matrix, ex, bm, qu, dir):
    if ((matrix[ex[0]][ex[1]] == S) or (matrix[ex[0]][ex[1]] == dir)) and not bm[ex[0]][ex[1]]: 
        qu.append([ex[0], ex[1]])
        bm[ex[0]][ex[1]] = 1
        return True
    return False

def process(matrix, ex, bm, qu) -> bool:
    has_child = add_node(matrix, [ex[0] - 1,ex[1]], bm, qu, D)
    has_child = True if add_node(matrix, [ex[0] + 1, ex[1]], bm, qu, U) else has_child
    has_child = True if add_node(matrix, [ex[0], ex[1] - 1], bm, qu, R) else has_child
    has_child = True if add_node(matrix, [ex[0], ex[1] + 1], bm, qu, L) else has_child

def find_fail(matrix: list, m: int, n: int, ex: list):

    # init bit map
    bm = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        bm[-1][i] = bm[0][i] = -1
    for i in range(m):
        bm[i][0] = bm[i][-1] = -1

    bm[ex[0]][ex[1]] = 1

    qu = []

    add_node(matrix, [ex[0] - 1, ex[1]], bm, qu, D)
    add_node(matrix, [ex[0] + 1, ex[1]], bm, qu, U)
    add_node(matrix, [ex[0], ex[1] - 1], bm, qu, R)
    add_node(matrix, [ex[0], ex[1] + 1], bm, qu, L)

    while len(qu) > 0:
        ex = qu[0].copy()
        qu.pop(0)
        process(matrix, ex, bm, qu)

    res = 0
    for e in bm:
        for se in e:
            if not se:
                res = res + 1

    print(res)


if __name__ == '__main__':
    m, n = list(map(int, input().strip().split(' ')))

    matrix = []
    
    ex = [-1, -1]
    matrix.append([-1 for _ in range(n + 2)])
    for i in range(1, m + 1):
        matrix.append([-1] + [dic[c] for c in input().upper().strip()] + [-1])
        if E in matrix[-1]:
            ex = [i, matrix[-1].index(E)]
        assert(len(matrix[-1]) == n + 2)
    matrix.append([-1 for _ in range(n + 2)])

    find_fail(matrix, m + 2, n + 2, ex)
