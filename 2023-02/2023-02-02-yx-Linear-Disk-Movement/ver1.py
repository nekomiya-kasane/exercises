import math, copy
from queue import PriorityQueue

def solve_distinct_disks(length, n):
    if n == 0:
        return [None]
    if n >= length:
        return None

    def is_solved(state):
        for i in range(len(state)):
            if state[i] != length - i - 1:
                return False
        return True

    state = [i for i in range(n)]
    qu = PriorityQueue()
    qu.put((heuristic(state, length), state, []))

    while not qu.empty():
        _, s, m = qu.get()
        if is_solved(s):
            return m
        nexts = get_possible_moves(s, m, length)
        for _s, _m in nexts:
            qu.put((len(_m) + heuristic(_s, length), _s, _m))

    return [None]
                    
def get_possible_moves(state, move, length):
    res = []

    for i in range(len(state)):
        if (state[i] < length - 1):
            mid = state[i] + 1 in state
            if (state[i] < length - 2) and (state[i] + 2 not in state) and mid:
                next_move = (state[i], state[i] + 2)
                if not len(move) or (next_move[0] != move[-1][1] or next_move[1] != move[-1][0]):
                    new_moves = copy.deepcopy(move)
                    new_moves.append(next_move)
                    new = copy.deepcopy(state)
                    new[i] += 2
                    res.append((new, new_moves))
            if not mid:
                next_move = (state[i], state[i] + 1)
                if not len(move) or (next_move[0] != move[-1][1] or next_move[1] != move[-1][0]):
                    new_moves = copy.deepcopy(move)
                    new_moves.append(next_move)
                    new = copy.deepcopy(state)
                    new[i] += 1
                    res.append((new, new_moves))
        
        if state[i] >= 1:
            mid = state[i] - 1 in state
            if (state[i] >= 2) and (state[i] - 2 not in state) and mid:
                next_move = (state[i], state[i] - 2)
                if not len(move) or (next_move[0] != move[-1][1] or next_move[1] != move[-1][0]):
                    new_moves = copy.deepcopy(move)
                    new_moves.append(next_move)
                    new = copy.deepcopy(state)
                    new[i] -= 2
                    res.append((new, new_moves))
            if not mid:
                next_move = (state[i], state[i] - 1)
                if not len(move) or (next_move[0] != move[-1][1] or next_move[1] != move[-1][0]):
                    new_moves = copy.deepcopy(move)
                    new_moves.append(next_move)
                    new = copy.deepcopy(state)
                    new[i] -= 1
                    res.append((new, new_moves))
    
    return res

def heuristic(state, length):
    h = 0
    for i in range(len(state)):
        h += length - state[i] - i
    return h

def test_solve_distinct_disks():
    def test(length, n, expected):
        sol = solve_distinct_disks(length, n)
        print("\nLength: {}  N: {}  Result: {}  Expected: {}".format(
            length, n, (-1 if not sol else 0 if not sol[0] else len(sol)), expected
        ))
        print(sol)
        assert((-1 if not sol else 0 if not sol[0] else len(sol)) == expected)

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