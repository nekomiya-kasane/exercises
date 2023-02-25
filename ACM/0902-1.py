def get_index(s, pat):
    dp = [
        [pat[0] == '*' or s[0] == pat[i]] + [False for _ in range(len(s) - 1)] 
        for i in range(len(pat))
    ]

    for ins in range(1, len(s)):
        for inp in range(len(pat)):
            if pat[inp] == '*' or pat[inp] == s[ins]:
                ac = dp[inp][ins] = True if not inp else dp[inp - 1][ins - 1]
                if ac and inp == len(pat) - 1:
                    return ins
    return -1

if __name__ == "__main__":
    #s, pat = list(map(lambda x: x.strip(' ').strip('"'), input().split(',')))
    #s, pat = eval(input())
    #print(get_index(s, pat[::-1]))

    # tests
    #assert(get_index("Hello world", "ow"[::-1]) == 7)
    # assert(get_index("Hello world", "l*o"[::-1]) == 9)
    # assert(get_index("Hello world Hello world", "l**"[::-1]) == 2)
    # print(get_index("Heolrllo wololrld.", "***"))
    print(get_index("Hello world", "eH"[::-1]))
