def p4b(a0: bool, a1: bool, b0: bool, b1: bool):
    return (a1 and (a1 ^ b1)) or ((a1 == b1) and (a0 and (a0 ^ b0)))

# Check
def check(a0: bool, a1: bool, b0: bool, b1: bool) -> bool:
    res = p4b(a0, a1, b0, b1)
    ref = (a0 + (a1 << 1)) > (b0 + (b1 << 1))
    return res == ref

for n in range(0, 1 << 4):
    try:
        assert(check(
            bool(n & 0b0001),
            bool(n & 0b0010),
            bool(n & 0b0100),
            bool(n & 0b1000)))
    except:
        print(bin(n))