from collections import defaultdict
from sys import stdin

def eval(tree, nodes, root):
    val = nodes[root]
    if val not in '*+':
        return int(nodes[root])

    res = 0 if val == "+" else 1
    op = (lambda a, b: a + b) if val == "+" else (lambda a, b: a * b)
    for child in tree[root]:
        res = op(res, eval(tree, nodes, child))
    
    return res


if __name__ == "__main__":
    #m = int(input())
    res = []

    #for _ in range(m):
    lines = []
    for line in stdin:
        if line == '\n':
            break
        lines.append(line)
    for i in range(0, len(lines), 2):
        #pres = list(map(int, input().split(',')))
        pres = list(map(int, lines[i].split(',')))
        #nodes = list(input().split(','))
        nodes = list(lines[i + 1].split(','))

        tree = defaultdict(list)

        root = 0

        for i, e in enumerate(pres):
            if e == -1:
                root = i
                continue
            tree[e].append(i)

        res.append(eval(tree, nodes, root))

    print('\n'.join(map(str, res)))