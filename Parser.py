from Node import Node


class Parser:
    TYPES = {"int", "float", "bool"}

    def __init__(self):
        self.i = 0

    # statement is a list of tokens
    def parse(self, statement):
        LEN = len(statement)
        self.i = 0
        return self.parseS(statement, self.i, LEN)

    # S -> A
    def parseS(self, tokens, i, LEN):
        n = Node.nonterminal("S")
        if(self.isInBounds(self.i, LEN)):
            # D -> <type> <id>
            if(tokens[self.i].lexeme in self.TYPES):
                n.addChild(self.parseD(tokens, self.i, LEN))
                if(tokens[self.i+1].tokenType == "SEPARATOR"):
                    n.addChild(Node.terminal(tokens[self.i]))
                    self.i += 1
                    return n
        n.addChild(self.parseA(tokens, self.i, LEN))
        return n

    def parseD(self, tokens, i, LEN):
        if(self.isInBounds(self.i, LEN)):
            n = Node.nonterminal("D")
            n.addChild(Node.terminal(tokens[self.i]))
            self.i += 1
            return n
        else:
            self.outOfBounds(self.i, LEN)

    # A -> <identifier> = <expression>
    def parseA(self, tokens, i, LEN):
        if(self.isInBounds(self.i, LEN)):
            n = Node.nonterminal("A")
            n.addChild(Node.terminal(tokens[self.i]))  # <identifier>
            self.i += 1  # index to =
            n.addChild(Node.terminal(tokens[self.i]))  # =
            self.i += 1  # index to expression
            n.addChild(self.parseE(tokens, self.i, LEN))  # <expression>
            return n
        else:
            self.outOfBounds(self.i, LEN)

    # E -> <T> <E'>
    def parseE(self, tokens, i, LEN):
        if(self.isInBounds(self.i, LEN)):
            n = Node.nonterminal("E")
            n.addChild(self.parseT(tokens, self.i, LEN))  # <T>
            n.addChild(self.parseEPrime(tokens, self.i, LEN))  # <E'>
            return n
        else:
            self.outOfBounds(self.i, LEN)

    # T -> <F> <T'>
    def parseT(self, tokens, i, LEN):
        n = Node.nonterminal("T")
        n.addChild(self.parseF(tokens, self.i, LEN))
        n.addChild(self.parseTPrime(tokens, self.i, LEN))
        return n

    # E' -> + T E' | - T E' | 0
    def parseEPrime(self, tokens, i, LEN):
        n = Node.nonterminal("E'")
        if(self.isInBounds(self.i+1, LEN)):
            t = tokens[self.i+1]  # gets + or -
            if(t.lexeme == "+" or t.lexeme == "-"):
                self.i += 1  # increments to the + -
                n.addChild(Node.terminal(t))  # save the + -
                self.i += 1  # increments to the character after the + -
                n.addChild(self.parseT(tokens, self.i, LEN))
                n.addChild(self.parseEPrime(tokens, self.i, LEN))
            return n
        else:
            self.outOfBounds(self.i, LEN)

    def parseTPrime(self, tokens, i, LEN):
        n = Node.nonterminal("T'")
        if(self.isInBounds(self.i+1, LEN)):
            t = tokens[self.i+1]
            if(t.lexeme == "*" or t.lexeme == "/"):
                self.i += 1
                n.addChild(Node.terminal(t))
                self.i += 1
                n.addChild(self.parseF(tokens, self.i, LEN))
                n.addChild(self.parseTPrime(tokens, self.i, LEN))
            return n
        else:
            self.outOfBounds(self.i, LEN)

    def parseF(self, tokens, i, LEN):
        n = Node.nonterminal("F")
        if(self.isInBounds(self.i, LEN)):
            t = tokens[self.i]
            if(t.tokenType == "IDENTIFIER" or t.tokenType == "NUMBER"):
                n.addChild(Node.terminal(t))
            else:
                print("Syntax error saw: ",
                      t.tokenType, ", expected identifier or number")
            return n
        else:
            self.outOfBounds(self.i, LEN)

    def isInBounds(self, i, LEN):
        return i < LEN

    def outOfBounds(self, i, LEN):
        print("Index: ", i, " greater than or equal to LEN = ", LEN)
