import sys


class SegTree:
    def __init__(self, n) -> None:
        N = 8 * n
        self.sum = [0] * N
        self.len = [0] * N
        self.tag = [0] * N
        self.lp = [0] * N
        self.rp = [0] * N

    def pull(self, l, r, o):
        if self.tag[o]:
            self.sum[o] = self.lp[o] = self.rp[o] = 1; self.len[o] = r - l;
        elif l + 1 == r: 
            self.sum[o] = self.len[o] = self.lp[o] = self.rp[o] = 0;
        else: 
            lson = o * 2 + 1; rson = o * 2 + 2
            self.sum[o] = self.sum[lson] + self.sum[rson] - (self.rp[lson] & self.lp[rson])
            self.len[o] = self.len[lson] + self.len[rson]
            self.lp[o] = self.lp[lson]
            self.rp[o] = self.rp[rson]

    def modify(self, l, r, ql, qr, v, o=0):
        if ql <= l and r <= qr:
            self.tag[o] += v
        else:
            mid = (l + r) >> 1
            lson, rson = o * 2 + 1, o * 2 + 2
            if qr <= mid:
                self.modify(l, mid, ql, qr, v, lson)
            elif mid <= ql:
                self.modify(mid, r, ql, qr, v, rson)
            else:
                self.modify(l, mid, ql, mid, v, lson)
                self.modify(mid, r, mid, qr, v, rson)
        self.pull(l, r, o)

    def qsum(self):
        return self.sum[0]

    def qlen(self):
        return self.len[0]


class Seg:
    def __init__(self, l, r, y, v):
        self.l = l
        self.r = r
        self.y = y
        self.v = v

    def __lt__(self, other):
        return self.y < other.y

if __name__ == "__main__":
    v = []
    try:
        file_name = "frames_1.txt"
        #file_name = input("Which data file do you want to use?")
        #if file_name[-4:] != '.txt':
        #    file_name += '.txt'
        raw_coordinates = open(file_name).readlines()
        for x in raw_coordinates:
            x1, y1, x2, y2 = list(map(int, x.split()))
            v.append(Seg(x1, x2, y1, 1))
            v.append(Seg(x1, x2, y2, -1))
        v.sort()
    except:
        print("Failed to open file.")
        sys.exit(-1)

    ans = 0; preY = 0
    N = 10005
    tree = SegTree(N)
    for i in v:
        ans += tree.qsum() * 2 * (i.y - preY)
        tt = tree.qlen()
        tree.modify(-N, N, i.l, i.r, i.v)
        ans += abs(tt - tree.qlen())
        preY = i.y

    print(f"The perimeter is: {ans}")
