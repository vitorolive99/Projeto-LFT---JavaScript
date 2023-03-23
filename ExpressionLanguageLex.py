import ply.lex as lex

#linguagem léxica de JavaScript

#palavras reservadas

reservadas = {
    'break' : 'BREAK' ,
    'case' : 'CASE' ,
    'catch' : 'CATCH' ,
    'class' : 'CLASS' ,
    'const' : 'CONST' ,
    'continue' : 'CONTINUE' ,
    'debugger' : 'DEBUGGER' ,
    'default' : 'DEFAULT' ,
    'delete' : 'DELETE' ,
    'do' : 'DO' ,
    'else' : 'ELSE' ,
    'export' : 'EXPORT' ,
    'extends' : 'EXTENDS' ,
    'finally' : 'FINALLY' ,
    'for' : 'FOR' ,
    'function' : 'FUNCTION' ,
    'if' : 'IF' ,
    'import' : 'IMPORT' ,
    'in' : 'IN' ,
    'instanceof' : 'INSTANCEOF' ,
    'new' : 'NEW' ,
    'return' : 'RETURN' ,
    'super' : 'SUPER' ,
    'switch' : 'SWITCH' ,
    'this' : 'THIS' ,
    'throw' : 'THROW' ,
    'try' : 'TRY' ,
    'typeof' : 'TYPEOF' ,
    'var' : 'VAR' ,
    'void' : 'VOID' ,
    'while' : 'WHILE' ,
    'with' : 'WITH' ,
    'yield' : 'YIELD',
    'await' : 'AWAIT',
    'protected' : 'PROTECTED',
    'static' : 'STATIC',
    'private' : 'PRIVATE',
    'public' : 'PUBLIC',
    'let' : 'LET',
    'abstract' : 'ABSTRACT',
    'boolean' : 'BOOLEAN',
    'byte' : 'BYTE',
    'char' : 'CHAR',
    'double' : 'DOUBLE',
    'final' : 'FINAL',
    'float' : 'FLOAT', 
    'int' : 'INT',
    'long' : 'LONG',
    'short' : 'SHORT',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'null' : 'NULL',
}

#lista de tokens
tokens=['INTEIRO',
        'ID',
        'SOMA',
        'SUB',
        'MULT',
        'DIV', 
        'RESTO', 
        'INCREMENT',
        'DECREMENT', 
        'ATRIBUICAO', 
        'INCREMENTN', 
        'EXPONENCIACAO',
        'DECREMENTN', 
        'MULTINCREMENT', 
        'DIVINCREMENT', 
        'RESTOINCREMENT', 
        'IGUAL', 
        'IGUALPACARAI', 
        'DIFERENTE', 
        'DIFERENTEPACARAI', 
        'MAIORQ', 
        'MENORQ', 
        'MAIORIGUALQ', 
        'MENORIGUALQ', 
        'AND', 
        'OR', 
        'NEGACAO', 
        'TERNARIO2', 
        'TERNARIO1', 
        'LCHAVES', 
        'RCHAVES', 
        'LPAREN', 
        'RPAREN', 
        'LCOLCHETE', 
        'RCOLCHETE', 
        'PV', 
        'VIRGULA',
        'ASPAD',
        'ASPAS', 
        'STRINGD',
        'STRINGS',
        'NFLOAT',
        'OCTAL',
        'HEXADECIMAL',
        'COMMENT',
        'COMMENTMULTI',
        'TRUE',
        'FALSE',
        'NULL',
        ] + list(reservadas.values())

t_SOMA = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_RESTO = r'%'
t_INCREMENT = r'\+\+'
t_EXPONENCIACAO = r'\*\*'
t_DECREMENT = r'--'
t_ATRIBUICAO = r'='
t_INCREMENTN = r'\+='
t_DECREMENTN = r'-='
t_MULTINCREMENT = r'\*='
t_DIVINCREMENT = r'/='
t_RESTOINCREMENT = r'%='
t_IGUAL = r'=='
t_IGUALPACARAI = r'==='
t_DIFERENTE = r'!='
t_DIFERENTEPACARAI = r'!=='
t_MAIORQ = r'>'
t_MENORQ = r'<'
t_MAIORIGUALQ = r'>='
t_MENORIGUALQ = r'<='
t_AND = r'&&'
t_OR = r'||'
t_NEGACAO = r'!'
t_TERNARIO1 = r'?'
t_TERNARIO2 = r':'
t_LCHAVES = r'\{'
t_RCHAVES = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCOLCHETE = r'['
t_RCOLCHETE = r']'
t_PV = r';'
t_VIRGULA = r','
t_ASPASD = r'\''
t_ASPAS = r'\"'

def t_STRINGD(t):
    r'[\"][^\"\n][\"]'

def t_STRINGS(t):
    r'[\'][^\'\n][\']'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
    r'//.*\n'
    pass

def t_COMMENTMULTI(t):
    r'/\*[^]+\*/'
    pass

def t_NFLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_OCTAL(t):
    r'0o[0-7]+'
    t.value = int(t.value, 8)
    return t

def t_HEXADECIMAL(t):
    r'0x[0-9a-fA-F]+'
    t.value = int(t.value, 16)
    return t

def t_TRUE(t):
    r'true'
    t.value = True
    return t

def t_FALSE(t):
    r'false'
    t.value = False
    return t

def t_NULL(t):
    r'null'
    t.value = None
    return t