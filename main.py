import Parser
import Lexer
import sys
from pptree import print_tree

def exec(fileName):
    lexer = Lexer.Lexer()
    parser = Parser.Parser()

    f = open(fileName)
    s = f.read()
    tokens = lexer.lex(s)
    i = 0
    statements = []
    while(i < len(tokens)):
        stack = []
        if(tokens[i].tokenType == "IDENTIFIER" or tokens[i].tokenType == "KEYWORD"):
            while(tokens[i].tokenType != "SEPARATOR" and i < len(tokens)):
                stack.append(tokens[i])
                i += 1
            stack.append(tokens[i])
            statements.append(stack)
        i += 1

    for statement in statements:
        print_tree(parser.parse(statement), nameattr="grammarType")

if __name__ == '__main__':

    if(len(sys.argv) > 1):
        i = 1
        while(i < len(sys.argv)):
            exec(sys.argv[i])
            i += 1
    else:
        exec("input2.txt")
