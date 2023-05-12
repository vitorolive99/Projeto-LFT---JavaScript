from ExpressionLanguageSint import *

# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor():

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
        print(varDeclID.type, ' ', end='', sep='')
        print(varDeclID.id, ' ', end='', sep='')

    def visitVarDeclIDExp (self, varDeclIDExp):
        print(varDeclIDExp.type)
        print(varDeclIDExp.id)
        varDeclIDExp.exp.accept(self)

    def visitVarDeclIDint (self, varDeclIDint):
        print(varDeclIDint.type)
        print(varDeclIDint.id)
        print(varDeclIDint.int)

    def visitVarDeclListExp (self, varDeclListExp):
        print(varDeclListExp.type)
        print(varDeclListExp.id)
        varDeclListExp.listexp.accept(self)

    def visitVarDeclIntListExp (self, varDeclIntListExp):
        print(varDeclIntListExp.type)
        print(varDeclIntListExp.id)
        print(varDeclIntListExp.int)
        varDeclIntListExp.listexp.accept(self)

    def visitfuncDeclSignatureBody(self, signatureBody):
        signatureBody.signature.accept(self)
        signatureBody.body.accept(self)

    def visitSignatureIDsigParams(self, signatureIDSigParams):
        print(signatureIDSigParams.id)
        signatureIDSigParams.sigParams.accept(self)

    def visitSingleSigParams(self, singleSigParams):
        print(singleSigParams.id)

    def visitCompoundSigParams (self, compoundSigParams):
        print(compoundSigParams.id)
        compoundSigParams.sigParams.accept(self)

    def visitbodystms(self, bodystms):
        bodystms.stms.accept(self)

    def visitBodyOrStm(self, bodyOrStm):
        bodyOrStm.body.accept(self)

    def visitBodyOrStmStm(self, bodyOrStm):
        bodyOrStm.stm.accept(self)

    def visitSingleStm(self, SingleStm):
        SingleStm.stm.accept(self)

    def visitCompoundStm(self, CompoundStm):
        CompoundStm.stm.accept(self)
        CompoundStm.stms.accept(self)

    def visitStmExp(self, stmExp):
        stmExp.exp.accept(self)

    def visitStmWhile(self, stmWhile):
        stmWhile.exp.accept(self)
        stmWhile.bodyorstm.accept(self)

    def visitReturn(self, Return):
        Return.exp.accept(self)

    def visitStmIf(self, stmIf):
        stmIf.exp.accept(self)
        stmIf.bodyorstm.accept(self)

    def visitStmIfElse(self, stmIfElse):
        stmIfElse.exp.accept(self)
        stmIfElse.bodyorstm1.accept(self)
        stmIfElse.bodyorstm2.accept(self)

    def visitStmFor(self, stmFor):
        stmFor.exp1.accept(self)
        stmFor.exp2.accept(self)
        stmFor.exp3.accept(self)
        stmFor.bodyorstm.accept(self)

    def visitExpVardecl(self, expVardecl):
        expVardecl.vardecl.accept(self)

    def visitSomaExp(self, somaExp):
        somaExp.exp1.accept(self)
        print('+')
        somaExp.exp2.accept(self)

    def visitSubExp(self, subExp):
        subExp.exp1.accept(self)
        print('-')
        subExp.exp2.accept(self)

    def visitMulExp(self, mulExp):
        mulExp.exp1.accept(self)
        print('*')
        mulExp.exp2.accept(self)

    def visitDivExp(self, divExp):
        divExp.exp1.accept(self)
        print('/')
        divExp.exp2.accept(self)

    def visitRestoExp(self, restoExp):
        restoExp.exp1.accept(self)
        print('%')
        restoExp.exp2.accept(self)

    def visitIncrementoExp(self, incrementoExp):
        incrementoExp.exp.accept(self)
        print('++')

    def visitIncrementoNExp(self, incrementoNExp):
        incrementoNExp.exp1.accept(self)
        print('+=')
        incrementoNExp.exp2.accept(self)

    def visitDecrementoExp(self, decrementoExp):
        decrementoExp.exp.accept(self)
        print('--')

    def visitDecrementoNExp(self, decrementoNExp):
        decrementoNExp.exp1.accept(self)
        print('-=')
        decrementoNExp.exp2.accept(self)

    def visitExponencialExp(self, exponencialExp):
        exponencialExp.exp1.accept(self)
        print('**')
        exponencialExp.exp2.accept(self)

    def visitIncrementNExp(self, incrementNExp):
        incrementNExp.exp1.accept(self)
        print('+=')
        incrementNExp.exp2.accept(self)

    def visitDecrementNExp(self, decrementNExp):
        decrementNExp.exp1.accept(self)
        print('-=')
        decrementNExp.exp2.accept(self)

    def visitMultIncrementoExp(self, multIncrementoExp):
        multIncrementoExp.exp1.accept(self)
        print('*=')
        multIncrementoExp.exp2.accept(self)

    def visitDivIncrementoExp(self, divIncrementoExp):
        divIncrementoExp.exp1.accept(self)
        print('/=')
        divIncrementoExp.exp2.accept(self)

    def visitRestoIncrementoExp(self, restoIncrementoExp):
        restoIncrementoExp.exp1.accept(self)
        print('%=')
        restoIncrementoExp.exp2.accept(self)

    def visitIgualExp(self, igualExp):
        igualExp.exp1.accept(self)
        print('==')
        igualExp.exp2.accept(self)

    def visitigualpracaraiExp(self, igualpracaraiExp):
        igualpracaraiExp.exp1.accept(self)
        print('===')
        igualpracaraiExp.exp2.accept(self)

    def visitDiferenteExp(self, diferenteExp):
        diferenteExp.exp1.accept(self)
        print('!=')
        diferenteExp.exp2.accept(self)

    def visitdiferentepracaraiExp(self, diferentepracaraiExp):
        diferentepracaraiExp.exp1.accept(self)
        print('!==')
        diferentepracaraiExp.exp2.accept(self)

    def visitMaiorQExp(self, maiorQExp):
        maiorQExp.exp1.accept(self)
        print('>')
        maiorQExp.exp2.accept(self)

    def visitMaiorIgualQExp(self, maiorIgualQExp):
        maiorIgualQExp.exp1.accept(self)
        print('>=')
        maiorIgualQExp.exp2.accept(self)

    def visitMenorQExp(self, menorQExp):
        menorQExp.exp1.accept(self)
        print('<')
        menorQExp.exp2.accept(self)

    def visitMenorIgualQExp(self, menorIgualQExp):
        menorIgualQExp.exp1.accept(self)
        print('<=')
        menorIgualQExp.exp2.accept(self)

    def visitAndExp(self, andExp):
        andExp.exp1.accept(self)
        print('&&')
        andExp.exp2.accept(self)

    def visitOrExp(self, orExp):
        orExp.exp1.accept(self)
        print('||')
        orExp.exp2.accept(self)

    def visitNotExp(self, notExp):
        print('!')
        notExp.exp.accept(self)

    def visitTernarioExp(self, ternarioExp):
        ternarioExp.exp1.accept(self)
        print('?')
        ternarioExp.exp2.accept(self)
        print(':')
        ternarioExp.exp3.accept(self)

    def visitAssignExp(self, assignExp):
        assignExp.assign.accept(self)

    def visitInteiroExp(self, iteiroExp):
        print(iteiroExp.inteiro)

    def visitRealExp(self, realExp):
        print(realExp.real)

    def visitIdExp(self, idExp):
        print(idExp.id)

    def visitCallExp(self, callExp):
        callExp.id.accept(self)

    def visitBooleanExp(self, booleanExp):
        print(booleanExp.booleanValue)

    def visitExpOpexp( self, expOpexp):
        expOpexp.exp.accept(self)

    def visitSingleListexp(self, listexp):
        listexp.exp.accept(self)

    def CompoundListexp(self, listexp):
        listexp.exp.accept(self)
        print(',')
        listexp.listexp.accept(self)

    def visitParamsCall(self, paramsCall):
        print(paramsCall.id)
        paramsCall.params.accept(self)

    def visitNoParamsCall(self, paramsCall):
        print(paramsCall.id)
        print( '()')

    def visitSingleParams(self, params):
        params.exp.accept(self)

    def visitCompoundParams(self, params):
        params.exp.accept(self)
        print(', ')
        params.params.accept(self)

    def visitAssignAssign(self, assign):
        print(assign.id)
        print('=')
        assign.exp.accept(self)

    def visittipodecl(self, tipodecl):
        print(tipodecl.tipo)

    def visitStringExp(self, stringExp):
        print(stringExp.stringd)

    
    

if __name__ == "__main__":

    data2 = '''
    function some (a, b){ 
        a = 88 + 44; 
        b = 70; 
        sumparabola(1, 2, 3); 
        if (b==70){     
            while (true){ 
                c = 38; 
                sumparabola(5, true, false); 
                while (c){ 
                    sumparabola(5, true, true); 
                } 
            }
        } 
        soma(); 
        sumparabolac(2); 
        return true; 
    }
    '''

    f = open("data.txt", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    parser.parse(debug=False)
    print("#imprime o programa que foi passado como entrada")
    visitor = Visitor()
