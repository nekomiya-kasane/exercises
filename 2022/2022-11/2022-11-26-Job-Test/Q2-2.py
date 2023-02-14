import math, sys

idx = 0

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    s = math.floor(math.log10(len(lines))) + 1
    prefix = "{:" + str(s) + "d} "
    
    def add_prefix(line):
        global idx
        idx = idx + 1
        return prefix.format(idx) + line

    results = map(add_prefix, lines)
    print(''.join(results))