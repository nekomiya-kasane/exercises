def p5d(a0: bool, a1: bool, a2: bool, a3: bool, a4: bool):
    return ((a0 or a1 or a2 or a3 or a4) and a0) ^ (a0 ^ a1 ^ a2 ^ a3 ^ a4)

# Check
def check(a0: bool, a1: bool, a2: bool, a3: bool, a4: bool) -> bool:
    res = p5d(a0, a1, a2, a3, a4)
    ref1 = ((a0 + (a1 << 1) + (a2 << 2) + (a3 << 3) + (a4 << 4)) != 0) and a0
    ref2 = bool((a0 + a1 + a2 + a3 + a4) & 0b1)
    return res == ((ref1 and not ref2) or (ref2 and not ref1))

for n in range(0, 1 << 5):
    try:
        assert(check(
            bool(n & 0b00001),
            bool(n & 0b00010),
            bool(n & 0b00100),
            bool(n & 0b01000),
            bool(n & 0b10000)
            ))
    except:
        print(bin(n))