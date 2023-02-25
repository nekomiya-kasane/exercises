# if __name__ == "__main__":

#         x = int(input())

#         res = ""

#         for i in reversed(range(10)):
#             if x >= 2 ** i:
#                 res += chr(ord('a') + i)
#                 x -= 2 ** i

#         print(res)

from collections import defaultdict
from email.policy import default

def subString(s, n):
  
    pre =  0xFFFFFFFF
  
    count = 0

    for i in range(len(s)):
        hash = defaultdict(int)
        for c in s[i:]:
            pre ^= (1 << ord(c) - 97)
            if (32 - pre.bit_count()) == 1:
                count += hash.get(pre, 1)
                hash[pre] += 1
          
    return count
  
if __name__ == '__main__':
    S = "babab"
    N = len(S)
    print(subString(S, N))
