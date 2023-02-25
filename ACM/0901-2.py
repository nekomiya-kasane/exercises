# def valid(s):
#     if len(s) < 3:
#         return False
#     si = ord(s[1]) - ord(s[0])
#     for i in range(1, len(s) - 1):
#         if ord(s[i + 1]) - ord(s[i]) != si:
#             return False
#     return True

# def check(s):
#     ss = []
#     tmp = ""
#     for c in s:
#         if c.isdigit():
#             tmp += c
#         else:
#             ss.append(tmp)
#             tmp = ""
#     if (len(tmp)):
#         ss.append(tmp)
#     for subs in ss:
#         if valid(subs):
#             return True
#     return False
        

# if __name__ == "__main__":
#     # n = int(input().strip())
#     # arr = []
#     # for _ in range(n):
#     #     arr.append(input().strip())

#     #arr = ["abc123aee22"], "abc12321a", "lxsb321yyy", "flww12345677"]
#     arr = ["a123456"]
#     for a in arr:
#         print("yes" if check(a) else "no")


# def operate(arr, op):
#     return list(map(lambda x: x + op, arr))

# def calc(arr):
#     res = 0
#     for e in arr:
#         res += abs(e)
#     return res

from datetime import timedelta
import random
from timeit import default_timer as timer

def optimized(arr, ops):
    n = len(arr)
    res = sum(list(map(lambda x: abs(x), arr)))
    resarr = []

    arr.sort()
    ind = 0
    for i in arr:
        if i >= 0:
            break
        ind += 1

    last_ind = ind
    for e in ops:
        diff = 0
        if e > 0: # plus
            while ind >= 1 and abs(arr[ind - 1]) < e:
                ind -= 1
                diff += abs(arr[ind] + e) - abs(arr[ind]) 
        elif e < 0: # minus
            while ind < n and arr[ind] < abs(e):
                diff += abs(arr[ind] + e) - abs(arr[ind]) 
                ind += 1
        res += diff + (n - ind - last_ind) * e
        last_ind = ind
        for a in arr:
            a += e
        resarr.append(res)
    return resarr

def original(arr, ops):
    def operate(arr, op):
        return list(map(lambda x: x + op, arr))

    def calc(arr):
        res = 0
        for e in arr:
            res += abs(e)
        return res

    resarr = [calc(operate(arr, e)) for e in ops]

    return resarr

    

if __name__ == "__main__":
    # n = int(input())
    # arr = list(map(int, input().strip().split(' ')))
    # m = int(input())
    # ops = list(map(int, input().strip().split(' ')))

    arr = [[random.randrange(-100, 100) for _ in range(random.randrange(5, 10))] for _ in range(100)]
    ops = [[random.randrange(-100, 100) for _ in range(random.randrange(1, 5))] for _ in range(100)]

    st = timer()
    opt_res = [optimized(arr[i], ops[i]) for i in range(len(arr))]
    end = timer()
    print(timedelta(seconds=end - st))
    st = timer()
    ori_res = [original(arr[i], ops[i]) for i in range(len(arr))]
    end = timer()
    print(timedelta(seconds=end - st))

    indic = []
    for i in range(len(ops)):
        if opt_res[i] != ori_res[i]:
            print(arr[i], ops[i], opt_res[i], ori_res[i])

    # arr = [-44, -16, 1, 5, 33]
    # ops = [-93]

    # optimized(arr, ops)



    

        


#     for e in ops:
#         arr = operate(arr, e)
#         print(calc(arr))

# def is_straight(cards):
#     dic = {'J': 11, 'Q': 12, 'K': 13, 'A': 1 }

#     def trans(card):
#         if len(card) > 1:
#             return -1
#         if card[0].isdigit():
#             return int(card[0])
#         return dic[card[0]]

#     cards = list(map(trans, cards))
#     cards.sort()
    
#     ind = 0
#     ousama = 0
#     while cards[ind] < 0:
#         ind += 1
#         ousama += 1
#     for i in range(ind + 1, len(cards)):
#         if cards[i] == cards[i - 1]:
#             print("false")
#             return
#             #return False
#         ousama -= cards[i] - cards[i - 1] - 1
#         if ousama < 0:
#             print("false")
#             return
#     print("true")
#     return

# if __name__ == '__main__':
#     is_straight(["A", "3", "2", "大王", "4"])
    


    