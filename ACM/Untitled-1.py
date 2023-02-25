# n m total test / total review
# pi
# ai

def solve(p: list, a: list, m: int) -> float:
    origin = [p[i] * a[i] for i in range(len(a))]

    values = [(1- p[i]) * a[i] for i in range(len(a))]
    values.sort()

    return sum(origin) + sum(values[-m:])


if __name__ == '__main__':
    n, m = input().strip().split(' ')
    p = input().strip().split(' ')
    a = input().strip().split(' ')
    assert((int(n) == len(p)) and (int(n) == len(a)) and (m <= n))
    
    res = solve([int(pi) / 100. for pi in p], [int(ai) for ai in a], int(m))

    print("%.2f" % res)