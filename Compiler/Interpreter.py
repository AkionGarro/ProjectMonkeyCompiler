from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor
from REPL import REPL, Frame


# from antlr4.CommonTokenFactory import CommonToken
level = 0
class MyVisitor(MonkeyGrammarVisitor):
    replVisitor = REPL()
    consoleResult = ""

    def visitProgramAST(self, ctx: MonkeyGrammarParser.ProgramASTContext, frame = None):
        for i in range(0, len(ctx.statement())):
            self.visit(ctx.statement(i))

    def visitStatementLetAST(self, ctx: MonkeyGrammarParser.StatementLetASTContext, frame = None):
        self.visit(ctx.letStatement())

    def visitStatementReturnAST(self, ctx: MonkeyGrammarParser.StatementReturnASTContext, frame = None):
        self.visit(ctx.returnStatement())

    def visitStatementExpressionAST(self, ctx: MonkeyGrammarParser.StatementExpressionASTContext, frame = None):
        self.visit(ctx.expressionStatement())

    def visitLetStatementAST(self, ctx: MonkeyGrammarParser.LetStatementASTContext, frame = None):
        varName = self.visit(ctx.identifier())
        self.visit(ctx.expression())
        self.replVisitor.data.add(varName, self.replVisitor.stack.pop())

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
                else:
                    print("No se permite este tipo de operacion en Str")

    def visitAdditionExpressionAST(self, ctx: MonkeyGrammarParser.AdditionExpressionASTContext, frame = None):
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())

    def visitAdditionFactorAST(self, ctx: MonkeyGrammarParser.AdditionFactorASTContext, frame = None):
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

    def visitMultiplicationExpressionAST(self, ctx: MonkeyGrammarParser.MultiplicationExpressionASTContext, frame = None):
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())

    def visitMultiplicationFactorAST(self, ctx: MonkeyGrammarParser.MultiplicationFactorASTContext, frame = None):
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

    def visitElementExpressionAST(self, ctx: MonkeyGrammarParser.ElementExpressionASTContext, frame = None):
        self.visit(ctx.primitiveExpression())
        if ctx.getChildCount() > 1:
            child = ctx.getChild(1).__class__.__name__
            if child == "CallExpressionASTContext":
                self.visit(ctx.callExpression())
                if frame == None:# si es none es porque es una llamada a una funcion desde el codigo principal, osea no es una funcion llamda dentro de otra funcion
                    funtionName = ctx.start.text
                    frame = self.replVisitor.data.get(funtionName)
                    print("frame: ", frame)
            else:
                self.visit(ctx.getChild(1))

    def visitElementAccessAST(self, ctx: MonkeyGrammarParser.ElementAccessASTContext, frame = None):
        self.visit(ctx.expression())
        key = self.replVisitor.stack.pop()
        hash = self.replVisitor.stack.pop()
        value = hash[key]
        self.replVisitor.stack.append(value)

    def visitCallExpressionAST(self, ctx: MonkeyGrammarParser.CallExpressionASTContext, frame = None):
        self.visit(ctx.expressionList())

    def visitPrimitiveExprDigitAST(self, ctx: MonkeyGrammarParser.PrimitiveExprDigitASTContext, frame = None):
        list1 = None
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
            list1 = self.replVisitor.stack.pop()
            list1.append(ctx.STRING().symbol.text)
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
                list1.append(object)
                self.replVisitor.stack.append(list1)
            except:
                self.replVisitor.stack.append(list1)
                self.replVisitor.stack.append(object)

        else:
            print("El identificador no existe")

        return self.visitChildren(ctx)

    def visitPrimitiveExprBooleanAST(self, ctx: MonkeyGrammarParser.PrimitiveExprBooleanASTContext, frame = None):
        self.visit(ctx.boolean())

    def visitPrimitiveExprBlockExprAST(self, ctx: MonkeyGrammarParser.PrimitiveExprBlockExprASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitPrimitiveExprArrLitAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrLitASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitPrimitiveExprArrFuncAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrFuncASTContext, frame = None):
        self.visitChildren(ctx)
        token = ctx.getChild(0).start.text
        id = ctx.getChild(2).start.text

        if token == "len":
            arr = self.replVisitor.stack.pop()
            self.replVisitor.stack.append(len(arr))

        elif token == "first":
            arr = self.replVisitor.stack.pop()
            if type(arr) == dict:
                self.replVisitor.stack.append(arr[next(iter(arr))])
            else:
                self.replVisitor.stack.append(arr[0])

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

            # reverse values
            values.reverse()

            for value in values:
                arr.append(value)

            self.replVisitor.data.add(id, arr)

    def visitPrimitiveExprFuncAST(self, ctx: MonkeyGrammarParser.PrimitiveExprFuncASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitPrimitiveExprHashAST(self, ctx: MonkeyGrammarParser.PrimitiveExprHashASTContext, frame = None):
        return self.visitChildren(ctx)

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

        if ctx.parentCtx == None:
            print("ctx: ", ctx.__class__.__name__)
            return
        else:
            name = ctx.__class__.__name__
            if name == "FunctionLiteralASTContext":
                print("ctx: ", ctx.__class__.__name__)
                self.find_let_fn(ctx.parentCtx)

            self.visitParents(ctx.parentCtx)
    def visitFunctionLiteralAST(self, ctx: MonkeyGrammarParser.FunctionLiteralASTContext, frame = None):
        print("\t-- Inicio de funcion --")
        self.visitParents(ctx)
        frame = Frame(ctx)
        print("\t-- Fin de funcion --\n")
        self.replVisitor.stack.append(frame)
    def visitFunctionParametersAST(self, ctx: MonkeyGrammarParser.FunctionParametersASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitMoreIdentifiersAST(self, ctx: MonkeyGrammarParser.MoreIdentifiersASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitHashLiteralAST(self, ctx: MonkeyGrammarParser.HashLiteralASTContext, frame = None):
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

        # reverse dictionary
        dicc = dict(reversed(list(dicc.items())))

        self.replVisitor.stack.append(dicc)

    def visitHashContentAST(self, ctx: MonkeyGrammarParser.HashContentASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitMoreHashContentAST(self, ctx: MonkeyGrammarParser.MoreHashContentASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitExpressionListAST(self, ctx: MonkeyGrammarParser.ExpressionListASTContext, frame = None):
        self.replVisitor.stack.append([])
        self.visitChildren(ctx)

        array = self.replVisitor.stack.pop()

        print("Array: ", array)
        self.replVisitor.stack.append(array)

    def visitExpressionListEmptyAST(self, ctx: MonkeyGrammarParser.ExpressionListEmptyASTContext, frame = None):
        self.replVisitor.stack.append([])


    def visitMoreExpressionsAST(self, ctx: MonkeyGrammarParser.MoreExpressionsASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitPrintExpressionAST(self, ctx: MonkeyGrammarParser.PrintExpressionASTContext, frame = None):

        try:
            self.visit(ctx.expression())
            info = self.replVisitor.stack.pop()
            print("Type: " + str(type(info)))
            if type(info) is str:
                info = info[1:-1]

            if type(self.consoleResult) == str and self.consoleResult == "":
                self.consoleResult = [info]
            else:
                self.consoleResult.append(info)
            print("print-> ", self.consoleResult)
        except:
            print("Error")

    def visitIfExpressionAST(self, ctx: MonkeyGrammarParser.IfExpressionASTContext, frame = None):
        self.visit(ctx.expression())
        flag = self.replVisitor.stack.pop()
        if flag == True:
            print("Entra al True")
            self.visit(ctx.blockStatement(0))
            return
        if flag == False:
            if ctx.blockStatement(1) != None:
                print("Entra al False")
                self.visit(ctx.blockStatement(1))

    def visitBlockStatementAST(self, ctx: MonkeyGrammarParser.BlockStatementASTContext, frame = None):
        return self.visitChildren(ctx)

    def visitIdentifierAST(self, ctx: MonkeyGrammarParser.IdentifierASTContext, frame = None):
        return ctx.getText()

    def visitBoolean(self, ctx: MonkeyGrammarParser.BooleanContext, frame = None):
        token = ctx.getChild(0).symbol
        if token.text == "true":
            var = True
            print("es true")
        elif token.text == "false":
            var = False
            print("es false")
        list1 = None
        try:
            list1 = self.replVisitor.stack.pop()
            list1.append(var)
            self.replVisitor.stack.append(list1)
        except:
            self.replVisitor.stack.append(list1)
            self.replVisitor.stack.append(var)
        return self.visitChildren(ctx)

    def visitCharAST(self, ctx: MonkeyGrammarParser.CharASTContext, frame = None):
        return self.visitChildren(ctx)