

# def fac(k, kp):
#     s = k
#     res = 1
#     while s <= kp:
#         res *= s
#         s += 1
#     return res

# def calc(n, k, p):
#     if n > k:
#         return True
#     return fac(n - k + 1, n) / n ** k <= 1. - p

facs = [1]

def fac(k):
    global facs
    if k > len(facs):
        facs += [fac(i) for i in range(len(facs), k + 1)]
    if k == len(facs):
        facs.append(facs[-1] * k)
    return facs[k]

def calc(n, k, p):
    if k > n:
        return True
    return fac(n) / fac(n - k) / n ** k <= 1. - p

if __name__ == "__main__":
    n, p = 365, 0.5
    if p == 1.:
        print(n + 1)
    else: 
        for k in range(1, n + 2):
            if calc(n, k, p):
                print(k)
                break