from visitor import *
import symbolTable as st

def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT or type2 == st.FLOAT):
            return st.FLOAT
        else:
            return st.INT
    else:
        return None

class SemanticVisitor(AbstractVisitor):

    def __init__(self):
        self.printer = Visitor()

    def visitProgramFuncDecl(self, program):
        program.funcdecl.accept(self)

    def visitProgramVarDecl(self, program):
        program.vardecl.accept(self)

    def visitProgramFuncDeclProgram(self, program):
        program.funcdecl.accept(self)
        program.program.accept(self)

    def visitProgramVarDeclProgram(self, program):
        program.vardecl.accept(self)
        program.program.accept(self)

    def visitVarDeclID (self, varDeclID):
        return [varDeclID.type, varDeclID.id]

    def visitVarDeclIDExp (self, varDeclIDExp):
        return [varDeclIDExp.type, varDeclIDExp.id, varDeclIDExp.exp.accept(self)]

    def visitVarDeclIDint (self, varDeclIDint):
        return [varDeclIDint.type, varDeclIDint.id, varDeclIDint.int]

    def visitVarDeclListExp (self, varDeclListExp):
        return [varDeclListExp.type, varDeclListExp.id] + varDeclListExp.listexp.accept(self)

    def visitVarDeclIntListExp (self, varDeclIntListExp):
        return [varDeclIntListExp.type, varDeclIntListExp.id, varDeclIntListExp.int] + varDeclIntListExp.listexp.accept(self)
    
    def visitfuncDeclSignatureBody(self, signatureBody):
        signatureBody.signature.accept(self)
        signatureBody.body.accept(self)

    def visitSignatureIDsigParams(self, signatureIDSigParams):
        pass

    def visitSingleSigParams(self, singleSigParams):
        return [singleSigParams.id]

    def visitCompoundSigParams (self, compoundSigParams):
        return [compoundSigParams.id] + compoundSigParams.sigParams.accept(self)

    def visitbodystms(self, bodystms):
        if bodystms.stms != None:
            bodystms.stms.accept(self)

    def visitSingleStm(self, SingleStm):
        SingleStm.stm.accept(self)

    def visitCompoundStm(self, CompoundStm):
        CompoundStm.stm.accept(self)
        CompoundStm.stms.accept(self)

    def visitStmExp(self, stmExp):
        stmExp.exp.accept(self)

    def visitStmVarDecl(self, stmVarDecl):
        stmVarDecl.vardecl.accept(self)

    def visitStmWhile(self, stmWhile):
        typeExp = stmWhile.exp.accept(self)
        if (typeExp == None):
            print('\n\t[Erro] Expressao ', stmWhile.exp.accept(self.printer), 'invalida.', end='')
        stmWhile.body.accept(self)

    def visitReturn(self, Return):
        pass

    def visitStmIf(self, stmIf):
        typeExp = stmIf.exp.accept(self)
        if (typeExp == None):
            print('\n\t[Erro] Expressao ', stmIf.exp.accept(self.printer), 'invalida.', end='')
        stmIf.body.accept(self)

    def visitStmIfElse(self, stmIfElse):
        typeExp = stmIfElse.exp.accept(self)
        if (typeExp == None):
            print('\n\t[Erro] Expressao ', stmIfElse.exp.accept(self.printer), 'invalida.', end='')
        stmIfElse.body1.accept(self)
        stmIfElse.body2.accept(self)

    def visitStmFor(self, stmFor):
        typeExp1 = stmFor.exp1.accept(self)
        typeExp2 = stmFor.exp2.accept(self)
        typeExp3 = stmFor.exp3.accept(self)
        if (typeExp1 == None or typeExp2 == None or typeExp3 == None):
            print('\n\t[Erro] Uma das expressoes esta incorreta ', stmFor.exp1.accept(self.printer),stmFor.exp2.accept(self.printer), stmFor.exp3.accept(self.printer), 'invalida.', end='')

    def visitExpVardecl(self, expVardecl):
        expVardecl.varDecl.accept(self)

    def visitSomaExp(self, somaExp): #feito
        tipoexp1 = somaExp.exp1.accept(self)
        tipoexp2 = somaExp.exp2.accept(self)
        c = coercion(tipoexp1, tipoexp2)
        if (c == None):
            somaExp.accept(self.printer)
            print('\n\t[Erro] Soma invalida. A expressao ', end='')
            somaExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            somaExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
        return c

    def visitSubExp(self, subExp): #feito
        tipoexp1 = subExp.exp1.accept(self)
        tipoexp2 = subExp.exp2.accept(self)
        c = coercion(tipoexp1, tipoexp2)
        if (c == None):
            subExp.accept(self.printer)
            print('\n\t[Erro] Subtracao invalida. A expressao ', end='')
            subExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            subExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
        return c

    def visitMulExp(self, mulExp): #feito
        tipoexp1 = mulExp.exp1.accept(self)
        tipoexp2 = mulExp.exp2.accept(self)
        c = coercion(tipoexp1, tipoexp2)
        if (c == None):
            mulExp.accept(self.printer)
            print('\n\t[Erro] Multiplicacao invalida. A expressao ', end='')
            mulExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            mulExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
        return c

    def visitDivExp(self, divExp):  #feito
        tipoexp1 = divExp.exp1.accept(self)
        tipoexp2 = divExp.exp2.accept(self)
        c = coercion(tipoexp1, tipoexp2)
        if (c == None):
            divExp.accept(self.printer)
            print('\n\t[Erro] Divisao invalida. A expressao ', end='')
            divExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            divExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
        return c

    def visitRestoExp(self, restoExp): #feito   
        tipoexp1 = restoExp.exp1.accept(self)
        tipoexp2 = restoExp.exp2.accept(self)
        c = coercion(tipoexp1, tipoexp2)
        if (c == None):
            restoExp.accept(self.printer)
            print('\n\t[Erro] Resto invalido. A expressao ', end='')
            restoExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            restoExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
        return c

    def visitIncrementoExp(self, incrementoExp): #feito
        tipoexp = incrementoExp.exp.accept(self)
        if (tipoexp != st.Number):
            incrementoExp.accept(self.printer)
            print('\n\t[Erro] Incremento invalido. A expressao ', end='')
            incrementoExp.exp.accept(self.printer)
            print(' eh do tipo', tipoexp,'\n')
            return None
        return tipoexp

    def visitDecrementoExp(self, decrementoExp): #feito
        tipoexp = decrementoExp.exp.accept(self)
        if (tipoexp not in st.Number):
            decrementoExp.accept(self.printer)
            print('\n\t[Erro] Decremento invalido. A expressao ', end='')
            decrementoExp.exp.accept(self.printer)
            print(' eh do tipo', tipoexp,'\n')
            return None
        return tipoexp

    def visitExponencialExp(self, exponencialExp): #feito
        tipoexp1 = exponencialExp.exp1.accept(self)
        tipoexp2 = exponencialExp.exp2.accept(self)
        c = coercion(tipoexp1, tipoexp2)
        if (c == None):
            exponencialExp.accept(self.printer)
            print('\n\t[Erro] Exponencial invalido. A expressao ', end='')
            exponencialExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            exponencialExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
        return c

    def visitIncrementoNExp(self, incrementNExp): #feito
        tipoexp1 = incrementNExp.exp1.accept(self)
        tipoexp2 = incrementNExp.exp2.accept(self)
        c = coercion(tipoexp1, tipoexp2)
        if (c == None):
            incrementNExp.accept(self.printer)
            print('\n\t[Erro] Incremento invalido. A expressao ', end='')
            incrementNExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            incrementNExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
        return c

    def visitDecrementNExp(self, decrementNExp): #feito
        tipoexp1 = decrementNExp.exp1.accept(self)
        tipoexp2 = decrementNExp.exp2.accept(self)
        c = coercion(tipoexp1, tipoexp2)
        if (c == None):
            decrementNExp.accept(self.printer)
            print('\n\t[Erro] Decremento invalido. A expressao ', end='')
            decrementNExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            decrementNExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
        return c

    def visitMultIncrementoExp(self, multIncrementoExp): #feito
        tipoexp1 = multIncrementoExp.exp1.accept(self)
        tipoexp2 = multIncrementoExp.exp2.accept(self)
        c = coercion(tipoexp1, tipoexp2)
        if (c == None):
            multIncrementoExp.accept(self.printer)
            print('\n\t[Erro] Multiplicacao invalida. A expressao ', end='')
            multIncrementoExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            multIncrementoExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
        return c

    def visitDivIncrementoExp(self, divIncrementoExp): #feito
        tipoexp1 = divIncrementoExp.exp1.accept(self)
        tipoexp2 = divIncrementoExp.exp2.accept(self)
        c = coercion(tipoexp1, tipoexp2)
        if (c == None):
            divIncrementoExp.accept(self.printer)
            print('\n\t[Erro] Divisao invalida. A expressao ', end='')
            divIncrementoExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            divIncrementoExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
        return c

    def visitRestoIncrementoExp(self, restoIncrementoExp): #feito
        tipoexp1 = restoIncrementoExp.exp1.accept(self)
        tipoexp2 = restoIncrementoExp.exp2.accept(self)
        c = coercion(tipoexp1, tipoexp2)
        if (c == None):
            restoIncrementoExp.accept(self.printer)
            print('\n\t[Erro] Resto invalido. A expressao ', end='')
            restoIncrementoExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            restoIncrementoExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
        return c

    def visitIgualExp(self, igualExp): #feito, EU ACHO
        tipoexp1 = igualExp.exp1.accept(self)
        tipoexp2 = igualExp.exp2.accept(self)
        if (tipoexp1 != tipoexp2):
            igualExp.accept(self.printer)
            print('\n\t[Erro] Igualdade invalida. A expressao ', end='')
            igualExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            igualExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
            return None
        return tipoexp1

    def visitigualpracaraiExp(self, igualpracaraiExp): #feito, EU ACHO
        tipoexp1 = igualpracaraiExp.exp1.accept(self)
        tipoexp2 = igualpracaraiExp.exp2.accept(self)
        if (tipoexp1 != tipoexp2):
            igualpracaraiExp.accept(self.printer)
            print('\n\t[Erro] Igualdade invalida. A expressao ', end='')
            igualpracaraiExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            igualpracaraiExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
            return None
        return tipoexp1

    def visitDiferenteExp(self, diferenteExp): #feito, EU ACHO
        tipoexp1 = diferenteExp.exp1.accept(self)
        tipoexp2 = diferenteExp.exp2.accept(self)
        if (tipoexp1 != tipoexp2):
            diferenteExp.accept(self.printer)
            print('\n\t[Erro] Diferenca invalida. A expressao ', end='')
            diferenteExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            diferenteExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
            return None
        return tipoexp1

    def visitdiferentepracaraiExp(self, diferentepracaraiExp): #feito, EU ACHO
        tipoexp1 = diferentepracaraiExp.exp1.accept(self)
        tipoexp2 = diferentepracaraiExp.exp2.accept(self)
        if (tipoexp1 != tipoexp2):
            diferentepracaraiExp.accept(self.printer)
            print('\n\t[Erro] Diferenca invalida. A expressao ', end='')
            diferentepracaraiExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            diferentepracaraiExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
            return None
        return tipoexp1

    def visitMaiorQExp(self, maiorQExp): #feito, EU ACHO
        tipoexp1 = maiorQExp.exp1.accept(self)
        tipoexp2 = maiorQExp.exp2.accept(self)
        if (tipoexp1 != tipoexp2):
            maiorQExp.accept(self.printer)
            print('\n\t[Erro] Maior que invalido. A expressao ', end='')
            maiorQExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            maiorQExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
            return None
        return tipoexp1

    def visitMaiorIgualQExp(self, maiorIgualQExp): #feito, EU ACHO
        tipoexp1 = maiorIgualQExp.exp1.accept(self)
        tipoexp2 = maiorIgualQExp.exp2.accept(self)
        if (tipoexp1 != tipoexp2):
            maiorIgualQExp.accept(self.printer)
            print('\n\t[Erro] Maior igual que invalido. A expressao ', end='')
            maiorIgualQExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            maiorIgualQExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
            return None
        return tipoexp1

    def visitMenorQExp(self, menorQExp):
        tipoexp1 = menorQExp.exp1.accept(self)
        tipoexp2 = menorQExp.exp2.accept(self)
        if (tipoexp1 != tipoexp2):
            menorQExp.accept(self.printer)
            print('\n\t[Erro] Menor que invalido. A expressao ', end='')
            menorQExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            menorQExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
            return None
        return tipoexp1

    def visitMenorIgualQExp(self, menorIgualQExp):
        tipoexp1 = menorIgualQExp.exp1.accept(self)
        tipoexp2 = menorIgualQExp.exp2.accept(self)
        if (tipoexp1 != tipoexp2):
            menorIgualQExp.accept(self.printer)
            print('\n\t[Erro] Menor igual que invalido. A expressao ', end='')
            menorIgualQExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoexp1, 'enquanto a expressao ', end='')
            menorIgualQExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoexp2,'\n')
            return None
        return tipoexp1

    def visitAndExp(self, andExp): #feito, EU ACHO
        andExp.exp1.accept(self)
        andExp.exp2.accept(self)

    def visitOrExp(self, orExp): #feito, EU ACHO
        orExp.exp1.accept(self)
        orExp.exp2.accept(self)
        

    def visitNotExp(self, notExp): #feito, EU ACHO
        notExp.exp.accept(self)

    def visitTernarioExp(self, ternarioExp): #feito, EU ACHO
        ternarioExp.exp1.accept(self)
        ternarioExp.exp2.accept(self)
        ternarioExp.exp3.accept(self)

    def visitAssignExp(self, assignExp): #feito, EU ACHO
        assignExp.assign.accept(self)

    def visitInteiroExp(self, inteiroExp): #feito
        if (isinstance(inteiroExp.inteiro, int)):
            return st.INT
        
    def visitRealExp(self, realExp): #feito
        if (isinstance(realExp.real, float)):
            return st.FLOAT
        
    def visitIdExp(self, idExp): #feito
        idName = st.getBindable(idExp.id)
        if (idName != None):
            return idName[st.TYPE]
        return None

    def visitStringExp(self, stringExp): #feito, EU ACHO
        if (isinstance(stringExp.stringd, str)):
            return st.STRING

    def visitCallExp(self, callExp): #feito
        callExp.id.accept(self)

    def visitBooleanExp(self, booleanExp): #feito
        return st.BOOL

    def visitExpOpexp( self, expOpexp):
        expOpexp.exp.accept(self)

    def visitSingleListexp(self, listexp):
        listexp.exp.accept(self)

    def CompoundListexp(self, listexp):
        listexp.exp.accept(self)
        print(',')
        listexp.listexp.accept(self)

    def visitParamsCall(self, paramsCall): #feito
        pass

    def visitNoParamsCall(self, simpleCall): #feito
        pass

    def visitSingleParams(self, params): #feito
        return [params.exp.accept(self)]
    
    def visitCompoundParams(self, params): #feito
        return [params.exp.accept(self)] + params.params.accept(self)

    def visitAssignAssign(self, assign): #feito
        typeVar = assign.exp.accept(self)
        if (isinstance(assign.id, sa.IdExp)):
            st.addVar (assign.id.id, typeVar)
            return typeVar
        return None

    def visittipodecl(self, tipodecl):
        return tipodecl.type

    def visitstring(self, string):
        return string.string

    
    

def main():

    f = open("data2.txt", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    print("#imprime o programa que foi passado como entrada")
    svisitor = SemanticVisitor()
    for r in result:
        r.accept(svisitor)

if __name__ == "__main__":
    main()