import bisect as bs
import math

def solve(expr):
    arr = eval(expr)
    owner = math.ceil(math.log2(len(arr))) + 1

    st = 1 << 31

    owner_mask = sum([1 << i for i in range(owner)]) << (31 - owner)
    val_mask = ~(st | owner_mask)

    def gen_owner(i):
        return i << (31 - owner)

    ses = []

    for i in range(len(arr)):
        for j in range(int(len(arr[i]) / 2)):
            ses.append(arr[i][2 * j] | st | gen_owner(i))
            ses.append(arr[i][2 * j + 1] | gen_owner(i))
            #ses.insert(-1, arr[i][2 * j] | st | gen_owner(i))
            #ses.insert(-1, arr[i][2 * j + 1] | gen_owner(i))
    ses.sort(key=lambda x: val_mask & x)
            #bs.insort(ses, arr[i][2 * j] | st | gen_owner(i), key=lambda x: val_mask & x)
            #bs.insort(ses, arr[i][2 * j + 1] | gen_owner(i), key=lambda x: val_mask & x)

    coll = 0
    ws = []

    for se in ses:
        if st & se: # start
            coll += 1
            ws.append(coll)
        else: #end
            coll -= 1
            ws.append(coll)

    res = []

    for k in range(len(arr)):
        ind = 0
        total = 0
        for i in range(int(len(arr[k]) / 2)):
            s = arr[k][2 * i]
            e = arr[k][2 * i + 1]
            while ses[ind] & val_mask < s:
                ind += 1
            while ses[ind] & val_mask < e:
                if ws[ind]:
                    total += 1 / ws[ind] * ((ses[ind + 1] & val_mask) - (ses[ind] & val_mask))
                ind += 1
            ind += 1
        res.append(int(total))

    return res

if __name__ == "__main__":
    print(solve(input()))



# print("--------------------")
# print(solve("[[1234,1235],[1236,1238]]"))
# print(solve("[[1234,1235],[1235,1238],[1235, 1240]]"))
# print(solve("[[1234, 1240], [1236, 1238, 1245, 1250]]"))