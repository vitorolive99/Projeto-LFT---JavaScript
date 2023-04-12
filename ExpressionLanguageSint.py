# Rascunho da gramatica
# program → funcdecl | funcdecl program | vardecl ; | vardecl ; program
# vardecl → tipodecl ID | tipodecl ID = exp | tipodecl ID [ INTEIRO ] | tipodecl ID = [ listexp ] | tipodecl ID [ INTEIRO ] = listexp | tipodecl ID = []
# funcdecl → signature body
# signature → FUNCTION ID ( sigParams )
# sigparams → ID |  ID , sigparams
# body → { stms }
# stms → stm | stm stms
# stm → vardecl ; | exp ;  | while ( exp ) bodyorstm | return exp ; | if ( exp ) bodyorstm | if ( exp ) bodyorstm else bodyorstm | for ( opexp;opexp;opexp ) bodyorstm 
# opexp → exp | VOID
# bodyorstm → body | stm
# exp → exp + exp | exp - exp | exp / exp | exp * exp | exp % exp | exp ++ |exp ** exp | exp -- | exp += exp | exp -= exp | exp *= exp | exp /= exp| exp %= exp | exp == exp | exp === exp | exp != exp | exp !== exp | exp > exp | exp < exp | exp <= exp | exp >= exp | exp && exp | exp || exp | !exp | exp ? exp : exp | call | assign | INTEIRO | FLOAT | ID | string | TRUE | FALSE
# call → ID (params) | ID ( )
# params → exp, params | exp
# assign → ID = exp
# tipodecl → LET | VAR | CONST
# string → STRINGD | STRINGS
# listexp →  exp | exp , listexp 
import ply.lex as lex
import ply.yacc as yacc
from ExpressionLanguageLex import *

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
    
)

def p_program(p):
    '''program : funcdecl
               | funcdecl program
               | vardecl PV
               | vardecl PV program'''

def p_vardecl(p):
    '''vardecl : tipodecl ID
               | tipodecl ID ATRIBUICAO exp
               | tipodecl ID LCOLCHETE INTEIRO RCOLCHETE
               | tipodecl ID ATRIBUICAO LCOLCHETE listexp RCOLCHETE
               | tipodecl ID LCOLCHETE INTEIRO RCOLCHETE ATRIBUICAO listexp
               | tipodecl ID ATRIBUICAO LCOLCHETE RCOLCHETE'''

def p_funcdecl(p):
    '''funcdecl : signature body'''

def p_signature(p):
    '''signature : FUNCTION ID LPAREN sigParams RPAREN'''

def p_sigParams(p):
    '''sigParams : ID
                 | ID VIRGULA sigParams'''

def p_body(p): 
    '''body : LCHAVES stms RCHAVES'''

def p_stms(p):
    '''stms : stm
            | stm stms'''

def p_stm(p):
    '''stm : vardecl PV
           | exp PV
           | WHILE LPAREN exp RPAREN bodyorstm
           | RETURN exp PV
           | IF LPAREN exp RPAREN bodyorstm
           | IF LPAREN exp RPAREN bodyorstm ELSE bodyorstm
           | FOR LPAREN opexp PV opexp PV opexp RPAREN bodyorstm'''

def p_opexp(p):
    '''opexp : exp
             | VOID'''

def p_bodyorstm(p):
    '''bodyorstm : body
                 | stm'''

def p_exp(p):
    '''exp : exp SOMA exp 
            | exp SUB exp 
            | exp DIV exp 
            | exp MULT exp 
            | exp RESTO exp 
            | exp INCREMENT 
            | exp EXPONENCIACAO exp 
            | exp DECREMENT 
            | exp INCREMENTN exp 
            | exp DECREMENTN exp 
            | exp MULTINCREMENT exp 
            | exp DIVINCREMENT exp
            | exp RESTOINCREMENT exp 
            | exp IGUAL exp 
            | exp IGUALPACARAI exp 
            | exp DIFERENTE exp 
            | exp DIFERENTEPACARAI exp 
            | exp MAIORQ exp 
            | exp MENORQ exp 
            | exp MENORIGUALQ exp 
            | exp MAIORIGUALQ exp 
            | exp AND exp 
            | exp OR exp 
            | NEGACAO exp 
            | exp TERNARIO1 exp TERNARIO2 exp 
            | call 
            | assign 
            | INTEIRO 
            | FLOAT 
            | ID 
            | string 
            | TRUE 
            | FALSE'''

def p_call(p):
    '''call : ID LPAREN params RPAREN
            | ID LPAREN RPAREN'''

def p_params(p):
    '''params : exp VIRGULA params
              | exp'''

def p_assign(p):
    '''assign : ID ATRIBUICAO exp'''

def p_tipodecl(p):
    '''tipodecl : LET
                | VAR
                | CONST'''

def p_string(p):
    '''string : STRINGD
              | STRINGS'''

def p_listexp(p):
    '''listexp : exp
               | exp VIRGULA listexp'''

data2 = '''
function some (a, b){ 
    a = 88 + 44; 
    b = 70; 
    sumparabola(1, 2, 3);         
    while (true){ 
        c = 38; 
        sumparabola(5, true, false); 
        while (c){ 
            sumparabola(5, true, true); 
        } 
    } 
    soma(); 
    sumparabolac(2); 
    return true; 
}
'''
lexer = lex.lex()
lexer.input(data2)
parser = yacc.yacc()
result = parser.parse(debug=False)