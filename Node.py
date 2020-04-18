import Lexer


# always has a grammar type
# and only terminals are going to have a token
class Node:
    def __init__(self, grammarType, *args):
        self.grammarType = grammarType
        if(len(args) > 0):
            self.token = args[0]
        self.children = []

	# Make a terminal node from a token
    #@staticmethod
    def terminal(token):
        return Node(token.tokenType + " " + token.lexeme, token)

    #@staticmethod
    def nonterminal(grammarType):
        return Node(grammarType)

    def addChild(self, child):
        self.children.append(child)
