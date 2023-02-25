import math

VAR, FUN, LP, RP, NUM, PLUS, MINUS, MUL, DIV, PWR = 'VAR', 'FUN', 'LP', 'RP', 'NUM', 'PLUS', 'MINUS', 'MUL', 'DIV', 'PWR'

functions = ['sin', 'cos', 'tan', 'ln']

bi_ops = '+-*/^'
bi_ops_map = {'+': PLUS, '-': MINUS, '*': MUL, '/': DIV, '^': PWR}

BIOP, NUM, VAR, FUN = 'BIOP', 'NUM', 'VAR', 'FUN'

class Token:
    def __init__(self, type, value = None) -> None:
        self.type = type
        self.value = value

    def __str__(self) -> str:
        return "[{}: {}]".format(self.type, self.value)
    
    def __repr__(self) -> str:
        return self.__str__()
    
class Lexer:
    def __init__(self, text) -> None:
        self.text = text
        self.pos = 0
        self.current_char = None if not self.text[0] else self.text[0]

    def error(self):
        raise RuntimeError('error')

    def advance(self):
        self.pos += 1
        self.current_char = None if self.pos >= len(self.text) else self.text[self.pos]
        return self.current_char

    def jump_to(self, pos):
        self.pos = pos
        self.current_char = None if self.pos >= len(self.text) else self.text[self.pos]
        return self.current_char

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()
    
    def raw_word(self):
        res = ''
        if not self.current_char or (not self.current_char.isalpha() and not self.current_char == '_'):
            return None
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            res += self.current_char
            self.advance()
        return res

    def integer(self):
        res = ''
        while self.current_char and self.current_char.isdigit():
            res += self.current_char
            self.advance()
        return res

    def raw_float(self):
        res = ''
        if self.current_char and self.current_char.isdigit():
            res = self.integer()
        if self.current_char == '.':
            self.advance()
            res = res + '.' + self.integer()
            return res, False
        return res, True

    def float(self):
        res, is_int = self.raw_float()
        old_pos = -1
        self.skip_whitespace() 
        if self.current_char and (self.current_char.upper() == 'E'):
            old_pos = self.pos
            self.advance()
            self.skip_whitespace()
            sign = None
            if self.current_char in '+-':
                sign = self.current_char
                self.advance()
            if self.current_char.isdigit():
                res += "E" + (sign if sign else "") + self.raw_float()[0]
                return float(res)
            self.jump_to(old_pos)
        return int(res) if is_int else float(res)
            
        
    def number(self):
        return self.float()

    def word(self):
        left_pos = self.current_char
        res = self.raw_word()
        if res in functions:
            self.jump_to(left_pos)
            return None
        return res

    def function(self):
        left_pos = self.current_char
        res = self.raw_word()
        if res not in functions:
            self.jump_to(left_pos)
            return None
        return res

    def word_or_function(self):
        res = self.raw_word()
        if res:
            if res in functions:
                return FUN, res
            return VAR, res
        return None, None

    #
    def get_next_token(self):
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isalpha():
                type, val = self.word_or_function()
                return Token(type, val)
            elif self.current_char.isdigit():
                return Token(NUM, self.number())
            elif self.current_char in bi_ops:
                res = Token(bi_ops_map[self.current_char])
                self.advance()
                return res
            elif self.current_char == '(':
                self.advance()
                return Token(LP)
            elif self.current_char == ')':
                self.advance()
                return Token(RP)
            else:
                self.error()


###################################################

class Indenter:
    indent = ""
    def get_indent(self):
        return self.indent
    def push_indent(self):
        self.indent += "  "
    def pop_indent(self):
        self.indent = self.indent[:-2]

indenter = Indenter()

class AST:
    def __repr__(self) -> str:
        return self.__str__()

class BiOp(AST):
    def __init__(self, left, op, right) -> None:
        super().__init__()
        self.left = left
        self.op = op
        self.right = right
        self.type = BIOP

    def __str__(self) -> str:
        indenter.push_indent()
        ind1 = indenter.get_indent()
        ind2 = ind1[:-2]
        res = "[{0}: \n{4}{1},\n{4}{2},\n{4}{3}\n{5}]".format("BiOp", self.left, self.op, self.right, ind1, ind2)
        indenter.pop_indent()
        return res

