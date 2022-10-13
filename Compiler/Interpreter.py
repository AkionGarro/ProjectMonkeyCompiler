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
        return self.visitChildren(ctx)

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
        return self.visitChildren(ctx)

    def visitFunctionLiteralAST(self, ctx: MonkeyGrammarParser.FunctionLiteralASTContext):
        return self.visitChildren(ctx)

    def visitFunctionParametersAST(self, ctx: MonkeyGrammarParser.FunctionParametersASTContext):
        return self.visitChildren(ctx)

    def visitMoreIdentifiersAST(self, ctx: MonkeyGrammarParser.MoreIdentifiersASTContext):
        return self.visitChildren(ctx)

    def visitHashLiteralAST(self, ctx: MonkeyGrammarParser.HashLiteralASTContext):
        return self.visitChildren(ctx)

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
            self.consoleResult = self.replVisitor.stack.pop()
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
