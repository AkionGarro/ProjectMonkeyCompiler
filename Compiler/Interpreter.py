from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor


# from antlr4.CommonTokenFactory import CommonToken
level = 0
class MyVisitor(MonkeyGrammarVisitor):
    replVisitor = REPL()
    consoleResult = ""
        self.consoleError += "\n"

    def addConsoleResult(self,msg):
        self.consoleResult += msg
        self.consoleResult += "\n"
    def visitProgramAST(self, ctx: MonkeyGrammarParser.ProgramASTContext):
        for i in range(0, len(ctx.statement())):
            self.visit(ctx.statement(i))

    def visitStatementLetAST(self, ctx: MonkeyGrammarParser.StatementLetASTContext, frame = None):
        self.visit(ctx.letStatement())

    def visitStatementReturnAST(self, ctx: MonkeyGrammarParser.StatementReturnASTContext):
        self.visit(ctx.returnStatement())

    def visitStatementExpressionAST(self, ctx: MonkeyGrammarParser.StatementExpressionASTContext):
        self.visit(ctx.expressionStatement())

    def visitLetStatementAST(self, ctx: MonkeyGrammarParser.LetStatementASTContext, frame = None):
    def visitLetStatementAST(self, ctx: MonkeyGrammarParser.LetStatementASTContext):
        varName = self.visit(ctx.identifier())
        self.visit(ctx.expression())

    def visitReturnStatementAST(self, ctx: MonkeyGrammarParser.ReturnStatementASTContext, frame = None):
        self.visit(ctx.expression())

    def visitExpressionStatementAST(self, ctx: MonkeyGrammarParser.ExpressionStatementASTContext, frame = None):
        self.visit(ctx.expression())


    def visitExpressionAST(self, ctx: MonkeyGrammarParser.ExpressionASTContext, frame = None):
        self.visit(ctx.additionExpression())
        self.visit(ctx.comparison())

    def visitComparisonAST(self, ctx: MonkeyGrammarParser.ComparisonASTContext, frame = None):
        index = 0

        for i in range(0, len(ctx.additionExpression())):
            self.visit(ctx.additionExpression(i))
            token = ctx.getChild(index).symbol
            index += 2
            op2 = (self.replVisitor.stack.pop())
            op1 = (self.replVisitor.stack.pop())
            if type(op2) == int:
                if token.text == "==":
                    flag = (op2 == op1)
                    self.replVisitor.stack.append(flag)
                elif token.text == "!=":
                    flag = (op2 != op1)
                    self.replVisitor.stack.append(flag)
                elif token.text == "<":
                    flag = (op1 < op2)
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
                op2 = (self.replVisitor.stack.pop())
                    if token.text == "==":
                        flagOperator = (op2 == op1)
                        self.replVisitor.stack.append(flagOperator)
                    elif token.text == "!=":
                        flagOperator = (op2 != op1)
                        self.replVisitor.stack.append(flagOperator)
                    elif token.text == "<":
                    elif token.text == "<=":
                        flagOperator = (op1 <= op2)
                        self.replVisitor.stack.append(flagOperator)
                    elif token.text == ">":
                else:
                    print("No se permite este tipo de operacion en Str")

    def visitAdditionExpressionAST(self, ctx: MonkeyGrammarParser.AdditionExpressionASTContext, frame = None):
                    elif token.text == "!=":
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())

    def visitAdditionFactorAST(self, ctx: MonkeyGrammarParser.AdditionFactorASTContext):
        index = 0
        flag = True

        for i in range(0, len(ctx.multiplicationExpression())):
            self.visit(ctx.multiplicationExpression(i))
            token = ctx.getChild(index).symbol
            index += 2
            try:

            if token.text == "+":
                self.replVisitor.stack.append(op1 + op2)
                self.replVisitor.stack.append(op1 - op2)

    def visitMultiplicationExpressionAST(self, ctx: MonkeyGrammarParser.MultiplicationExpressionASTContext, frame = None):
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())

    def visitMultiplicationFactorAST(self, ctx: MonkeyGrammarParser.MultiplicationFactorASTContext):
        index = 0
        flag = True
        for i in range(0, len(ctx.elementExpression())):
            self.visit(ctx.elementExpression(i))
            token = ctx.getChild(index).symbol
            index += 2
            op2 = (int)(self.replVisitor.stack.pop())
            op1 = (int)(self.replVisitor.stack.pop())
            try:

            if token.text == "*":
                self.replVisitor.stack.append(op1 * op2)
            elif token.text == "/":
                self.replVisitor.stack.append(op1 / op2)
            if flag == True:
                if token.text == "*":
                    self.replVisitor.stack.append((int)(op1 * op2))
                elif token.text == "/":
                    self.replVisitor.stack.append((int)(op1 / op2))

        self.visit(ctx.primitiveExpression())
        if ctx.getChildCount() > 1:
                    frame = self.replVisitor.data.get(funtionName)
            self.visit(ctx.getChild(1))

    def visitElementAccessAST(self, ctx: MonkeyGrammarParser.ElementAccessASTContext):
        self.visit(ctx.expression())
        key = self.replVisitor.stack.pop()
        hash = self.replVisitor.stack.pop()
        value = hash[key]
        self.replVisitor.stack.append(value)
                #self.addError("<ElementAccess> Error = (Indice debe ser int)")
                #flag = False
        except:
            self.addError("<ElementAccess> Error = (Error en la pila)")

    def visitCallExpressionAST(self, ctx: MonkeyGrammarParser.CallExpressionASTContext, frame = None):
        self.visit(ctx.expressionList())

        try:
            list1 = self.replVisitor.stack.pop()
            list1.append((int)(ctx.DIGIT().symbol.text))
            self.replVisitor.stack.append(list1)
        except:
            self.replVisitor.stack.append(list1)
            self.replVisitor.stack.append((int)(ctx.DIGIT().symbol.text))
        return self.visitChildren(ctx)

    def visitPrimitiveExprStringAST(self, ctx: MonkeyGrammarParser.PrimitiveExprStringASTContext, frame = None):
        list1 = None
        try:
            self.replVisitor.stack.append(list1)
        except:
            self.replVisitor.stack.append(list1)
            self.replVisitor.stack.append(ctx.STRING().symbol.text)

        return self.visitChildren(ctx)

    def visitPrimitiveExprIdAST(self, ctx: MonkeyGrammarParser.PrimitiveExprIdASTContext, frame = None):
        object = self.replVisitor.data.get(self.visit(ctx.identifier()))
        if (object != None):
            list1 = None
            try:
                list1 = self.replVisitor.stack.pop()
                self.replVisitor.stack.append(list1)
            except:
                self.replVisitor.stack.append(list1)
                self.replVisitor.stack.append(object)

        else:
            print("El identificador no existe")

        return self.visitChildren(ctx)

    def visitPrimitiveExprBooleanAST(self, ctx: MonkeyGrammarParser.PrimitiveExprBooleanASTContext, frame = None):
        self.visit(ctx.boolean())

        return self.visitChildren(ctx)
        self.visit(ctx.expression())

    def visitPrimitiveExprArrLitAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrLitASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitPrimitiveExprArrFuncAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrFuncASTContext, frame = None):
        self.visitChildren(ctx)
    def visitPrimitiveExprArrFuncAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrFuncASTContext):
        token = ctx.getChild(0).start.text
        id = ctx.getChild(2).start.text

        if token == "len":
            arr = self.replVisitor.stack.pop()
            self.replVisitor.stack.append(len(arr))
                arr = self.replVisitor.stack.pop()
                self.addError("<ArrFunc len> Error = (No se pudo realizar)")

        elif token == "first":
            arr = self.replVisitor.stack.pop()
            if type(arr) == dict:
            else:
            try:
                arr = self.replVisitor.stack.pop()
                arr = arr[0]
                if type(arr) == dict:
                    self.replVisitor.stack.append(arr[next(iter(arr))])
                else:

        elif token == "last":
            arr = self.replVisitor.stack.pop()

            if type(arr) == dict:
                self.replVisitor.stack.append(arr[list(arr)[-1]])
            else:
                self.replVisitor.stack.append(arr[-1])

                arr = self.replVisitor.stack.pop()
                arr= arr[0]
                if type(arr) == dict:
                    self.replVisitor.stack.append(arr[(int)(len(arr) - 1)])
                    self.replVisitor.stack.append(arr[-1])
            except:
                self.addError("<ArrFunc last> Error = (No se pudo realizar)")
        elif token == "rest":
                self.replVisitor.stack.append(list(arr.values())[1:])
            else:
                self.replVisitor.stack.append(list(arr.values())[1:])

        elif token == "push":

            values = []

            while len(self.replVisitor.stack) > 1:
                values.append(self.replVisitor.stack.pop())
                arr = self.replVisitor.stack.pop()
                element = arr[1]


            # reverse values

                arr.append(value)

    def visitPrimitiveExprHashAST(self, ctx: MonkeyGrammarParser.PrimitiveExprHashASTContext):
        self.visit(ctx.hashLiteral())

        self.visit(ctx.printExpression())

    def visitPrimitiveExprIfAST(self, ctx: MonkeyGrammarParser.PrimitiveExprIfASTContext):
        self.visit(ctx.ifExpression())

    def visitPrimitiveExprPrintAST(self, ctx: MonkeyGrammarParser.PrimitiveExprPrintASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitPrimitiveExprIfAST(self, ctx: MonkeyGrammarParser.PrimitiveExprIfASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitArrayFunctions(self, ctx: MonkeyGrammarParser.ArrayFunctionsContext, frame = None):
        return self.visitChildren(ctx)

    def visitArrayLitetalAST(self, ctx: MonkeyGrammarParser.ArrayLitetalASTContext, frame = None):
        self.visitChildren(ctx)
        array = []
        for i in range(0, len(self.replVisitor.stack)):
            array.append(self.replVisitor.stack.pop())
        array.reverse()
        self.replVisitor.stack.append(array)

    def find_let_fn(self, ctx):
        if ctx.parentCtx == None:
            return None
        else:
            if ctx.__class__.__name__ == "LetStatementASTContext":
                print("Funtion Name: ", ctx.start.text)
                return ctx
            else:
                return self.find_let_fn(ctx.parentCtx)
    def visitParents(self, ctx):
        # print ctx name
    def visitFunctionLiteralAST(self, ctx: MonkeyGrammarParser.FunctionLiteralASTContext):
        self.visit(ctx.functionParameters())
        self.visit(ctx.blockStatement())

            return
            if name == "FunctionLiteralASTContext":
                print("ctx: ", ctx.__class__.__name__)
                self.find_let_fn(ctx.parentCtx)

    def visitFunctionLiteralAST(self, ctx: MonkeyGrammarParser.FunctionLiteralASTContext, frame = None):
        print("\t-- Inicio de funcion --")
        self.visitParents(ctx)
        print("\t-- Fin de funcion --\n")
        self.replVisitor.stack.append(frame)
    def visitFunctionParametersAST(self, ctx: MonkeyGrammarParser.FunctionParametersASTContext):

    def visitMoreIdentifiersAST(self, ctx: MonkeyGrammarParser.MoreIdentifiersASTContext, frame = None):
        return self.visitChildren(ctx)

        self.visitChildren(ctx)
        self.visitChildren(ctx)
        dicc = {}
        for i in range(0, len(self.replVisitor.stack), 2):
            value = self.replVisitor.stack.pop()
            key = self.replVisitor.stack.pop()


            if type(value) is str:
                value = value[1:-1]
                if type(value) is str:
                    value = value[1:-1]

                dicc[key] = value
            except:
                self.addError("<Hashliteral> Error = (No se pudo realizar)")

        # reverse dictionary
        dicc = dict(reversed(list(dicc.items())))

        self.replVisitor.stack.append(dicc)


    def visitMoreHashContentAST(self, ctx: MonkeyGrammarParser.MoreHashContentASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitExpressionListAST(self, ctx: MonkeyGrammarParser.ExpressionListASTContext, frame = None):
        self.replVisitor.stack.append([])
        self.visitChildren(ctx)

    def visitMoreHashContentAST(self, ctx: MonkeyGrammarParser.MoreHashContentASTContext):
        for i in range(0,len(ctx.hashContent())):
            self.visit(ctx.hashContent(i))

    def visitExpressionListAST(self, ctx: MonkeyGrammarParser.ExpressionListASTContext):
        exprFull = []
        self.visit(ctx.expression())
        exprFull.append(self.replVisitor.stack.pop())
        self.visit(ctx.moreExpressions())
        moreExpression = self.replVisitor.stack.pop()
        for i in range(0,len(moreExpression)):
            exprFull.append(moreExpression[i])
        self.replVisitor.stack.append(exprFull)



    def visitExpressionListEmptyAST(self, ctx: MonkeyGrammarParser.ExpressionListEmptyASTContext):
        print("ExprListEmpty")

    def visitMoreExpressionsAST(self, ctx: MonkeyGrammarParser.MoreExpressionsASTContext):
        expr = []
        for i in range(0,len(ctx.expression())):
            self.visit(ctx.expression(i))
            expr.append(self.replVisitor.stack.pop())
        print(expr)
        self.replVisitor.stack.append(expr)

    def visitPrintExpressionAST(self, ctx: MonkeyGrammarParser.PrintExpressionASTContext):
        try:
            self.visit(ctx.expression())
            info = self.replVisitor.stack.pop()
            if type(info) is str:
                info = info[1:-1]
                self.addConsoleResult(info)
            else:
                self.addConsoleResult(str(info))
        except:
            self.addError("<PrintExpr> Error = (No se pudo realizar)")

    def visitIfExpressionAST(self, ctx: MonkeyGrammarParser.IfExpressionASTContext):
        self.visit(ctx.expression())

        try:
            flag = self.replVisitor.stack.pop()
            if flag == True:
                self.visit(ctx.blockStatement(0))
                return
            if flag == False:
                if ctx.blockStatement(1) != None:
                    self.visit(ctx.blockStatement(1))
        except:
            self.addError("<IfExpr> Error = (No se pudo realizar)")


    def visitBlockStatementAST(self, ctx: MonkeyGrammarParser.BlockStatementASTContext):
        for i in range(0,len(ctx.statement())):
            self.visit(ctx.statement(i))

    def visitIdentifierAST(self, ctx: MonkeyGrammarParser.IdentifierASTContext):
        return ctx.getText()

    def visitBoolean(self, ctx: MonkeyGrammarParser.BooleanContext):
        token = ctx.getChild(0).symbol
        if token.text == "true":
            self.replVisitor.stack.append(True)
        elif token.text == "false":
            self.replVisitor.stack.append(False)
        return self.visitChildren(ctx)

    def visitCharAST(self, ctx: MonkeyGrammarParser.CharASTContext):
        return ctx.getText()