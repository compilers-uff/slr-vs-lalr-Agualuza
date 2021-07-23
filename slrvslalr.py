import ply.lex as lex
import ply.yacc as yacc

tokens = (
    "SYMBOL",
    "EQUAL",
    "MULT"
)

t_EQUAL = r'='
t_MULT = r'\*'

def t_SYMBOL(t):
    r'.+'
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def p_S_eq(p):
    'S : L EQUAL R'
    p[0] = p[1] == p[3]

def p_S_att(p):
    'S : R'
    p[0] = p[1]

def p_L_mult(p):
    'L : MULT R'
    p[0] = 1 * p[2]

def p_L_att(p):
    'L : SYMBOL'
    p[0] = p[1]

def p_R_att(p):
    'R : L'
    p[0] = p[1]

def p_error(p):
    print("ERROR!")

lexer = lex.lex()
parser = yacc.yacc(method="SLR")
