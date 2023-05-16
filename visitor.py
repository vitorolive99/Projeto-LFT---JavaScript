from AbstractVisitor import AbstractVisitor
from ExpressionLanguageSint import *

# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(AbstractVisitor):

    def visitProgramFuncDecl(self, program):
        program.funcdecl.accept(self)

    def visitProgramFuncDeclProgram(self, program):
        program.funcdecl.accept(self)
        program.program.accept(self)

    def visitProgramStms(self, program):
        program.stms.accept(self)

    def visitProgramStmsProgram(self, program):
        program.stms.accept(self)
        program.program.accept(self)

    def visitVarDeclID (self, varDeclID):
        varDeclID.type.accept(self)
        print(varDeclID.id, '; ', end='', sep='')

    def visitVarDeclIDExp (self, varDeclIDExp):
        varDeclIDExp.type.accept(self)
        print(varDeclIDExp.id, '= ', end='', sep='')
        varDeclIDExp.exp.accept(self)

    def visitVarDeclIDint (self, varDeclIDint):
        varDeclIDint.type.accept(self)
        print(varDeclIDint.id, ' ', end='', sep='')
        print('[',varDeclIDint.int, '] ', end='', sep='')

    def visitVarDeclListExp (self, varDeclListExp):
        varDeclListExp.type.accept(self)
        print(varDeclListExp.id, '= ', end='', sep='')
        varDeclListExp.listexp.accept(self)

    def visitVarDeclIntListExp (self, varDeclIntListExp):
        varDeclIntListExp.type.accept(self)
        print(varDeclIntListExp.id, ' ', end='', sep='')
        print('[',varDeclIntListExp.int, '] = ', end='', sep='')
        varDeclIntListExp.listexp.accept(self)

    def visitfuncDeclSignatureBody(self, signatureBody):
        signatureBody.signature.accept(self)
        signatureBody.body.accept(self)

    def visitSignatureIDsigParams(self, signatureIDSigParams):
        print('function ', signatureIDSigParams.id, ' (', end='', sep='')
        if signatureIDSigParams.sigParams is not None:
            signatureIDSigParams.sigParams.accept(self)
        print(') ', end='', sep='')

    def visitSingleSigParams(self, singleSigParams):
        print(singleSigParams.id, ' ', end='', sep='')

    def visitCompoundSigParams (self, compoundSigParams):
        print(compoundSigParams.id, ' ', end='', sep='')
        compoundSigParams.sigParams.accept(self)

    def visitbodystms(self, bodystms):
        global tab
        print ('{ ')
        tab = tab + 4
        if bodystms.stms is not None:
            bodystms.stms.accept(self)
        tab = tab - 4
        print ('} ')

    def visitSingleStm(self, SingleStm):
        SingleStm.stm.accept(self)

    def visitCompoundStm(self, CompoundStm):
        CompoundStm.stm.accept(self)
        CompoundStm.stms.accept(self)

    def visitStmExp(self, stmExp):
        print(blank(), end='', sep='')
        stmExp.exp.accept(self)
        print(';')

    def visitStmWhile(self, stmWhile):
        print(blank(),'while (', end='', sep='')
        stmWhile.exp.accept(self)
        print(') ', end='', sep='')
        stmWhile.body.accept(self)

    def visitReturn(self, Return):
        print(blank(),'return ', end='', sep='')
        Return.exp.accept(self)
        print(';')

    def visitStmIf(self, stmIf):
        print(blank(),'if (', end='', sep='')
        stmIf.exp.accept(self)
        print(') ', end='', sep='')
        stmIf.body.accept(self)

    def visitStmIfElse(self, stmIfElse):
        print(blank(),'if (', end='', sep='')
        stmIfElse.exp.accept(self)
        print(') ', end='', sep='')
        stmIfElse.body.accept(self)
        print(blank(),'else ', end='', sep='')
        stmIfElse.body2.accept(self)

    def visitStmFor(self, stmFor):
        print(blank(),'for (', end='', sep='')
        stmFor.exp1.accept(self)
        print('; ', end='', sep='')
        stmFor.exp2.accept(self)
        print('; ', end='', sep='')
        stmFor.exp3.accept(self)
        print(') ', end='', sep='')
        stmFor.body.accept(self)

    def visitExpVardecl(self, expVardecl):
        expVardecl.varDecl.accept(self)

    def visitSomaExp(self, somaExp):
        somaExp.exp1.accept(self)
        print(' + ', end='')
        somaExp.exp2.accept(self)

    def visitSubExp(self, subExp):
        subExp.exp1.accept(self)
        print(' - ', end='')
        subExp.exp2.accept(self)

    def visitMulExp(self, mulExp):
        mulExp.exp1.accept(self)
        print(' * ', end='')
        mulExp.exp2.accept(self)

    def visitDivExp(self, divExp):
        divExp.exp1.accept(self)
        print(' / ', end='')
        divExp.exp2.accept(self)

    def visitRestoExp(self, restoExp):
        restoExp.exp1.accept(self)
        print(' % ', end='')
        restoExp.exp2.accept(self)

    def visitIncrementoExp(self, incrementoExp):
        incrementoExp.exp.accept(self)
        print(' ++ ', end='')

    def visitIncrementoNExp(self, incrementoNExp):
        incrementoNExp.exp1.accept(self)
        print(' += ', end='')
        incrementoNExp.exp2.accept(self)

    def visitDecrementoExp(self, decrementoExp):
        decrementoExp.exp.accept(self)
        print(' --')

    def visitDecrementoNExp(self, decrementoNExp):
        decrementoNExp.exp1.accept(self)
        print(' -= ', end='')
        decrementoNExp.exp2.accept(self)

    def visitExponencialExp(self, exponencialExp):
        exponencialExp.exp1.accept(self)
        print(' ** ', end='')
        exponencialExp.exp2.accept(self)

    def visitIncrementNExp(self, incrementNExp):
        incrementNExp.exp1.accept(self)
        print(' += ', end='')
        incrementNExp.exp2.accept(self)

    def visitDecrementNExp(self, decrementNExp):
        decrementNExp.exp1.accept(self)
        print(' -= ', end='')
        decrementNExp.exp2.accept(self)

    def visitMultIncrementoExp(self, multIncrementoExp):
        multIncrementoExp.exp1.accept(self)
        print(' *= ', end='')
        multIncrementoExp.exp2.accept(self)

    def visitDivIncrementoExp(self, divIncrementoExp):
        divIncrementoExp.exp1.accept(self)
        print(' /= ', end='')
        divIncrementoExp.exp2.accept(self)

    def visitRestoIncrementoExp(self, restoIncrementoExp):
        restoIncrementoExp.exp1.accept(self)
        print(' %= ', end='')
        restoIncrementoExp.exp2.accept(self)

    def visitIgualExp(self, igualExp):
        igualExp.exp1.accept(self)
        print(' == ', end='')
        igualExp.exp2.accept(self)

    def visitigualpracaraiExp(self, igualpracaraiExp):
        igualpracaraiExp.exp1.accept(self)
        print(' === ', end='')
        igualpracaraiExp.exp2.accept(self)

    def visitDiferenteExp(self, diferenteExp):
        diferenteExp.exp1.accept(self)
        print(' != ', end='')
        diferenteExp.exp2.accept(self)

    def visitdiferentepracaraiExp(self, diferentepracaraiExp):
        diferentepracaraiExp.exp1.accept(self)
        print(' !== ', end='')
        diferentepracaraiExp.exp2.accept(self)

    def visitMaiorQExp(self, maiorQExp):
        maiorQExp.exp1.accept(self)
        print(' > ', end='')
        maiorQExp.exp2.accept(self)

    def visitMaiorIgualQExp(self, maiorIgualQExp):
        maiorIgualQExp.exp1.accept(self)
        print(' >= ', end='')
        maiorIgualQExp.exp2.accept(self)

    def visitMenorQExp(self, menorQExp):
        menorQExp.exp1.accept(self)
        print(' < ', end='')
        menorQExp.exp2.accept(self)

    def visitMenorIgualQExp(self, menorIgualQExp):
        menorIgualQExp.exp1.accept(self)
        print(' <= ', end='')
        menorIgualQExp.exp2.accept(self)

    def visitAndExp(self, andExp):
        andExp.exp1.accept(self)
        print(' && ', end='')
        andExp.exp2.accept(self)

    def visitOrExp(self, orExp):
        orExp.exp1.accept(self)
        print(' || ', end='')
        orExp.exp2.accept(self)

    def visitNotExp(self, notExp):
        print('!', end='')
        notExp.exp.accept(self)

    def visitTernarioExp(self, ternarioExp):
        ternarioExp.exp1.accept(self)
        print(' ? ', end='')
        ternarioExp.exp2.accept(self)
        print(' : ', end='')
        ternarioExp.exp3.accept(self)

    def visitAssignExp(self, assignExp):
        assignExp.assign.accept(self)

    def visitInteiroExp(self, iteiroExp):
        print(iteiroExp.inteiro, ' ', end='', sep='')

    def visitRealExp(self, realExp):
        print(realExp.real, ' ', end='', sep='')

    def visitIdExp(self, idExp):
        print(idExp.id, ' ', end='', sep='')

    def visitCallExp(self, callExp):
        callExp.id.accept(self)

    def visitBooleanExp(self, booleanExp):
        print(booleanExp.booleanValue, ' ', end='', sep='')

    def visitExpOpexp( self, expOpexp):
        expOpexp.exp.accept(self)

    def visitSingleListexp(self, listexp):
        listexp.exp.accept(self)

    def CompoundListexp(self, listexp):
        listexp.exp.accept(self)
        print(', ', end='')
        listexp.listexp.accept(self)

    def visitParamsCall(self, paramsCall):
        print(paramsCall.id, '(', end='', sep='')
        paramsCall.params.accept(self)
        print(')', end='')

    def visitNoParamsCall(self, paramsCall):
        print(blank(), paramsCall.id, '()',end='', sep='')

    def visitSingleParams(self, params):
        params.exp.accept(self)

    def visitCompoundParams(self, params):
        params.exp.accept(self)
        print(', ', end='')
        params.params.accept(self)

    def visitAssignAssign(self, assign):
        print(blank(), assign.id)
        print('=')
        assign.exp.accept(self)

    def visittipodecl(self, tipodecl):
        print(tipodecl.tipo, ' ',end='', sep='')

    def visitStringExp(self, stringExp):
        print(stringExp.stringd, ' ',end='', sep='')

    
    

if __name__ == "__main__":

    f = open("data.txt", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    print("#imprime o programa que foi passado como entrada")
    visitor = Visitor()
    for r in result:
        r.accept(visitor)