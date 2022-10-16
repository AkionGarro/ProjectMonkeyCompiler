from antlr4 import *
import eel
from Generated.MonkeyGrammarLexer import MonkeyGrammarLexer
from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.error.ErrorListener import ErrorListener

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
    consoleResultError = consoleResultError.strip()
    print("getConsoleResult")
    print(consoleResultError)
    print("end")

    if consoleResultError != "":
        txt = consoleResultError
    else:
        if consoleResult != "":
            txt = consoleResult
        else:
            txt = ["Syntactic analysis Sucessfull"]

    consoleResultError = ""
    return txt


@eel.expose
def send_data(msg):
    print(msg)


def printTokens(lista):
    global consoleResultTokens
    res = ""
    for t in lista:
        res += "Line: " + str(t) + "  |  Type: " + str(t.type) + "  |  Lexeme: " + t.text;
        res += "\n";
    consoleResultTokens += res


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
    consoleResult = visitor.consoleResult
    visitor.consoleResult = ""

eel.start('index.html', mode='my_portable_chromium', host='localhost', port=27000, block=True)
