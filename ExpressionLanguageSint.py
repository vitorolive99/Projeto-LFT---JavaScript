# Rascunho da gramatica
# program → funcdecl | funcdecl program | vardecl ; | vardecl ; program
# vardecl → tipodecl ID | tipodecl ID = exp | tipodecl ID [ INTEIRO ] | tipodecl ID = [ listexp ] | tipodecl ID [ INTEIRO ] = listexp
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
# listexp →  exp | exp , listexp | VOID
