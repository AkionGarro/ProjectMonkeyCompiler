from antlr4 import *

from Generated.MonkeyGrammarLexer import MonkeyGrammarLexer


file_name = 'test.txt'
input_stream = FileStream(file_name)
lexer = MonkeyGrammarLexer(input_stream)
print('input_stream:')
print(input_stream)
print()
token_stream = CommonTokenStream(lexer)
token_stream.fill()
print('tokens:')
for tk in token_stream.tokens:
    print(tk)
print()