class Num(AST):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
        self.type = NUM

    def __str__(self) -> str:
        return "[{}: {}]".format("NUM", self.value)
    
    def __repr__(self) -> str:
        return self.__str__()

class Var(AST):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return "[{}: {}]".format("VAR", self.name)
    
    def __repr__(self) -> str:
        return self.__str__()

class Fun(AST):
    def __init__(self, name, value):
        super().__init__()
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return "[{}: {}, {}]".format("FUN", self.name, self.value)
    
    def __repr__(self) -> str:
        return self.__str__()

class Parser(AST):
    def __init__(self, lexer: Lexer) -> None:
        super().__init__()
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise RuntimeError('error')

    def advance(self):
        self.current_token = self.lexer.get_next_token()

    def eat(self, type):
        if self.current_token and (self.current_token.type == type):
            self.current_token = self.lexer.get_next_token()
            return
        self.error()

    def expr(self):
        if not self.current_token:
            self.error()
        node = self.term()
        while self.current_token and self.current_token.type in (PLUS, MINUS):
            last = self.current_token.type
            self.eat(self.current_token.type)
            node = BiOp(node, last, self.term())
        return node

    def factor(self):
        if not self.current_token:
            self.error()
        if self.current_token.type == NUM:
            res = Num(self.current_token.value)
            self.advance()
            return res
        if self.current_token.type == VAR:
            res = Var(self.current_token.value)
            self.advance()
            return res
        if self.current_token.type == FUN:
            name = self.current_token.value
            self.eat(FUN)
            return Fun(name, self.factor())
        if self.current_token.type == LP:
            self.eat(LP)
            node = self.expr()
            self.eat(RP)
            return node
        if self.current_token.type in (MINUS, PLUS):
            last = self.current_token.type
            self.eat(last)
            return BiOp(Num(0), last, self.factor())

    def powered(self):
        node = self.factor()
        if (not self.current_token) or (self.current_token.type != PWR):
            return node
        else:
            self.eat(PWR)
        return BiOp(node, PWR, self.factor())

    def term(self):
        node = self.powered()
        while self.current_token and self.current_token.type in (MUL, DIV, VAR):
            last = self.current_token.type
            if last == VAR:
                node = BiOp(node, MUL, self.powered())
                continue
            self.eat(self.current_token.type)
            node = BiOp(node, last, self.powered())
        return node

    def parse(self):
        return self.expr()


calculate = {
    PLUS: lambda a,b: a + b,
    MINUS: lambda a,b: a - b,
    MUL: lambda a,b: a * b,
    DIV: lambda a,b: a / b,
    PWR: lambda a,b: a ** b,
    'sin': lambda a: math.sin(a),
    'cos': lambda a: math.cos(a),
    'tan': lambda a: math.tan(a),
    'ln': lambda a: math.log(a),
}


class Simplifier(AST):
    def __init__(self, tree):
        self.tree = tree

    def simplify(self):
        return

    def dfs(self, node):
        if node.type != BIOP:
            return
        if node.left.type == BIOP:
            self.dfs(node.left)
        if node.right.type == BIOP:
            self.dfs(node.right)
        if (node.left.type == NUM) and (node.right.type == NUM):
            node = Num(calculate[node.op](node.left.value, node.right.value))
        if (node.type == FUN) and (node.value.type == NUM):
            node = Num(calculate[node.name](node.value.value))
            


if __name__ == '__main__':
    s = ' (-1297E2 - sin (4.23) + cos (7var + 6 ^ 2)^2) - 7'
    lexer = Lexer(s)
    res = []
    # while True:
    #     next = lexer.get_next_token()
    #     if not next:
    #         break
    #     res.append(next)
    # print(res)

    parser = Parser(lexer)
    res = parser.parse()
    print(res)
        