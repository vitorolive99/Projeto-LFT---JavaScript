from abc import abstractmethod
from abc import ABCMeta

'''programa'''
class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ProgramFuncDecl(Program):
    def __init__(self, funcdecl):
        self.funcdecl = funcdecl

    def accept(self, visitor):
        return visitor.visitProgramFuncDecl(self)

'''declaracao de variaveis'''
class varDecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class varDeclID(varDecl):
    def __init__(self, type, id):
        self.type = type
        self.id = id

    def accept(self, visitor):
        return visitor.visitVarDeclID(self)
    
class varDeclIDexp(varDecl):
    def __init__(self, type, id, exp):
        self.type = type
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitVarDeclIDexp(self)
    
class varDeclIDint(varDecl):
    def __init__(self, type, id, int):
        self.type = type
        self.id = id
        self.int = int

    def accept(self, visitor):
        return visitor.visitVarDeclIDint(self)
    
class varDeclIDlistexp(varDecl):
    def __init__(self, type, id, listexp):
        self.type = type
        self.id = id
        self.listexp = listexp

    def accept(self, visitor):
        return visitor.visitVarDeclIDlistexp(self)
    
class varDeclIDintlistexp(varDecl):
    def __init__(self, type, id, int, listexp):
        self.type = type
        self.id = id
        self.int = int
        self.listexp = listexp

    def accept(self, visitor):
        return visitor.visitVarDeclIDintlistexp(self)
    
class varDeclIDlistexplempty(varDecl):
    def __init__(self, type, id):
        self.type = type
        self.id = id

    def accept(self, visitor):
        return visitor.visitVarDeclIDlistexplempty(self)

'''declaracao de funcoes'''

class funcDecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class funcDeclSignatureBody(funcDecl):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body

    def accept(self, visitor):
        return visitor.visitFuncDeclSignatureBody(self)
    
'''assinatura de funcoes'''

class signature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class signatureIDsigParams(signature):
    def __init__(self, id, sigParams):
        self.id = id
        self.sigParams = sigParams

    def accept(self, visitor):
        return visitor.visitSignatureIDsigParams(self)
    
'''parametros de funcoes'''

class sigParams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleSigParams(sigParams):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitSigParamsID(self)
    
class CompoundSigParams(sigParams):
    def __init__(self, id, sigParams):
        self.id = id
        self.sigParams = sigParams

    def accept(self, visitor):
        return visitor.visitSigParamsIDsigParams(self)
    
'''corpo de funcoes'''

class body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class bodystms(body):
    def __init__(self, stms):
        self.stms = stms

    def accept(self, visitor):
        return visitor.visitBodyLCHAVESstmsRCHAVES(self)

class bodystm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class BodyOrStm(body):
    def __init__(self, body):
        self.body = body

    def accept(self, visitor):
        return visitor.visitBodyOrStm(self)

class BodyOrStmStm(body):
    def __init__(self, stm):
        self.stm = stm

    def accept(self, visitor):
        return visitor.visitBodyOrStmStm(self)
'''comandos'''

