from antlr4 import *
import eel

from Generated.MonkeyGrammarLexer import MonkeyGrammarLexer
from Generated.MonkeyGrammarListener import MonkeyGrammarListener
from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor
from antlr4.tree.Tree import TerminalNodeImpl


eel.init('GUI')
consoleResult = ""

@eel.expose
def getConsoleResult():
    print (consoleResult)
    return consoleResult

@eel.expose
def send_data(msg):
    print(msg)

@eel.expose
def startInterpreter(text):

    f = open('test.txt', 'w')
    f.write(text)
    f.close()
    msg = 'test.txt';
    input_stream = FileStream(msg)
    lexer = MonkeyGrammarLexer(input_stream)
    lista = lexer.getAllTokens()
    inst = MonkeyGrammarLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MonkeyGrammarParser(tokens)
    res = ""

    for t in lista:
        res += "type: " + str(t.type) + " Lexeme:" + t.text+ "Row"+t.getL;
        res += "\n";
    global consoleResult
    consoleResult = res;

    """tree = parser.startRule()
    visitor = MonkeyGrammarVisitor()
    result = visitor.visit(tree)
    print(result)
    """





eel.start('index.html', mode='my_portable_chromium',host='localhost',port=27000,block=True )