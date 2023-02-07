def p1c(a0: bool, a1: bool, b0: bool, b1: bool):
    return ((a1 ^ b1) and a0 and b0) or (a1 and b1) # s2


# Check
def check(a0: bool, a1: bool, b0: bool, b1: bool) -> bool:
    res = p1c(a0, a1, b0, b1)
    ref = bool((a0 + (a1 << 1) + b0 + (b1 << 1)) & 0b0100)
    return res == ref

for n in range(0, 1 << 4):
    assert(check(
        bool(n & 0b0001),
        bool(n & 0b0010),
        bool(n & 0b0100),
        bool(n & 0b1000)))