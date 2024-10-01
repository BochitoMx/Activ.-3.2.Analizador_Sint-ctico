import ply.yacc as yacc
from lexer import tokens  # Asegúrate de que los tokens estén definidos en el lexer

# Resultado del análisis
resultado_gramatica = []

# Precedencia de los operadores
precedence = (
    ('right', 'ASIGNAR'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV', 'MODULO'),
    ('right', 'POTENCIA'),
    ('right', 'UMINUS'),
)

# Reglas de gramática
def p_programa(t):
    '''programa : declaracion main'''
    resultado_gramatica.append('Programa analizado correctamente')

def p_main(t):
    'main : tipo IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CIERRE bloque'
    resultado_gramatica.append("Función main declarada")

def p_bloque(t):
    '''bloque : declaracion bloque
              | declaracion
              | PARENTESIS_APERTURA PARENTESIS_CIERRE'''
    # Manejo del bloque de código

def p_declaracion(t):
    'declaracion : tipo IDENTIFICADOR ASIGNAR expresion PUNTOYCOMA'
    resultado_gramatica.append(f"Declaración: {t[1]} {t[2]} = {t[4]}")

def p_tipo(t):
    '''tipo : INT
             | FLOAT
             | CHAR
             | DOUBLE
             | VOID'''
    if t[1] == 'FLOAT':
        t[0] = float
    elif t[1] == 'INT':
        t[0] = int
    elif t[1] == 'CHAR':
        t[0] = str
    elif t[1] == 'DOUBLE':
        t[0] = float
    elif t[1] == 'VOID':
        t[0] = None

def p_expresion(t):
    '''expresion : expresion SUMA expresion
                 | expresion RESTA expresion
                 | expresion MULT expresion
                 | expresion DIV expresion
                 | expresion MODULO expresion
                 | PARENTESIS_APERTURA expresion PARENTESIS_CIERRE
                 | IDENTIFICADOR
                 | NUMERO
                 | UMINUS expresion %prec UMINUS'''
    if len(t) == 2:  # Identificador o número
        t[0] = t[1]
    elif len(t) == 4:  # Operaciones
        if t[2] == '+':
            t[0] = t[1] + t[3]
        elif t[2] == '-':
            t[0] = t[1] - t[3]
        elif t[2] == '*':
            t[0] = t[1] * t[3]
        elif t[2] == '/':
            t[0] = t[1] / t[3]
        elif t[2] == '%':
            t[0] = t[1] % t[3]

def p_expresion_logicas(t):
    '''expresion : expresion MENORQUE expresion
                 | expresion MAYORQUE expresion
                 | expresion MENORIGUAL expresion
                 | expresion MAYORIGUAL expresion
                 | expresion IGUAL expresion
                 | expresion DISTINTO expresion
                 | expresion AND expresion
                 | expresion OR expresion
                 | NOT expresion'''
    if len(t) == 4:
        if t[2] == '<':
            t[0] = t[1] < t[3]
        elif t[2] == '>':
            t[0] = t[1] > t[3]
        elif t[2] == '<=':
            t[0] = t[1] <= t[3]
        elif t[2] == '>=':
            t[0] = t[1] >= t[3]
        elif t[2] == '==':
            t[0] = t[1] == t[3]
        elif t[2] == '!=':
            t[0] = t[1] != t[3]
        elif t[2] == '&&':
            t[0] = t[1] and t[3]
        elif t[2] == '||':
            t[0] = t[1] or t[3]
    elif len(t) == 3:  # NOT
        t[0] = not t[2]

def p_error(t):
    global resultado_gramatica
    if t:
        resultado_gramatica.append(f"Error sintáctico en '{t.value}' en la línea {t.lineno}")
    else:
        resultado_gramatica.append("Error sintáctico en EOF")

# Construir el parser
parser = yacc.yacc()

def parse(codigo):
    global resultado_gramatica
    resultado_gramatica.clear()  # Limpiar resultados previos
    result = parser.parse(codigo)  # Analizar el código completo
    
    # Verificar si hubo errores o no
    if "Error sintáctico" not in resultado_gramatica:
        resultado_gramatica.insert(0, "El código que ingresó está correctamente estructurado.")
    
    return resultado_gramatica