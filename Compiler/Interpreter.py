from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor
from REPL import REPL, HashMap


# from antlr4.CommonTokenFactory import CommonToken

class MyVisitor(MonkeyGrammarVisitor):
    replVisitor = REPL()
    consoleResult = ""
    consoleError = ""
    returnFlag = False
    returns = []
    returnsExpr = []

    def addError(self, msg):
        self.consoleError += msg
        self.consoleError += "\n"

    def addConsoleResult(self, msg):
        self.consoleResult += msg
        self.consoleResult += "\n"

    def visitProgramAST(self, ctx: MonkeyGrammarParser.ProgramASTContext):
        len1 = len(ctx.statement())
        for i in range(0, len(ctx.statement())):
            self.visit(ctx.statement(i))

    def visitStatementLetAST(self, ctx: MonkeyGrammarParser.StatementLetASTContext):
        if self.returnFlag:
            self.returnFlag = False
            return
        self.visit(ctx.letStatement())

    def visitStatementReturnAST(self, ctx: MonkeyGrammarParser.StatementReturnASTContext):

        self.returnFlag = True
        # si es 1 es porque es un return vacio, sin nisiquiera un ;
        if len(ctx.children) == 1:
            if len(self.returns) > 0:
                self.returns[-1] = False
            if len(self.returnsExpr) > 0:
                self.returnsExpr[-1] = False
            return
        class_name = ctx.getChild(1).__class__.__name__

        # si es un return con un ; pero sin nada
        if class_name == "TerminalNodeImpl":
            if len(self.returns) > 0:
                self.returns[-1] = False
            if len(self.returnsExpr) > 0:
                self.returnsExpr[-1] = False
            return
        # si es un return que sí retorna
        elif class_name == "ReturnStatementASTContext":
            if len(self.returns) > 0:
                self.returns[-1] = True
            if len(self.returnsExpr) > 0:
                self.returnsExpr[-1] = False
            self.visit(ctx.getChild(1))

    def visitStatementExpressionAST(self, ctx: MonkeyGrammarParser.StatementExpressionASTContext):
        if self.returnFlag:
            self.returnFlag = False
            return
        self.visit(ctx.expressionStatement())

    def visitLetStatementAST(self, ctx: MonkeyGrammarParser.LetStatementASTContext):
        varName = self.visit(ctx.identifier())
        self.visit(ctx.expression())

        try:
            self.replVisitor.data.add(varName, self.replVisitor.stack.pop())
        except:
            self.addError("<LetExpresion>  Error = (Almacenar la variable)")

    def visitReturnStatementAST(self, ctx: MonkeyGrammarParser.ReturnStatementASTContext):
        self.visit(ctx.expression())

    def visitExpressionStatementAST(self, ctx: MonkeyGrammarParser.ExpressionStatementASTContext):
        self.visit(ctx.expression())

    def visitExpressionAST(self, ctx: MonkeyGrammarParser.ExpressionASTContext):
        self.returnsExpr.append(True)  # se asume que el exp siempre retorna
        self.visitChildren(ctx)
        if len(self.returnsExpr) > 0:
            if self.returnsExpr[-1] == False:
                self.addError("<Expression> Error = (La función no retorna nada)")

            self.returnsExpr.pop()

    def visitComparisonAST(self, ctx: MonkeyGrammarParser.ComparisonASTContext):
        index = 0
        flag = True
        for i in range(0, len(ctx.additionExpression())):
            self.visit(ctx.additionExpression(i))
            token = ctx.getChild(index).symbol
            index += 2
            try:
                op2 = (self.replVisitor.stack.pop())
                op1 = (self.replVisitor.stack.pop())
                if type(op1) != type(op2):
                    self.addError(
                        "<Comparison> Error = (Datos incompatibles)" + str(type(op1)) + " y " + str(type(op2)))
                    flag = False
            except:
                flag = False

            if flag == True:
                if type(op2) == int:
                    if token.text == "==":
                        flagOperator = (op2 == op1)
                        self.replVisitor.stack.append(flagOperator)
                    elif token.text == "!=":
                        flagOperator = (op2 != op1)
                        self.replVisitor.stack.append(flagOperator)
                    elif token.text == "<":
                        flagOperator = (op1 < op2)
                        self.replVisitor.stack.append(flagOperator)
                    elif token.text == "<=":
                        flagOperator = (op1 <= op2)
                        self.replVisitor.stack.append(flagOperator)
                    elif token.text == ">":
                        flagOperator = (op1 > op2)
                        self.replVisitor.stack.append(flagOperator)
                    elif token.text == ">=":
                        flagOperator = (op1 >= op2)
                        self.replVisitor.stack.append(flagOperator)
                    else:
                        self.addError("<Int Operation>  Error = (No existe el operador)")
                else:
                    if token.text == "==":
                        flagOperator = (op2 == op1)
                        self.replVisitor.stack.append(flagOperator)
                    elif token.text == "!=":
                        flagOperator = (op2 != op1)
                        self.replVisitor.stack.append(flagOperator)
                    else:
                        self.addError("<Str Operation>  Error = (No existe el operador)")

    def visitAdditionExpressionAST(self, ctx: MonkeyGrammarParser.AdditionExpressionASTContext):
        self.visitChildren(ctx)

    def visitAdditionFactorAST(self, ctx: MonkeyGrammarParser.AdditionFactorASTContext):
        index = 0

        for i in range(0, len(ctx.multiplicationExpression())):
            self.visit(ctx.multiplicationExpression(i))
            token = ctx.getChild(index).symbol
            index += 2
            opa1 = None
            opa2 = None

            try:
                op2 = (self.replVisitor.stack.pop())
                op1 = (self.replVisitor.stack.pop())
                opa2 = type(op2)
                opa1 = type(op1)

                if op1.__class__.__name__ == 'FunctionLiteralASTContext':
                    op1 = 1
                if op2.__class__.__name__ == 'FunctionLiteralASTContext':
                    op2 = 2
                # print(op2.__class__.__name__)
                if (type(op1) == str and type(op2) == str):
                    if token.text == "+":
                        flagOperator = (op1[0:-1] + op2[1:])
                        self.replVisitor.stack.append(flagOperator)
                    else:
                        self.addError("<Addition> Error = (No puede restar strings) " + op1 + " - " + op2)
                elif (type(op1) == int and type(op2) == int):
                    if token.text == "+":
                        self.replVisitor.stack.append(op1 + op2)
                    else:
                        self.replVisitor.stack.append(op1 - op2)
                elif (type(op1) == int and type(op2) == float):
                    if token.text == "+":
                        self.replVisitor.stack.append(float(op1) + op2)
                    else:
                        self.replVisitor.stack.append(float(op1) - op2)
                elif (type(op1) == float and type(op2) == int):
                    if token.text == "+":
                        self.replVisitor.stack.append(op1 + float(op2))
                    else:
                        self.replVisitor.stack.append(op1 - float(op2))
                elif (type(op1) == float and type(op2) == float):
                    if token.text == "+":
                        self.replVisitor.stack.append(op1 + op2)
                    else:
                        self.replVisitor.stack.append(op1 - op2)
                else:
                    print("-------------------------- aqui 1 ------------------------------------")
                    self.addError("<Addition> Error = (Datos incompatibles)" + str(type(op1)) + " y " + str(type(op2)))

            except:
                print("-------------------------- aqui 2 ------------------------------------")
                self.addError("<Addition> Error = (Error en la pila)")
                self.addError("<Addition> Error = (Datos incompatibles)" + opa1 + " y " + opa2)

    def visitMultiplicationExpressionAST(self, ctx: MonkeyGrammarParser.MultiplicationExpressionASTContext):
        self.visitChildren(ctx)

    def visitMultiplicationFactorAST(self, ctx: MonkeyGrammarParser.MultiplicationFactorASTContext):
        index = 0
        flag = True
        for i in range(0, len(ctx.elementExpression())):
            self.visit(ctx.elementExpression(i))
            token = ctx.getChild(index).symbol
            index += 2
            try:
                op2 = (self.replVisitor.stack.pop())
                op1 = (self.replVisitor.stack.pop())

                if type(op1) != int or type(op2) != int:
                    self.addError("<Multiplication> Error = (Solo se permite Int)")
                    flag = False
                if type(op1) != type(op2):
                    self.addError(
                        "<Multiplication> Error = (Datos incompatibles)" + str(type(op1)) + " y " + str(type(op2)))
                    flag = False
            except:
                self.addError("<Multiplication> Error = (Error en la pila)")
                flag = False

            if flag == True:
                if token.text == "*":
                    self.replVisitor.stack.append((int)(op1 * op2))
                elif token.text == "/":
                    self.replVisitor.stack.append((int)(op1 / op2))

    def getIndexes(self, ctx):
        if ctx.parentCtx == None:
            return [0]
        else:
            name_class = ctx.__class__.__name__
            if name_class == "FunctionLiteralASTContext":

                return [ctx.indice] + self.getIndexes(ctx.parentCtx)
            else:
                return [] + self.getIndexes(ctx.parentCtx)

    def getParamsNames(self, ctx):

        # Lista de nombres de parametros
        params = []
        param = ctx.getChild(0).start.text
        params.append(param)
        for i in range(1, len(ctx.children)):
            param = ctx.getChild(i).stop.text
            if param not in params:
                params.append(param)
        return params

    def ejecutarFuncion(self, ctx: MonkeyGrammarParser.FunctionLiteralASTContext, listParams):
        indices = self.getIndexes(ctx)
        if len(indices) > 1:
            indices = indices[1:]
        # Se crea un nuevo data para la llamada a la funcion
        data = HashMap()
        # Se obtiene el indice de la funcion
        indice_data = self.replVisitor.indice_datas

        list1 = ctx.functionParameters()
        if list1.children != None:
            # Se obtienen los nombres de los parametros
            cxt_params = self.getParamsNames(list1)
        else:
            cxt_params = []

        # Si  no coinciden los parametros se lanza un error porque  no se enviaron los parametros correctos
        if len(cxt_params) != len(listParams):
            self.addError("<Function> Error = (Cantidad de parametros incorrecta, se esperan " + str(
                len(cxt_params)) + " parametros, pero se enviaron " + str(len(listParams)) + ")")
            return
        # Se agregan los parametros a la tabla de simbolos
        for i in range(0, len(cxt_params)):
            data.add(cxt_params[i], listParams[i])

        # Se respalda el data actual
        data_aux = self.replVisitor.data

        # Se respaldan los indices de los data
        datas_indices_aux = self.replVisitor.datas_indices

        # Se agrega el nuevo data
        self.replVisitor.data = data

        # Se agregan los indices de los data
        self.replVisitor.datas_indices = indices

        # Se agrega el nuevo data a la lista de datas
        self.replVisitor.add_data(data)

        # Se asigna el indice de la llamada a la funcion, para que funciones hijos la puedan usar
        ctx.indice = indice_data

        # respaldos del return para el input

        returnFlag_aux = self.returnFlag
        #returnFlagPuts_aux = self.returnFlagPuts

        self.returnFlag = False
        #self.returnFlagPuts = None

        #self.activePuts_aux = self.activePuts
        #self.activePuts = False


        # Se ejecuta el bloque de la funcion
        self.visit(ctx.blockStatement())

        # Se restauran los respaldos
        self.returnFlag = returnFlag_aux
        #self.returnFlagPuts = returnFlagPuts_aux
        #self.activePuts = self.activePuts_aux

        # Se reestablece el data anterior
        self.replVisitor.data = data_aux

        # Se reestablecen los indices de los data
        self.replVisitor.datas_indices = datas_indices_aux

        # Se elimina el data llamada a la funcion
        self.replVisitor.del_data()

    def validarReturn(self, ctx):
        # verifica que después de ejecutada una función con return no quede basura en la pila
        if ctx.parentCtx == None:
            return
        else:
            name_class = ctx.__class__.__name__
            if name_class == "StatementExpressionASTContext":
                self.replVisitor.stack.pop()# se elimina el return de la pila porque no se va a usar
                return
            elif name_class == "StatementLetASTContex":
                return
            elif name_class == "StatementReturnASTContext":
                return
            elif name_class == "PrintExpressionASTContext":
                return
            elif name_class == "ExpressionASTContext":
                return
            else:
                self.validarReturn(ctx.parentCtx)
    def visitElementExpressionAST(self, ctx: MonkeyGrammarParser.ElementExpressionASTContext):
        self.visit(ctx.primitiveExpression())
        if ctx.getChildCount() > 1:
            ctxName = ctx.getChild(1).__class__.__name__
            if ctxName == "CallExpressionASTContext":
                self.visit(ctx.getChild(1))
                if ctx.getChild(1).getChild(1).__class__.__name__ == "ExpressionListEmptyASTContext":
                    ctx_funcion = self.replVisitor.stack.pop()
                    self.ejecutarFuncion(ctx_funcion, [])
                else:
                    parametros = self.replVisitor.stack.pop()
                    nombre_funcion = ctx.primitiveExpression().identifier().start.text

                    # se verifica si la funcion existe
                    object = self.replVisitor.data.get(nombre_funcion)

                    # Si el objeto no existe se busca en los datas padres de la funcion
                    if object == None:
                        indice_datas = self.replVisitor.datas_indices

                        for i in range(0, len(indice_datas)):
                            object = self.replVisitor.datas[indice_datas[i]].get(nombre_funcion)
                            if object != None:
                                break

                    if (object != None):
                        # Si el objeto es una funcion se ejecuta
                        ctx_funcion = self.replVisitor.stack.pop()
                        self.ejecutarFuncion(ctx_funcion, parametros)
                    else:
                        # Si no existe se lanza un error
                        self.addError("<CallFuntion> Error = (La función <<" + nombre_funcion + ">> no existe)")
                        return



                self.validarReturn(ctx)
            else:
                self.visit(ctx.getChild(1))

    def visitElementAccessAST(self, ctx: MonkeyGrammarParser.ElementAccessASTContext):
        flag = True
        self.visit(ctx.expression())
        try:
            key = self.replVisitor.stack.pop()
            hash = self.replVisitor.stack.pop()
            if type(key) is str:
                key = key[1:-1]

        except:
            self.addError("<ElementAccess> Error = (Error en la pila)")
            flag = False
        if flag == True:
            value = hash[key]
            self.replVisitor.stack.append(value)

    def visitCallExpressionAST(self, ctx: MonkeyGrammarParser.CallExpressionASTContext):

        self.visit(ctx.expressionList())

    def visitPrimitiveExprDigitAST(self, ctx: MonkeyGrammarParser.PrimitiveExprDigitASTContext):

        self.replVisitor.stack.append(int(ctx.getText()))

        return self.visitChildren(ctx)

    def visitPrimitiveExprDigitPointAST(self, ctx: MonkeyGrammarParser.PrimitiveExprDigitPointASTContext):
        self.replVisitor.stack.append(float(ctx.getText()))
        return self.visitChildren(ctx)

    def visitPrimitiveExprStringAST(self, ctx: MonkeyGrammarParser.PrimitiveExprStringASTContext):
        self.replVisitor.stack.append(ctx.start.text)
        return

    def visitPrimitiveExprIdAST(self, ctx: MonkeyGrammarParser.PrimitiveExprIdASTContext):
        try:
            identifier = ctx.identifier()
        except:
            print("Error")

        object = self.replVisitor.data.get(self.visit(identifier))

        # Si el objeto no existe se busca en los datas padres de la funcion
        if object == None:
            indice_datas = self.replVisitor.datas_indices

            for i in range(0, len(indice_datas)):
                object = self.replVisitor.datas[indice_datas[i]].get(self.visit(identifier))
                if object != None:
                    break

        if (object != None):
            self.replVisitor.stack.append(object)
        else:
            self.addError("<PrimitiveExprId> Error = (No se encuentra el id <<" + str(self.visit(identifier)) + ">>)")
        return self.visitChildren(ctx)

    def visitPrimitiveExprBooleanAST(self, ctx: MonkeyGrammarParser.PrimitiveExprBooleanASTContext):
        self.visit(ctx.boolean())

    def visitPrimitiveExprBlockExprAST(self, ctx: MonkeyGrammarParser.PrimitiveExprBlockExprASTContext):
        self.visit(ctx.expression())

    def visitPrimitiveExprArrLitAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrLitASTContext):
        self.visit(ctx.arrayLiteral())

    def visitPrimitiveExprArrFuncAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrFuncASTContext):
        name = self.visit(ctx.expressionList())
        token = ctx.getChild(0).start.text
        id = ctx.getChild(2).start.text

        if token == "len":
            try:
                arr = self.replVisitor.stack.pop()
                arr = arr[0]
                lng = len(arr)
                self.replVisitor.stack.append(lng)
            except:
                self.addError("<ArrFunc len> Error = (No se pudo realizar)")

        elif token == "first":
            try:
                arr = self.replVisitor.stack.pop()
                arr = arr[0]
                if type(arr) == dict:
                    self.replVisitor.stack.append(arr[next(iter(arr))])
                else:
                    self.replVisitor.stack.append(arr[0])
            except:
                self.addError("<ArrFunc first> Error = (No se pudo realizar)")

        elif token == "last":
            try:
                arr = self.replVisitor.stack.pop()
                arr = arr[0]
                if type(arr) == dict:
                    self.replVisitor.stack.append(arr[(int)(len(arr) - 1)])
                else:
                    self.replVisitor.stack.append(arr[-1])
            except:
                self.addError("<ArrFunc last> Error = (No se pudo realizar)")
        elif token == "rest":
            try:
                arr = self.replVisitor.stack.pop()
                arr = arr[0]
                if type(arr) == dict:
                    self.replVisitor.stack.append(arr[1:])
                else:
                    self.replVisitor.stack.append(arr[1:])
            except:
                self.addError("<ArrFunc rest> Error = (No se pudo realizar)")

        elif token == "push":
            try:
                values = []

                while len(self.replVisitor.stack) > 1:
                    values.append(self.replVisitor.stack.pop())

                arr = self.replVisitor.stack.pop()
                element = arr[1]
                arr = arr[0]
                arr.append(element)
                # reverse values
                values.reverse()

                for value in values:
                    arr.append(value)

                self.replVisitor.data.add(id, arr)
            except:
                self.addError("<ArrFunc push> Error = (No se pudo realizar)")

    def visitPrimitiveExprFuncAST(self, ctx: MonkeyGrammarParser.PrimitiveExprFuncASTContext):

        self.visit(ctx.functionLiteral())

    def visitPrimitiveExprHashAST(self, ctx: MonkeyGrammarParser.PrimitiveExprHashASTContext):
        self.visit(ctx.hashLiteral())

    def visitPrimitiveExprPrintAST(self, ctx: MonkeyGrammarParser.PrimitiveExprPrintASTContext):
        self.visit(ctx.printExpression())

    def visitPrimitiveExprIfAST(self, ctx: MonkeyGrammarParser.PrimitiveExprIfASTContext):
        self.visit(ctx.ifExpression())

    def visitArrayFunctions(self, ctx: MonkeyGrammarParser.ArrayFunctionsContext):
        return self.visitChildren(ctx)

    def visitArrayLitetalAST(self, ctx: MonkeyGrammarParser.ArrayLitetalASTContext):
        self.visit(ctx.expressionList())
        exprFull = self.replVisitor.stack.pop()
        self.replVisitor.stack.append(exprFull)

    def visitFunctionLiteralAST(self, ctx: MonkeyGrammarParser.FunctionLiteralASTContext):
        self.replVisitor.stack.append(ctx)
        # self.visit(ctx.functionParameters())
        # self.visit(ctx.blockStatement())

    def visitFunctionParametersAST(self, ctx: MonkeyGrammarParser.FunctionParametersASTContext):
        self.visit(ctx.identifier())
        self.visit(ctx.moreIdentifiers())

    def visitMoreIdentifiersAST(self, ctx: MonkeyGrammarParser.MoreIdentifiersASTContext):
        for i in range(0, len(ctx.identifier())):
            self.visit(ctx.identifier(i))

    def visitHashLiteralAST(self, ctx: MonkeyGrammarParser.HashLiteralASTContext):

        dicc = {}
        self.visit(ctx.hashContent())
        try:
            value = self.replVisitor.stack.pop()
            key = self.replVisitor.stack.pop()

            if type(key) is str:
                key = key[1:-1]

            if type(value) is str:
                value = value[1:-1]

            dicc[key] = value
        except:
            self.addError("<Hashliteral> Error = (No se pudo realizar)")

        self.visit(ctx.moreHashContent())
        moreHash = self.replVisitor.stack.pop()
        for key, value in moreHash.items():
            dicc[key] = value
        self.replVisitor.stack.append(dicc)

    def visitHashContentAST(self, ctx: MonkeyGrammarParser.HashContentASTContext):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))

    def visitMoreHashContentAST(self, ctx: MonkeyGrammarParser.MoreHashContentASTContext):
        dicc = {}
        for i in range(0, len(ctx.hashContent())):
            self.visit(ctx.hashContent(i))
            try:
                value = self.replVisitor.stack.pop()
                key = self.replVisitor.stack.pop()

                if type(key) is str:
                    key = key[1:-1]

                if type(value) is str:
                    value = value[1:-1]

                dicc[key] = value
            except:
                self.addError("<Hashliteral> Error = (No se pudo realizar)")

                # reverse dictionary
        dicc = dict(reversed(list(dicc.items())))
        self.replVisitor.stack.append(dicc)

    def visitExpressionListAST(self, ctx: MonkeyGrammarParser.ExpressionListASTContext):
        exprFull = []
        self.visit(ctx.expression())
        exprFull.append(self.replVisitor.stack.pop())
        self.visit(ctx.moreExpressions())
        moreExpression = self.replVisitor.stack.pop()
        for i in range(0, len(moreExpression)):
            exprFull.append(moreExpression[i])
        self.replVisitor.stack.append(exprFull)

    def visitExpressionListEmptyAST(self, ctx: MonkeyGrammarParser.ExpressionListEmptyASTContext):
        return

    def visitMoreExpressionsAST(self, ctx: MonkeyGrammarParser.MoreExpressionsASTContext):
        expr = []
        for i in range(0, len(ctx.expression())):
            self.visit(ctx.expression(i))
            expr.append(self.replVisitor.stack.pop())
        self.replVisitor.stack.append(expr)

    def visitPrintExpressionAST(self, ctx: MonkeyGrammarParser.PrintExpressionASTContext):
        self.returns.append(False) # se asume que el print nunca retorna
        try:
            self.visit(ctx.expressionList())
            info = self.replVisitor.stack.pop()
            res = ""
            for i in range(0, len(info)):
                if type(info[i]) is str:
                    if info[i][0] == '"':
                        res += info[i][1:-1] + " "
                    else:
                        res += info[i] + " "
                else:
                    res += str(info[i]) + " "
            self.addConsoleResult(res)
        except:
            if len(self.returns) > 0:
                if self.returns[-1] == False:
                    self.addError("<Print> Error = (La función no retorna nada)")
                else:
                    self.addError("<Print> Error = (No se pudo realizar)")

                self.returns.pop()
            else:
                self.addError("<Print> Error = (No se pudo realizar)")

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
        for i in range(0, len(ctx.statement())):
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
