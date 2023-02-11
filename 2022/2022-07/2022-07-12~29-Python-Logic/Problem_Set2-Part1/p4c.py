def p4c(a0: bool, a1: bool, a2: bool, b0: bool, b1: bool, b2: bool):
    return (a2 and (a2 ^ b2)) or \
        ((a2 == b2) and ((a1 and (a1 ^ b1)) or ((a1 == b1) and (a0 and (a0 ^ b0)))))

# Check
def check(a0: bool, a1: bool, a2: bool, b0: bool, b1: bool, b2: bool) -> bool:
    res = p4c(a0, a1, a2, b0, b1, b2)
    ref = (a0 + (a1 << 1) + (a2 << 2)) > (b0 + (b1 << 1) + (b2 << 2))
    return res == ref

for n in range(0, 1 << 6):
    try:
        assert(check(
            bool(n & 0b000001),
            bool(n & 0b000010),
            bool(n & 0b000100),
            bool(n & 0b001000),
            bool(n & 0b010000),
            bool(n & 0b100000),
            ))
    except:
        print(bin(n))