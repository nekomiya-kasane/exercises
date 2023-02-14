from collections import defaultdict
from operator import * 
from collections import defaultdict
from datetime import date
import sys

def todate(s: str):
    y, m, d = map(int, s.split('-'))
    return (date(y, m, d) - date(2021, 1, 1)).days

def nonzero(dic: dict):
    return len(dic) - countOf(dic.values(), 0)

def advance(dic, arr, ind, subs=False):
    if ind >= len(arr):
        return ind
    tmp = arr[ind][1]
    while ind < len(arr) and arr[ind][1] == tmp:
        if subs:
            dic[arr[ind][0]] -= 1
        else:
            dic[arr[ind][0]] += 1
        ind += 1
    return ind

if __name__ == "__main__":
    n = int(input())
    arr = list(map(lambda x: (x[0], todate(x[1])), [input().strip().split() for _ in range(n)]))
    k = int(input())

    arr.sort(key=lambda x: x[1])

    lf = 0
    rt = 0
    win = sys.maxsize

    cnts = defaultdict(int)

    while rt < len(arr):
        while nonzero(cnts) < k and rt != len(arr):
            rt = advance(cnts, arr, rt, False)
        while nonzero(cnts) >= k and lf <= rt:
            lf = advance(cnts, arr, lf, True)
        if rt == len(arr) and lf == 0 and nonzero(cnts) < n:
            break
        win = min(win, arr[rt - 1][1] - arr[lf - 1][1] + 1)
    
    print(win if win != sys.maxsize else -1)


    


    

