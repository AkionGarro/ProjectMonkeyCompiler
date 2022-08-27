from antlr4 import *

from Generated.MonkeyGrammarLexer import MonkeyGrammarLexer
from Generated.MonkeyGrammarListener import MonkeyGrammarListener
from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor
from KeyPrinter import KeyPrinter


def main():
    input = 'test.txt'
    input_stream = FileStream(input)
    lexer = MonkeyGrammarLexer(input_stream)
    token = CommonTokenStream(lexer)
    parser = MonkeyGrammarParser(token)
    tree = parser.startRule()
    visitor = MonkeyGrammarVisitor()
    visitor.visit(tree)

