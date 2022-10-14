from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor
from REPL import REPL
from antlr4.CommonTokenFactory import CommonToken


class MyVisitor(MonkeyGrammarVisitor):
    replVisitor = REPL()
    consoleResult = ""

    def visitProgramAST(self, ctx: MonkeyGrammarParser.ProgramASTContext):
        for i in range(0, len(ctx.statement())):
            self.visit(ctx.statement(i))

    def visitStatementLetAST(self, ctx: MonkeyGrammarParser.StatementLetASTContext):
        self.visit(ctx.letStatement())

    def visitStatementReturnAST(self, ctx: MonkeyGrammarParser.StatementReturnASTContext):
        self.visit(ctx.returnStatement())

    def visitStatementExpressionAST(self, ctx: MonkeyGrammarParser.StatementExpressionASTContext):
        self.visit(ctx.expressionStatement())


    def visitLetStatementAST(self, ctx: MonkeyGrammarParser.LetStatementASTContext):
        varName = self.visit(ctx.identifier())
        self.visit(ctx.expression())
        self.replVisitor.data.add(varName, self.replVisitor.stack.pop())


    def visitReturnStatementAST(self, ctx: MonkeyGrammarParser.ReturnStatementASTContext):
        self.visit(ctx.expression())

    def visitExpressionStatementAST(self, ctx: MonkeyGrammarParser.ExpressionStatementASTContext):
        self.visit(ctx.expression())

    def visitExpressionAST(self, ctx: MonkeyGrammarParser.ExpressionASTContext):
        self.visit(ctx.additionExpression())
        self.visit(ctx.comparison())

    def visitComparisonAST(self, ctx: MonkeyGrammarParser.ComparisonASTContext):
        index = 0

        for i in range(0, len(ctx.additionExpression())):
            self.visit(ctx.additionExpression(i))
            token = ctx.getChild(index).symbol
            index += 2
            op2 = (self.replVisitor.stack.pop())
            op1 = (self.replVisitor.stack.pop())
            if type(op2) == int:
                if token.text == "==":
                    flag = (op2==op1)
                    self.replVisitor.stack.append(flag)
                elif token.text == "!=":
                    flag = (op2 != op1)
                    self.replVisitor.stack.append(flag)
                elif token.text == "<":
                    flag = (op1<op2)
                    self.replVisitor.stack.append(flag)
                elif token.text == "<=":
                    flag = (op1 <= op2)
                    self.replVisitor.stack.append(flag)
                elif token.text == ">":
                    flag = (op1 > op2)
                    self.replVisitor.stack.append(flag)
                elif token.text == ">=":
                    flag = (op1 >= op2)
                    self.replVisitor.stack.append(flag)
                else:
                    print("Operador no existe")
            else:
                if token.text == "==":
                    flag = (op2 == op1)
                    self.replVisitor.stack.append(flag)
                elif token.text == "!=":
                    flag = (op2 != op1)
                    self.replVisitor.stack.append(flag)
                else:
                    print("No se permite este tipo de operacion en Str")


    def visitAdditionExpressionAST(self, ctx: MonkeyGrammarParser.AdditionExpressionASTContext):
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())

    def visitAdditionFactorAST(self, ctx: MonkeyGrammarParser.AdditionFactorASTContext):
        index = 0
        for i in range(0, len(ctx.multiplicationExpression())):
            self.visit(ctx.multiplicationExpression(i))
            token = ctx.getChild(index).symbol
            index += 2
            op2 = (int)(self.replVisitor.stack.pop())
            op1 = (int)(self.replVisitor.stack.pop())

            if token.text == "+":
                self.replVisitor.stack.append(op1 + op2)
            elif token.text == "-":
                self.replVisitor.stack.append(op1 - op2)


    def visitMultiplicationExpressionAST(self, ctx: MonkeyGrammarParser.MultiplicationExpressionASTContext):
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())

    def visitMultiplicationFactorAST(self, ctx: MonkeyGrammarParser.MultiplicationFactorASTContext):
        index = 0
        for i in range(0, len(ctx.elementExpression())):
            self.visit(ctx.elementExpression(i))
            token = ctx.getChild(index).symbol
            index += 2
            op2 = (int)(self.replVisitor.stack.pop())
            op1 = (int)(self.replVisitor.stack.pop())

            if token.text == "*":
                self.replVisitor.stack.append(op1 * op2)
            elif token.text == "/":
                self.replVisitor.stack.append(op1 / op2)

    def visitElementExpressionAST(self, ctx: MonkeyGrammarParser.ElementExpressionASTContext):
        self.visit(ctx.primitiveExpression())
        if ctx.getChildCount()>1:
            self.visit(ctx.getChild(1))


    def visitElementAccessAST(self, ctx: MonkeyGrammarParser.ElementAccessASTContext):
        self.visit(ctx.expression())

    def visitCallExpressionAST(self, ctx: MonkeyGrammarParser.CallExpressionASTContext):
        self.visit(ctx.expressionList())

    def visitPrimitiveExprDigitAST(self, ctx: MonkeyGrammarParser.PrimitiveExprDigitASTContext):
        self.replVisitor.stack.append((int)(ctx.DIGIT().symbol.text))
        return self.visitChildren(ctx)

    def visitPrimitiveExprStringAST(self, ctx: MonkeyGrammarParser.PrimitiveExprStringASTContext):
        self.replVisitor.stack.append(ctx.STRING().symbol.text)
        return self.visitChildren(ctx)

    def visitPrimitiveExprIdAST(self, ctx: MonkeyGrammarParser.PrimitiveExprIdASTContext):
        object = self.replVisitor.data.get(self.visit(ctx.identifier()))
        if (object != None):
            self.replVisitor.stack.append(object)
        else:
            print("El identificador no existe")

        return self.visitChildren(ctx)

    def visitPrimitiveExprBooleanAST(self, ctx:MonkeyGrammarParser.PrimitiveExprBooleanASTContext):
        self.visit(ctx.boolean())

    def visitPrimitiveExprBlockExprAST(self, ctx: MonkeyGrammarParser.PrimitiveExprBlockExprASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprArrLitAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrLitASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprArrFuncAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrFuncASTContext):
        self.visitChildren(ctx)
        token = ctx.getChild(0).start.text
        id = ctx.getChild(2).start.text

        if token == "len":
            arr = self.replVisitor.stack.pop()
            if self.consoleResult == "":
                self.consoleResult = str(len(arr))
            else:
                self.consoleResult += "\n" + str(len(arr))

        elif token == "first":
            arr = self.replVisitor.stack.pop()
            if self.consoleResult == "":
                if type(arr) == dict:
                     self.consoleResult = str(arr[next(iter(arr))])
                else:
                    self.consoleResult = "\n" + str(arr[0])
            else:
                if type(arr) == dict:
                    self.consoleResult = str(arr[next(iter(arr))])
                else:
                    self.consoleResult = "\n" + str(arr[0])

        elif token == "last":
            arr = self.replVisitor.stack.pop()

            if type(arr) == dict:
                self.replVisitor.stack.append(arr[list(arr)[-1]])
            else:
                self.replVisitor.stack.append(arr[-1])


        elif token == "rest":
            arr = self.replVisitor.stack.pop()

            if type(arr) == dict:
                self.replVisitor.stack.append(list(arr.values())[1:])
            else:
                self.replVisitor.stack.append(list(arr.values())[1:])


        elif token == "push":

            values = []

            while len(self.replVisitor.stack) > 1:
                values.append(self.replVisitor.stack.pop())

            arr = self.replVisitor.stack.pop()

            #reverse values
            values.reverse()

            for value in values:
                arr.append(value)

            self.replVisitor.data.add(id, arr)


    def visitPrimitiveExprFuncAST(self, ctx: MonkeyGrammarParser.PrimitiveExprFuncASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprHashAST(self, ctx: MonkeyGrammarParser.PrimitiveExprHashASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprPrintAST(self, ctx: MonkeyGrammarParser.PrimitiveExprPrintASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprIfAST(self, ctx: MonkeyGrammarParser.PrimitiveExprIfASTContext):
        return self.visitChildren(ctx)

    def visitArrayFunctions(self, ctx: MonkeyGrammarParser.ArrayFunctionsContext):
        return self.visitChildren(ctx)

    def visitArrayLitetalAST(self, ctx: MonkeyGrammarParser.ArrayLitetalASTContext):
        self.visitChildren(ctx)
        array = []
        for i in range(0, len(self.replVisitor.stack)):
            array.append(self.replVisitor.stack.pop())

        #reverse array
        array.reverse()
        self.replVisitor.stack.append(array)

    def visitFunctionLiteralAST(self, ctx: MonkeyGrammarParser.FunctionLiteralASTContext):
        return self.visitChildren(ctx)

    def visitFunctionParametersAST(self, ctx: MonkeyGrammarParser.FunctionParametersASTContext):
        return self.visitChildren(ctx)

    def visitMoreIdentifiersAST(self, ctx: MonkeyGrammarParser.MoreIdentifiersASTContext):
        return self.visitChildren(ctx)

    def visitHashLiteralAST(self, ctx: MonkeyGrammarParser.HashLiteralASTContext):
        self.visitChildren(ctx)
        self.visitChildren(ctx)
        dicc = {}
        for i in range(0, len(self.replVisitor.stack), 2):
            value = self.replVisitor.stack.pop()
            key = self.replVisitor.stack.pop()

            if type(key) is str:
                key = key[1:-1]

            if type(value) is str:
                value = value[1:-1]

            dicc[key] = value

        #reverse dictionary
        dicc = dict(reversed(list(dicc.items())))

        self.replVisitor.stack.append(dicc)

    def visitHashContentAST(self, ctx: MonkeyGrammarParser.HashContentASTContext):
        return self.visitChildren(ctx)

    def visitMoreHashContentAST(self, ctx: MonkeyGrammarParser.MoreHashContentASTContext):
        return self.visitChildren(ctx)

    def visitExpressionListAST(self, ctx: MonkeyGrammarParser.ExpressionListASTContext):
        return self.visitChildren(ctx)

    def visitExpressionListEmptyAST(self, ctx: MonkeyGrammarParser.ExpressionListEmptyASTContext):
        return self.visitChildren(ctx)

    def visitMoreExpressionsAST(self, ctx: MonkeyGrammarParser.MoreExpressionsASTContext):
        return self.visitChildren(ctx)

    def visitPrintExpressionAST(self, ctx: MonkeyGrammarParser.PrintExpressionASTContext):
        try:

            self.visit(ctx.expression())
            self.consoleResult = str(self.replVisitor.stack.pop())
            print("print-> ", self.consoleResult)
        except:
            print("Error")
        return self.visitChildren(ctx)

    def visitIfExpressionAST(self, ctx: MonkeyGrammarParser.IfExpressionASTContext):
        self.visit(ctx.expression())
        flag=self.replVisitor.stack.pop()
        if flag == True:
            print("Entra al True")
            self.visit(ctx.blockStatement(0))
            return
        if flag == False :
            if ctx.blockStatement(1) != None:
                print("Entra al False")
                self.visit(ctx.blockStatement(1))

    def visitBlockStatementAST(self, ctx: MonkeyGrammarParser.BlockStatementASTContext):
        return self.visitChildren(ctx)

    def visitIdentifierAST(self, ctx: MonkeyGrammarParser.IdentifierASTContext):
        return ctx.getText()

    def visitBoolean(self, ctx:MonkeyGrammarParser.BooleanContext):
        token = ctx.getChild(0).symbol
        if token.text == "true":
            self.replVisitor.stack.append(True)
            print("es true")
        elif token.text == "false":
            self.replVisitor.stack.append(False)
            print("es false")
        return self.visitChildren(ctx)

    def visitCharAST(self, ctx: MonkeyGrammarParser.CharASTContext):
        return self.visitChildren(ctx)
