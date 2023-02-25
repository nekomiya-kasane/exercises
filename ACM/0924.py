# def point_in_shape(px, py, y, h, w1, w2):
#     # under
#     b1 = 2. * h * (py  -  y) / (w2  -  w1)  -  (w1  +  w2) / 4.  -  px <= 0
#     b2 = 2. * h * (py  -  y) / (w1  -  w2)  +  (w1  +  w2) / 4.  -  px >= 0
#     b3 = abs(py  -  y) <= h / 2.
#     return b1 and b2 and b3

# def calc(ya, ha, wa1, wa2, yb, hb, wb1, wb2):
#     dir1 = 

#     if yb  +  hb / 2. <= ya  -  ha / 2.:
#         return 0
#     if yb  +  hb / 2. <= ya  +  ha / 2.:
#         if yb  -  hb / 2. >= ya  -  ha / 2.:
#             return 1.

# def gen_f(ya, ha, wa1, wa2):
#     def f(x):
#         if x <=  - wa1/ 2:
#             return 
#     return f
        
def integrate(f, a, b, N):
    result = 0; 
    dx = abs(b - a) / N
    while a < b:
        result += (f(a) + f(a + dx)) * dx / 2
        a += dx
    return result

def get_fun(y, h, w1, w2):
    def f(x):
        return (w2 - w1) / (2 * h) * x + (h * w1 + h * w2 + 2 * y * w1 - 2 * y * w2) / (4 * h)
    return f

def inter(ya, ha, wa1, wa2, yb, hb, wb1, wb2):
    f1 = get_fun(ya, ha, wa1, wa2)
    f2 = get_fun(yb, hb, wb1, wb2)
    def g(x):
        return 2 * min(f1(x), f2(x))
    return g

def union(ya, ha, wa1, wa2, yb, hb, wb1, wb2):
    f1 = get_fun(ya, ha, wa1, wa2)
    f2 = get_fun(yb, hb, wb1, wb2)
    def g(x):
        return 2 * max(f1(x), f2(x))
    return g 

if __name__ == "__main__":
    ya, ha, wa1, wa2 = map(int, input().strip().split())
    yb, hb, wb1, wb2 = map(int, input().strip().split())

    if (yb  +  hb / 2. <= ya  -  ha / 2.) or (ya  +  ha / 2. <= yb  -  hb / 2.):
        print(0)
        exit(0)

    soko = [ya - ha / 2., ya + ha / 2., yb - hb / 2., yb + hb / 2.]
    soko.sort()

    args = (ya, ha, wa1, wa2, yb, hb, wb1, wb2)

    intersect = integrate(inter(*args), soko[1], soko[2], 10000)
    uni = (wa1 + wa2) * ha / 2 + (wb1 + wb2) * hb / 2 - intersect

    print(intersect, uni)

    print(intersect / uni)




# def calc(arr, cnt):
#     n = len(arr)
#     dp = [[0] * (cnt + 1) for _ in range(n + 1)]
#     s = [0] * (n + 1)
#     for i in range(1, n + 1):
#         s[i] = s[i - 1] + arr[i - 1]
#         for k in range(1, min(i + 1, cnt + 1)):
#             if k == 1:
#                 dp[i][k] = s[i] / i
#                 continue
#             for j in range(k - 1, i):
#                 dp[i][k] = max(dp[i][k], dp[j][k - 1] + (s[i] - s[j]) / (i - j))
    
#     # mx = dp[n][1]
#     # for i in range(2, cnt + 1):
#     #     mx = max(mx, dp[n][i])
#     # return mx

#     return dp[n][cnt]


# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int, input().strip().split()))
#     k = int(input())

#     print(round(calc(arr, k)))