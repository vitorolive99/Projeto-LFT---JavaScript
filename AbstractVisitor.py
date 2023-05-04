from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass=ABCMeta):
    
    @abstractmethod
    def visitProgramFuncDecl(self, program):
        pass

    @abstractmethod
    def visitProgramVarDecl(self, program):
        pass

    @abstractmethod
    def visitProgramFuncDeclProgram(self, program):
        pass

    @abstractmethod
    def visitProgramVarDeclProgram(self, program):
        pass

    @abstractmethod
    def visitVarDecl(self, varDecl):
        pass

    @abstractmethod
    def visitVarDeclID(self, varDeclID):
        pass

    @abstractmethod
    def visitVarDeclIDExp(self, varDeclIDExp):
        pass

    @abstractmethod
    def visitVarDeclIDint (self, varDeclIDint):
        pass

    @abstractmethod
    def visitVarDeclListExp(self, varDeclListExp):
        pass

    @abstractmethod
    def visitVarDeclIntListExp(self, varDeclIntListExp):
        pass

    @abstractmethod
    def visitFuncDecl(self, funcDecl):
        pass

    @abstractmethod
    def visitFuncDeclSignatureBody(self, funcDeclSignatureBody):
        pass

    @abstractmethod
    def visitSignature(self, signature):
        pass

    @abstractmethod
    def visitSignatureIDSigParams(self, signatureIDSigParams):
        pass

    @abstractmethod
    def visitSigParams(self, sigParams):
        pass

    @abstractmethod
    def visitSingleSigParams(self, singleSigParams):
        pass

    @abstractmethod
    def visitCompoundSigParams(self, compoundSigParams):
        pass

    @abstractmethod
    def visitBody(self, body):
        pass

    @abstractmethod
    def visitBodyStms(self, bodyStms):
        pass

    @abstractmethod
    def visitBodyStm(self, bodyStm):
        pass

    @abstractmethod
    def visitBodyOrStm(self, bodyOrStm):
        pass

    @abstractmethod
    def visitBodyOrStmStm(self, bodyOrStmStm):
        pass

    @abstractmethod
    def visitStms(self, stms):
        pass

    @abstractmethod
    def visitSingleStm (self, singleStm):
        pass

    @abstractmethod
    def visitCompoundStm (self, compoundStm):
        pass

    @abstractmethod
    def visitStm (self, stm):
        pass

    @abstractmethod
    def visitStmVarDecl (self, stmVarDecl):
        pass

    @abstractmethod
    def visitStmExp (self, stmExp):
        pass

    @abstractmethod
    def visitStmWhile (self, stmWhile):
        pass

    @abstractmethod
    def visitStmReturn (self, stmReturn):
        pass

    @abstractmethod
    def visitStmIf (self, stmIf):
        pass

    @abstractmethod
    def visitStmIfElse (self, stmIfElse):
        pass

    @abstractmethod
    def visitStmFor (self, stmFor):
        pass

    @abstractmethod
    def visitExp (self, exp):
        pass

    @abstractmethod
    def visitSomaExp (self, somaExp):
        pass

    @abstractmethod
    def visitSubExp (self, subExp):
        pass

    @abstractmethod
    def visitMulExp (self, mulExp):
        pass

    @abstractmethod
    def visitDivExp (self, divExp):
        pass

    @abstractmethod
    def visitRestoExp (self, restoExp):
        pass

    @abstractmethod
    def visitIncrementoExp (self, incrementoExp):
        pass
    
    @abstractmethod
    def visitDecrementoExp (self, decrementoExp):
        pass

    @abstractmethod
    def visitExponencialExp (self, exponencialExp):
        pass

    @abstractmethod
    def visitIncrementoExp (self, incrementoExp):
        pass

    @abstractmethod
    def visitDecrementoExp (self, decrementoExp):
        pass

    @abstractmethod
    def visitMultIncrementoExp (self, multIncrementoExp):
        pass

    @abstractmethod
    def visitDivIncrementoExp (self, divIncrementoExp):
        pass

    @abstractmethod
    def visitRestoIncrementoExp (self, restoIncrementoExp):
        pass

    @abstractmethod
    def visitIgualExp (self, igualExp):
        pass

    @abstractmethod
    def visitIgualPraCaraiExp (self, igualPraCaraiExp):
        pass

    @abstractmethod
    def visitDiferenteExp (self, diferenteExp):
        pass

    @abstractmethod
    def visitDiferePraCaraiExp (self, diferePraCaraiExp):
        pass

    @abstractmethod
    def visitMaiorQExp (self, maiorQExp):
        pass

    @abstractmethod
    def visitMenorQExp (self, menorQExp):
        pass

    @abstractmethod
    def visitMenorIgualQExp (self, menorIgualQExp):
        pass

    @abstractmethod
    def visitAndExp (self, andExp):
        pass

    @abstractmethod
    def visitOrExp (self, orExp):
        pass

    @abstractmethod
    def visitNotExp (self, notExp):
        pass

    @abstractmethod
    def visitTernarioExp (self, ternarioExp):
        pass

    @abstractmethod
    def visitCallExp (self, callExp):
        pass

    @abstractmethod
    def visitAssignExp (self, assignExp):
        pass

    @abstractmethod
    def visitInteiroExp (self, inteiroExp):
        pass

    @abstractmethod
    def visitRealExp (self, realExp):
        pass

    @abstractmethod
    def visitIdExp (self, idExp):
        pass    
    
    @abstractmethod
    def visitStringExp (self, stringExp):
        pass

    @abstractmethod
    def visitTrueExp (self, trueExp):
        pass

    @abstractmethod
    def visitFalseExp (self, falseExp):
        pass

    @abstractmethod
    def visitOpexp (self, opexp):
        pass

    @abstractmethod
    def visitExpOpexp (self, expOpexp):
        pass
    
    @abstractmethod
    def visitVoidOpexp (self, voidOpexp):
        pass

    @abstractmethod
    def visitListExp (self, listExp):
        pass

    @abstractmethod
    def visitSingleListExp (self, singleListExp):
        pass

    @abstractmethod
    def visitCompoundListExp (self, compoundListExp):
        pass

    @abstractmethod
    def visitCall (self, call):
        pass

    @abstractmethod
    def visitParamsCall (self, paramsCall):
        pass

    @abstractmethod
    def visitNoParamsCall (self, noParamsCall):
        pass

    @abstractmethod
    def visitParams (self, params):
        pass

    @abstractmethod
    def visitSingleParams (self, singleParams):
        pass

    @abstractmethod
    def visitCompoundParams (self, compoundParams):
        pass

    @abstractmethod
    def visitAssign (self, assign):
        pass

    @abstractmethod
    def visitAssignAssign (self, assignAssign):
        pass
    
    