class stms(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class singleStm(stms): 
    def __init__(self, stm):
        self.stm = stm

    def accept(self, visitor):
        return visitor.visitSingleStm(self)
    
class CompoundStm(stms):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms

    def accept(self, visitor):
        return visitor.visitCompoundStm(self)
    
'''comando'''

class stm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class StmVarDecl(stm):
    def __init__(self, varDecl):
        self.varDecl = varDecl

    def accept(self, visitor):
        return visitor.visitStmVarDecl(self)
    
class StmExp(stm):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitStmExp(self)

class StmWhile(stm):
    def __init__(self, exp, bodyorstm):
        self.exp = exp
        self.bodyorstm = bodyorstm

    def accept(self, visitor):
        return visitor.visitStmWhile(self)
class StmReturn(stm):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitStmReturn(self) 
    
class StmIf(stm):
    def __init__(self, exp, bodyorstm):
        self.exp = exp
        self.bodyorstm = bodyorstm

    def accept(self, visitor):
        return visitor.visitStmIf(self)
class StmIfElse(stm):
    def __init__(self, exp, bodyorstm1, bodyorstm2):
        self.exp = exp
        self.bodyorstm1 = bodyorstm1
        self.bodyorstm2 = bodyorstm2

    def accept(self, visitor):
        return visitor.visitStmIfElse(self)
class StmFor(stm):
    def __init__(self, exp1, exp2, exp3, bodyorstm):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.bodyorstm = bodyorstm

    def accept(self, visitor):
        return visitor.visitStmFor(self)
    
'''expressoes'''

class exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SomaExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitSomaExp(self)
    
class SubExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitSubExp(self)

class DivExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitDivExp(self)
        
class MultExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitMultExp(self)

class RestoExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitRestoExp(self)
    
class IncrementoExp(exp):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitIncrementoExp(self)
    
class DecrementoExp(exp):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitDecrementoExp(self)
    
class ExponecialExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitExponecialExp(self)
    
class IncrementoNExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitIncrementoExp(self)
    
class DecrementoNExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitDecrementoExp(self)
    
class MultIncrementoExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitMultIncrementoExp(self)
    
class DivIncrementoExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitDivIncrementoExp(self)

class RestoIncrementoExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitRestoIncrementoExp(self)

class IgualExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitIgualExp(self)
    
class igualpracaraiExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitigualpracaraiExp(self)
    
class DiferenteExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitDiferenteExp(self)
    
class diferentepracaraiExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitdiferentepracaraiExp(self)
    
class MaiorQExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitMaiorQExp(self)
    
class MaiorIgualQExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitMaiorIgualQExp(self)
    
class MenorQExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitMenorQExp(self)
    
class MenorIgualQExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitMenorIgualQExp(self)
    
class AndExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitAndExp(self)
    
class OrExp(exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitOrExp(self)
    
class NotExp(exp):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitNotExp(self)
    
class TernarioExp(exp):
    def __init__(self, exp1, exp2, exp3):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3

    def accept(self, visitor):
        return visitor.visitTernarioExp(self)
    
class AssignExp(exp):
    def __init__(self, assign):
        self.assign = assign

    def accept(self, visitor):
        return visitor.visitAssignExp(self)
    
class InteiroExp(exp):
    def __init__(self, inteiro):
        self.inteiro = inteiro

    def accept(self, visitor):
        return visitor.visitInteiroExp(self)

class RealExp(exp):
    def __init__(self, real):
        self.real = real

    def accept(self, visitor):
        return visitor.visitRealExp(self)
    
class IdExp(exp):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitIdExp(self)

class StringExp(exp):
    def __init__(self, string):
        self.string = string

    def accept(self, visitor):
        return visitor.visitStringExp(self)
    
class CallExp(exp):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitCallExp(self)
    
class BooleanExp(exp):
    def __init__(self, boolean):
        self.booleanValue = boolean

    def accept(self, visitor):
        return visitor.visitBooleanExp(self)

class Opexp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpOpexp(Opexp):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitExpOpexp(self)
    
class Listexp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleListexp(Listexp):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitSingleListexp(self)
    
class CompoundListexp(Listexp):
    def __init__(self, exp, listexp):
        self.exp = exp
        self.listexp = listexp

    def accept(self, visitor):
        return visitor.visitCompoundListexp(self)

'''chamar funcao'''

class Call(metaclass=ABCMeta):  
    @abstractmethod
    def accept(self, visitor):
        pass

class ParamsCall(Call):
    def __init__(self, id, params):
        self.id = id
        self.params = params

    def accept(self, visitor):
        return visitor.visitParamsCall(self)

class NoParamsCall(Call):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitNoParamsCall(self)
    
'''parametros'''

class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleParams(Params):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitSingleParams(self)
    
class CompoundParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params

    def accept(self, visitor):
        return visitor.visitCompoundParams(self)

'''atribuicao'''   
class Assign(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class AssignAssign(Assign):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitAssignAssign(self)
    
class tipoDecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class tipodecl(tipoDecl):
    def __init__(self, tipo):
        self.tipo = tipo

    def accept(self, visitor):
        return visitor.visittipodecl(self)
    
class String (metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class string(String):
    def __init__(self, string):
        self.string = string

    def accept(self, visitor):
        return visitor.visitstringD(self)
    
