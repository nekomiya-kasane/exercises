import copy, sys
from queue import Queue


def advance(lst, k, v, b):
    lst[0][k] = b
    lst[1].remove(b)
    lst[1].add(v)


def get_possible_moves(lst):
    for k, v in lst[0].items():
        if v + 1 in lst[1]:
            temp = copy.deepcopy(lst)
            advance(temp, k, v, v + 1)
            yield ((v, v +1 ), temp)
        elif v + 1 not in lst[1] and v+2 in lst[1]:
            temp = copy.deepcopy(lst)
            advance(temp, k, v, v + 2)
            yield ((v, v + 2), temp)
        elif v - 1 in lst[1]:
            temp = copy.deepcopy(lst)
            advance(temp, k, v, v - 1)
            yield ((v, v - 1), temp)
        elif v - 1 not in lst[1] and v - 2 in lst[1]:
            temp = copy.deepcopy(lst)
            advance(temp, k, v, v - 2)
            yield ((v, v - 2), temp)


def solve_distinct_disks(length, n):
    if n == 0:
        return [None]
    if length <= n or length <= 0 or n < 0:
        return None
    
    st = ({i: i for i in range(n)}, set(i for i in range(n, length)))
    goal = ({length - i - 1: i for i in range(length - n, length)}, 
                 set(i for i in range(length - n)))
    
    heads = set([(k, v) for k, v in st[0].items()])

    queue = Queue()
    queue.put(([], st))
    while not queue.empty():
        next = queue.get()
        for move, newState in get_possible_moves(next[1]):
            newHead = tuple(newState[0].items())
            if newHead not in heads:
                newMoves = next[0] + [move]
                if newState == goal:
                    return newMoves
                heads.add(newHead)
                queue.put((newMoves, newState))
    return None

def test_solve_distinct_disks():
    def test(length, n, expected):
        sol = solve_distinct_disks(length, n)
        print("\nLength: {}  N: {}  Result: {}  Expected: {}".format(
            length, n, (-1 if not sol else 0 if not sol[0] else len(sol)), expected
        ))
        print(sol)
        assert((-1 if not sol else (0 if not sol[0] else len(sol))) == expected)

    test(4, 2, 3)
    test(5, 2, 3)
    test(4, 3, 6)
    test(5, 3, 5)
    test(0, 0, 0)
    test(5, 5, -1)
    test(5, 0, 0)
    test(8, 7, 28)
    test(10, 5, 15)
    test(9, 6, 23)
    test(11, 4, 18)
    test(7, 8, -1)
    test(16, 8, 36)
    test(18, 6, 39)

test_solve_distinct_disks()