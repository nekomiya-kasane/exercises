chs = ['q', 'w', 'k', 'h', 'j']

def cond_0(s):
    return [c in chs for c in s].count(1) == len(s)

def cond_1(s):
    for i in range(len(s) - 5):
        if cond_0(s[i : i + 5]):
            return True
    return False

def cond_2(strs, find):
    return strs.count(find) > 0

def filter_strings(arr):
    res = [False for _ in range(len(arr))]
    for i in range(len(arr)):
        if cond_1(arr[i]) or (cond_2(arr[max(0, i - 10) : i], arr[i])):
            res[i] = True

    for r in res:
        print('yes' if r else 'no')
     
if __name__ == '__main__':
    n = int(input().strip())
    arr = [input().strip() for _ in range(n)]

    #n = 13
    #arr = ['hello', 'are you ok?', 'how are you', 'how are you', 'qwwwwwwaaa', 'you so good', \
    #    'wow', 'owiq jjww', 'are you ok?', 'QWQ', 'what\'s that???', 'no...']

    filter_strings(arr)