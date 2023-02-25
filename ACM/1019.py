
A, B, C = 1, -1, 0

def func():

    def toint(s):
        if s[0] == "A":
            return A
        elif s[0] == "B":
            return B
        return C

    def flood(mat, ss):
        ind = 1
        total = 0
        last_qu = ss
        while len(last_qu):
            this_qu = []
            for e in last_qu:
                if mat[e[0] - 1][e[1]] == A:
                    total += ind
                    this_qu.append([e[0] - 1, e[1]]) # up
                    mat[e[0] - 1][e[1]] = B
                if mat[e[0] + 1][e[1]] == A:
                    total += ind
                    this_qu.append([e[0] + 1, e[1]]) # down
                    mat[e[0] + 1][e[1]] = B
                if mat[e[0]][e[1] - 1] == A:
                    total += ind
                    this_qu.append([e[0], e[1] - 1]) # left
                    mat[e[0]][e[1] - 1] = B
                if mat[e[0]][e[1] + 1] == A:
                    total += ind
                    this_qu.append([e[0], e[1] + 1]) # right
                    mat[e[0]][e[1] + 1] = B
            last_qu = this_qu
            ind += 1
        return total

    n = int(input())
    mat = [[B] * (n + 2)]
    ss = []
    for i in range(n):
        nxt = [B] + list(map(toint, input().strip().split())) + [B]
        for j in range(len(nxt)):
            if nxt[j] == C:
                ss.append([i + 1, j])
        mat += [nxt]
    mat += [[B] * (n + 2)]

    print(flood(mat, ss))


if __name__ == "__main__":
    func()