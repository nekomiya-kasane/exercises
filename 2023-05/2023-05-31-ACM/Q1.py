from collections import defaultdict
from sys import stdin

def solve(tree, nodes, root):
    value = nodes[root].strip()
    if value != '*' and value != '+':
        return int(value)

    if value == "+":
        ret = 0
        for v in tree[root]:
            ret = ret + solve(tree, nodes, v)
    else:
        ret = 1
        for v in tree[root]:
            ret = ret * solve(tree, nodes, v)

    return ret


if __name__ == "__main__":
    result = []
    lines = []
    for line in stdin:
        if not(len(line.strip())):
            break
        lines.append(line)
    for i in range(0, len(lines), 2):
        pres = list(map(int, lines[i].split(',')))
        nodes = list(lines[i + 1].split(','))

        tree = defaultdict(list)
        root = 0

        for i, e in enumerate(pres):
            if e == -1:
                root = i
                continue
            tree[e].append(i)

        result.append(solve(tree, nodes, root))

    print('\n'.join(map(str, result)))