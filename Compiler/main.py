from antlr4 import *
import eel
from Generated.MonkeyGrammarLexer import MonkeyGrammarLexer
from Generated.MonkeyGrammarListener import MonkeyGrammarListener
from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.error.ErrorListener import ErrorListener

eel.init('GUI')
consoleResult = ""

class MyErrorListener( ErrorListener ):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        global consoleResult
        consoleResult = str(line) + ":" + str(column) + ": sintax ERROR, " + str(msg)


    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        global consoleResult
        consoleResult = "Ambiguity ERROR, " + str(configs)


    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        global consoleResult
        consoleResult = "Attempting full context ERROR, " + str(configs)


    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        global consoleResult
        consoleResult = "Context ERROR, " + str(configs)


@eel.expose
def getConsoleResult():
    print (consoleResult)
    return consoleResult

@eel.expose
def send_data(msg):
    print(msg)

@eel.expose
def startInterpreter(text):
    print("---------------------")
    global consoleResult
    consoleResult = ""
    print(text)
    inputText = InputStream(text)
    lexer = MonkeyGrammarLexer(inputText)
    stream = CommonTokenStream(lexer)
    parser = MonkeyGrammarParser(stream)
    parser._listeners = [MyErrorListener()]
    tree = parser.program()
    visitor = MonkeyGrammarVisitor()
    visitor.visit(tree)


eel.start('index.html', mode='my_portable_chromium',host='localhost',port=27000,block=True )