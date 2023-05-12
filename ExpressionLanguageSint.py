# Rascunho da gramatica
# program → funcdecl | funcdecl program | stms | stms program
# vardecl → tipodecl ID | tipodecl ID = exp | tipodecl ID [ INTEIRO ] | tipodecl ID = [ listexp ] | tipodecl ID [ INTEIRO ] = listexp | tipodecl ID = []
# funcdecl → signature body
# signature → FUNCTION ID ( sigParams )
# sigparams → ID |  ID , sigparams
# body → { stms }
# stms → stm | stm stms
# stm → exp ;  | while ( exp ) bodyorstm | return exp ; | if ( exp ) bodyorstm | if ( exp ) bodyorstm else bodyorstm | for ( opexp;opexp;opexp ) bodyorstm 
# opexp → exp | VOID
# bodyorstm → body | stm
# exp → exp + exp | exp - exp | exp / exp | exp * exp | exp % exp | exp ++ |exp ** exp | exp -- | exp += exp | exp -= exp | exp *= exp | exp /= exp| exp %= exp | exp == exp | exp === exp | exp != exp | exp !== exp | exp > exp | exp < exp | exp <= exp | exp >= exp | exp && exp | exp || exp | !exp | exp ? exp : exp | call | assign | INTEIRO | FLOAT | ID | TRUE | FALSE | vardecl | STRING
# call → ID (params) | ID ( )
# params → exp, params | exp
# assign → ID = exp
# tipodecl → LET | VAR | CONST
# listexp →  exp | exp , listexp 
import ply.lex as lex
import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa

