
ST, ED, MID = 1, 2, 3

class Lexer:
    def __init__(self, s):
        self.s = s
        self.ind = 0

    def advance(self):
        # if self.ind >= len(self.s):
        #     return None
        res = self.s[self.ind]
        self.ind += 1
        return res

    def is_end(self):
        return self.ind >= len(self.s)

    def next_token(self):
        if self.is_end():
            return None
        type = ST
        res = ''

        assert self.advance() == '<'
        nxt = self.advance()
        if nxt == '/':
            type = ED
        else:
            res = nxt

        while True:
            c = self.advance()
            if c == '/':
                type = MID
                assert self.advance() == '>'
            elif c == '>':
                break
            else:
                res += c
        
        return type, res

class Paser:
    def __init__(self, lexer):
        self.lexer = lexer
        

