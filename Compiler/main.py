from antlr4 import *
import eel
from Generated.MonkeyGrammarLexer import MonkeyGrammarLexer
from Generated.MonkeyGrammarListener import MonkeyGrammarListener
from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.error.ErrorListener import ErrorListener

eel.init('GUI')
consoleResultError = ""
consoleResultTokens = ""

class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        global consoleResultError
        consoleResultError += str(line) + ":" + str(column) + ": Syntax Error, " + str(msg)
        consoleResultError += "\n"
        consoleResultError += "\n"


@eel.expose
def getConsoleResult():
    global consoleResultError
    if consoleResultError !="" :
        txt = consoleResultError
    else:
        txt = "Syntactic analysis Sucessfull"
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
    visitor = MonkeyGrammarVisitor()
    visitor.visit(tree)


eel.start('index.html', mode='my_portable_chromium', host='localhost', port=27000, block=True)