precedence = (
    ('left', 'VIRGULA'),
    ('right', 'ATRIBUICAO', 'INCREMENTN', 'DECREMENTN', 'MULTINCREMENT', 'DIVINCREMENT', 'RESTOINCREMENT'),
    ('right', 'TERNARIO1', 'TERNARIO2'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUAL', 'DIFERENTE', 'IGUALPACARAI', 'DIFERENTEPACARAI'),
    ('left', 'MENORQ', 'MENORIGUALQ', 'MAIORQ', 'MAIORIGUALQ', 'IN', 'INSTANCEOF'),
    ('left', 'SOMA', 'SUB'),
    ('left', 'MULT', 'DIV', 'RESTO'),
    ('right', 'EXPONENCIACAO'),
    ('right', 'DECREMENT', 'INCREMENT', 'NEGACAO'),
    ('nonassoc', 'LPAREN', 'RPAREN')
)

def p_program(p):
    '''program : funcdecl'''
    p[0] = sa.ProgramFuncDecl(p[1])

def p_program1(p):
    '''program : funcdecl program'''
    p[0] = sa.programFuncDeclProgram(p[1], p[2])

def p_program2(p):
    '''program : stms'''
    p[0] = sa.programStms(p[1])

def p_program3(p):
    '''program : stms program'''
    p[0] = sa.programStmsProgram(p[1], p[2])

def p_vardecl(p):
    '''vardecl : tipodecl ID
               | tipodecl ID ATRIBUICAO exp
               | tipodecl ID LCOLCHETE INTEIRO RCOLCHETE
               | tipodecl ID ATRIBUICAO LCOLCHETE listexp RCOLCHETE
               | tipodecl ID LCOLCHETE INTEIRO RCOLCHETE ATRIBUICAO listexp'''
    if len(p) == 3:
        p[0] = sa.varDeclID(p[1], p[2])
    elif len(p) == 5:
        p[0] = sa.varDeclIDexp(p[1], p[2], p[4])
    elif len(p) == 6:
        p[0] = sa.varDeclIDint(p[1], p[2], p[4])
    elif len(p) == 7:
        p[0] = sa.varDeclIDlistexp(p[1], p[2], p[5])
    elif len(p) == 8:
        p[0] = sa.varDeclIDintlistexp(p[1], p[2], p[4], p[6])
    
def p_vardecl1(p):
    '''vardecl : tipodecl ID ATRIBUICAO LCOLCHETE RCOLCHETE'''
    p[0] = sa.varDeclIDlistexp(p[1], p[2], None)

def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = sa.funcDeclSignatureBody(p[1], p[2])
    

def p_signature(p):
    '''signature : FUNCTION ID LPAREN sigParams RPAREN'''
    p[0] = sa.signatureIDsigParams(p[2], p[4])

def p_sigParams(p):
    '''sigParams : ID
                 | ID VIRGULA sigParams'''
    if len(p) == 2:
        p[0] = sa.SingleSigParams(p[1])
    else:
        p[0] = sa.CompoundSigParams(p[1], p[3])

def p_body(p): 
    '''body : LCHAVES stms RCHAVES'''
    p[0] = sa.bodystms(p[2])

def p_stms(p):
    '''stms : stm
            | stm stms'''
    if len(p) == 2:
        p[0] = sa.singleStm(p[1])
    else:
        p[0] = sa.CompoundStm(p[1], p[2])

def p_stm(p):
    '''stm : RETURN exp PV'''
    p[0] = sa.StmReturn(p[2])
    
def p_stm1(p):
    '''stm : exp PV'''
    p[0] = sa.StmExp(p[1])

def p_stmWhile(p):
    '''stm : WHILE LPAREN exp RPAREN bodyorstm'''
    p[0] = sa.StmWhile(p[3], p[5])

def p_stmFor(p):
    '''stm : FOR LPAREN opexp PV opexp PV opexp RPAREN bodyorstm'''
    p[0] = sa.StmFor(p[3], p[5], p[7], p[9])

def p_stmIfElse(p):
    '''stm : IF LPAREN exp RPAREN bodyorstm ELSE bodyorstm'''
    p[0] = sa.StmIfElse(p[3], p[5], p[7])

def p_opexpIf(p):
    '''stm : IF LPAREN exp RPAREN bodyorstm'''
    p[0] = sa.StmIf(p[3], p[5])

def p_opexp(p):
    '''opexp : exp
             | VOID'''
    if isinstance(p[1], sa.exp):
        p[0] = sa.ExpOpexp(p[1])
    else:
        p[0] = sa.ExpOpexp(None)
    

def p_bodyorstm(p):
    '''bodyorstm : body
                 | stm'''
    if isinstance(p[1], sa.body):
        p[0] = sa.BodyOrStm(p[1])
    else:
        p[0] = sa.BodyOrStmStm(p[1])


def p_expVardecl(p):
    '''exp : vardecl'''
    p[0] = sa.ExpVarDecl(p[1])

def p_expSoma(p):
    '''exp : exp SOMA exp'''
    p[0] = sa.SomaExp(p[1], p[3])
    
def p_expBoolean(p):
    '''exp : FALSE
           | TRUE'''
    p[0] = sa.BooleanExp(p[1])

def p_expId(p):
    '''exp : ID'''
    p[0] = sa.IdExp(p[1])

def p_expFloat(p):
    '''exp : FLOAT'''
    p[0] = sa.RealExp(p[1])

def p_expInt(p):
    '''exp : INTEIRO'''
    p[0] = sa.InteiroExp(p[1])

def p_expAssign(p):
    '''exp : assign'''
    p[0] = sa.AssignExp(p[1])

def p_expCall(p):
    '''exp : call'''
    p[0] = sa.CallExp(p[1])

def p_expTernario(p):
    '''exp : exp TERNARIO1 exp TERNARIO2 exp'''
    p[0] = sa.TernarioExp(p[1], p[3], p[5])

def p_expNegacao(p):
    '''exp : NEGACAO exp'''
    p[0] = sa.NotExp(p[2])

def p_expOr(p):
    '''exp : exp OR exp'''
    p[0] = sa.OrExp(p[1], p[3])

def p_expAnd(p):
    '''exp : exp AND exp'''
    p[0] = sa.AndExp(p[1], p[3])

def p_expMaiorIgual(p):
    '''exp : exp MAIORIGUALQ exp'''
    p[0] = sa.MaiorIgualQExp(p[1], p[3])

def p_expMenorIgual(p):
    '''exp : exp MENORIGUALQ exp'''
    p[0] = sa.MenorIgualQExp(p[1], p[3])

def p_expMenorQ(p):
    '''exp : exp MENORQ exp'''
    p[0] = sa.MenorQExp(p[1], p[3])

def p_expMaiorQ(p):
    '''exp : exp MAIORQ exp'''
    p[0] = sa.MaiorQExp(p[1], p[3])

def p_expDiferentePacarai(p):
    '''exp : exp DIFERENTEPACARAI exp'''
    p[0] = sa.diferentepracaraiExp(p[1], p[3])

def p_expDiferente(p):
    '''exp : exp DIFERENTE exp'''
    p[0] = sa.DiferenteExp(p[1], p[3])

def p_expIgualPacarai(p):
    '''exp : exp IGUALPACARAI exp'''
    p[0] = sa.igualpracaraiExp(p[1], p[3])

def p_expIgual(p):
    '''exp : exp IGUAL exp'''
    p[0] = sa.IgualExp(p[1], p[3])

def p_expRestoIncrement(p):
    '''exp : exp RESTOINCREMENT exp'''
    p[0] = sa.RestoIncrementoExp(p[1], p[3])

def p_expDivIncrement(p):
    '''exp : exp DIVINCREMENT exp'''
    p[0] = sa.DivIncrementoExp(p[1], p[3])

def p_expMultIncrement(p):
    '''exp : exp MULTINCREMENT exp'''
    p[0] = sa.MultIncrementoExp(p[1], p[3])

def p_expDecrementN(p):
    '''exp : exp DECREMENTN exp'''
    p[0] = sa.DecrementoNExp(p[1],p[3])

def p_expIncrementN(p):
    '''exp : exp INCREMENTN exp'''
    p[0] = sa.IncrementoNExp(p[1],p[3])

def p_expDecrement(p):
    '''exp : exp DECREMENT'''
    p[0] = sa.DecrementoExp(p[1])

def p_expExponenciacao(p):
    '''exp : exp EXPONENCIACAO exp'''
    p[0] = sa.ExponecialExp(p[1], p[3])

def p_expIncrement(p):
    '''exp : exp INCREMENT'''
    p[0] = sa.IncrementoExp(p[1])

def p_expResto(p):
    '''exp : exp RESTO exp'''
    p[0] = sa.RestoExp(p[1], p[3])

def p_expMult(p):
    '''exp : exp MULT exp'''
    p[0] = sa.MultExp(p[1], p[3])

def p_expDiv(p):
    '''exp : exp DIV exp'''
    p[0] = sa.DivExp(p[1], p[3])

def p_expSub(p):
    '''exp : exp SUB exp'''
    p[0] = sa.SubExp(p[1], p[3])

def p_expString(p):
    '''exp : STRING '''
    p[0] = sa.StringExp(p[1])

def p_call(p):
    '''call : ID LPAREN params RPAREN
            | ID LPAREN RPAREN'''
    if len(p) == 5:
        p[0] = sa.ParamsCall(p[1], p[3])
    else:
        p[0] = sa.NoParamsCall(p[1])

def p_params(p):
    '''params : exp VIRGULA params
              | exp'''
    if len(p) == 4:
        p[0] = sa.CompoundParams(p[1], p[3])
    else:
        p[0] = sa.SingleParams(p[1])

def p_assign(p):
    '''assign : ID ATRIBUICAO exp'''
    p[0] = sa.AssignAssign(p[1], p[3])

def p_tipodecl(p):
    '''tipodecl : LET
                | CONST
                | VAR'''
    p[0] = sa.tipodecl(p[1])

def p_listexp(p):
    '''listexp : exp
               | exp VIRGULA listexp'''
    if len(p) == 4:
        p[0] = sa.CompoundListexp(p[1], p[3])
    else:
        p[0] = sa.SingleListexp(p[1])

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
if __name__ == '__main__':
    f = open('data.txt', 'r')
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    parser.parse(debug=True)