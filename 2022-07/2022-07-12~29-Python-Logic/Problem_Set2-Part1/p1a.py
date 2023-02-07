def p1a(a0: bool, a1: bool, b0: bool, b1: bool):
    return a0 ^ b0 # s0

# Check
assert(p1a(1, 1, 0, 0) == 1)
assert(p1a(1, 1, 1, 1) == 0)