def p4a(a: bool, b: bool):
    return a and (a ^ b)

# Check
def check(a: bool, b: bool) -> bool:
    res = p4a(a, b)
    ref = a > b
    return res == ref

for n in range(0, 1 << 2):
    try:
        assert(check(
            bool(n & 0b0001),
            bool(n & 0b0010)
            ))
    except:
        print(bin(n))