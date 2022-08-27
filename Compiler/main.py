from antlr4 import *
import eel

from Generated.MonkeyGrammarLexer import MonkeyGrammarLexer
from Generated.MonkeyGrammarListener import MonkeyGrammarListener
from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor
from KeyPrinter import KeyPrinter



eel.init('GUI')
eel.start('index.html', mode='my_portable_chromium',
                        host='localhost',
                        port=27000,
                        block=True )
print("hola mundo")
input = 'test.txt'
input_stream = FileStream(input)
lexer = MonkeyGrammarLexer(input_stream)
token = CommonTokenStream(lexer)
parser = MonkeyGrammarParser(token)
tree = parser.startRule()
visitor = MonkeyGrammarVisitor()
visitor.visit(tree)

