from Generated.MonkeyGrammarListener import MonkeyGrammarListener


class KeyPrinter(MonkeyGrammarListener):
    def exitKey(self, ctx):
        print("Oh, a key!")