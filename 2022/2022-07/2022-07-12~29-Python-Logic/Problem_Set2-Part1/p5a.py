def p5a(a0: bool, a1: bool, a2: bool, a3: bool, a4: bool):
    return a0 ^ a1 ^ a2 ^ a3 ^ a4

# Check
def check(a0: bool, a1: bool, a2: bool, a3: bool, a4: bool) -> bool:
    res = p5a(a0, a1, a2, a3, a4)
    ref = bool((a0 + a1 + a2 + a3 + a4) & 0b1)
    return res == ref

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