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

    def visitVarDeclID (self, varDeclID):
        varDeclID.id.accept(self)
        print(blank() + 'var ' + varDeclID.id + ';')

    def visitVarDeclIDExp (self, varDeclIDExp):
        varDeclIDExp.id.accept(self)
        varDeclIDExp.exp.accept(self)
        print(blank() + 'var ' + varDeclIDExp.id + ' = ' + varDeclIDExp.exp + ';')

    def visitVarDeclIDint (self, varDeclIDint):
        varDeclIDint.id.accept(self)
        varDeclIDint.int.accept(self)
        print(blank() + 'var ' + varDeclIDint.id + '[' + varDeclIDint.int + '];')

    def visitVarDeclListExp (self, varDeclListExp):
        varDeclListExp.id.accept(self)
        varDeclListExp.listexp.accept(self)
        print(blank() + 'var ' + varDeclListExp.id + ' = ' + varDeclListExp.listexp + ';')

    def visitVarDeclIntListExp (self, varDeclIntListExp):
        varDeclIntListExp.id.accept(self)
        varDeclIntListExp.int.accept(self)
        varDeclIntListExp.listexp.accept(self)
        print(blank() + 'var ' + varDeclIntListExp.id + '[' + varDeclIntListExp.int + '] = ' + varDeclIntListExp.listexp + ';')


    def visitVarDeclIDlistExplEmpty (self, varDeclIDlistExplEmpty):
        varDeclIDlistExplEmpty.id.accept(self)
        print(blank() + 'var ' + varDeclIDlistExplEmpty.id + '[];')

    def visitFuncDeclSignatureBody(self, funcDeclSignatureBody):
        funcDeclSignatureBody.signature.accept(self)
        funcDeclSignatureBody.body.accept(self)

    def visitSignatureIDSigParams(self, signatureIDSigParams):
        signatureIDSigParams.id.accept(self)
        signatureIDSigParams.sigparams.accept(self)
        print(blank() + 'function ' + signatureIDSigParams.id + '(' + signatureIDSigParams.sigparams + ')')

    def visitSingleSigParams(self, singleSigParams):
        singleSigParams.id.accept(self)
        print(singleSigParams.id)