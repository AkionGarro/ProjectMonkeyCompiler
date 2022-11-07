import numpy as np
from antlr4 import *
import eel
from Generated.MonkeyGrammarLexer import MonkeyGrammarLexer
from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.error.ErrorListener import ErrorListener
import sys
sys.setrecursionlimit(2147483647)#para fibonacci hasta 35
#9223372036854775807

import Interpreter
from Interpreter import MyVisitor
from REPL import REPL

eel.init('GUI')
consoleResultError = ""
consoleResult = ""
consoleResultTokens = ""
repl = REPL()


class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        global consoleResultError
        consoleResultError += str(line) + ":" + str(column) + ": Syntax Error, " + str(msg)
        consoleResultError += "\n"
        consoleResultError += "\n"


@eel.expose
def getConsoleResult(mode):
    global consoleResultError
    global consoleResult

    print("Error: \n", consoleResultError)
    print("\nResult: \n", consoleResult)
    if consoleResultError !=['']:
        txt = str(consoleResult) + str(consoleResultError)
        print("console Result Error")
    else:
        if consoleResult !=['']:
            txt = consoleResult
            print("console Result")
        else:
            txt = ["Syntactic analysis Sucessfull"]
            print("console Result Empty")

    consoleResultError = ""
    return txt


@eel.expose
def send_data(msg):
    print(msg)


@eel.expose
def startInterpreter(text):
    inputText = InputStream(text)
    lexer = MonkeyGrammarLexer(inputText)
    stream = CommonTokenStream(lexer)
    parser = MonkeyGrammarParser(stream)
    parser._listeners = [MyErrorListener()]
    tree = parser.program()
    visitor = MyVisitor()
    visitor.visit(tree)
    repl.data.print()
    global consoleResult
    global consoleResultError
    consoleResult = [visitor.consoleResult]
    consoleResultError = [visitor.consoleError]
    visitor.consoleError = ""
    visitor.consoleResult = ""


eel.start('index.html', mode='my_portable_chromium', host='localhost', port=27000, block=True)
