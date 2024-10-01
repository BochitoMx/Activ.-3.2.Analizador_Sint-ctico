import ply.lex as lex

tokens = [
    'IDENTIFICADOR',
    'NUMERO',
    'PARENTESIS_APERTURA',
    'PARENTESIS_CIERRE',
    'LLAVE_APERTURA',
    'LLAVE_CIERRE',
    'PUNTOYCOMA',
    'ASIGNAR',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',
    'UMINUS',
    'PARIZQ',
    'PARDER',
    'LLAIZQ',
    'LLADER',
    'CORIZQ',
    'CORDER',
    'COMDOB',
    'ENTERO',
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MAYORQUE',
    'MENORIGUAL',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    'FLOAT',
]

# Palabras reservadas
palabras_reservadas = {
    'main': 'MAIN',
    'for': 'FOR',
    'if': 'IF',
    'while': 'WHILE',
    'return': 'RETURN',
}

# Tipos de dato
tipos_dato = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'double': 'DOUBLE',
    'void': 'VOID'
}

tokens = list(tokens) + list(palabras_reservadas.values()) + list(tipos_dato.values())

t_ASIGNAR = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_POTENCIA = r'\\'
t_MODULO = r'%'
t_UMINUS = r'-'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_LLAIZQ = r'\['
t_LLADER = r'\]'
t_CORIZQ = r'\{'
t_CORDER = r'\}'
t_COMDOB = r'\"'
t_ENTERO = r'\d+'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_IGUAL = r'=='
t_DISTINTO = r'!='
t_PUNTOYCOMA = r';'
t_FLOAT = r'\d+\.\d+[eE][+-]?\d+|\d+\.\d+'

t_ignore = ' \t'

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in palabras_reservadas:
        t.type = palabras_reservadas[t.value]  
    elif t.value in tipos_dato:
        t.type = tipos_dato[t.value]  
    return t

def t_NUMERO(t):
    r'\d+|\d+\.\d+[eE][+-]?\d+|\d+\.\d+'
    if '.' in t.value or 'e' in t.value or 'E' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

def analizar_codigo(codigo):
    lineas = codigo.splitlines()  
    resultado = [] 
    
    for i, linea in enumerate(lineas, start=1):
        lexer.input(linea)  
        tokens_por_linea = []
        
        for token in lexer:
            if token.type in tipos_dato.values():
                tokens_por_linea.append(("<Tipo de dato>", token.value))
            elif token.type in palabras_reservadas.values():
                tokens_por_linea.append(("<Reservada {}>".format(token.value), token.value))
            elif token.type == 'PARENTESIS_APERTURA':
                tokens_por_linea.append(("<Parentesis de apertura>", token.value))
            elif token.type == 'PARENTESIS_CIERRE':
                tokens_por_linea.append(("<Parentesis de cierre>", token.value))
            elif token.type == 'LLAVE_APERTURA':
                tokens_por_linea.append(("<Llave de apertura>", token.value))
            elif token.type == 'LLAVE_CIERRE':
                tokens_por_linea.append(("<Llave de cierre>", token.value))
            elif token.type == 'PUNTOYCOMA':
                tokens_por_linea .append(("<Punto y coma>", token.value))
            elif token.type == 'IDENTIFICADOR':
                tokens_por_linea.append(("<Identificador>", token.value))
            elif token.type == 'NUMERO':
                tokens_por_linea.append(("<Número>", token.value))
            elif token.type == 'ASIGNAR':
                tokens_por_linea.append(("<Asignar>", token.value))
            elif token.type == 'SUMA':
                tokens_por_linea.append(("<Suma>", token.value))
            elif token.type == 'RESTA':
                tokens_por_linea.append(("<Resta>", token.value))
            elif token.type == 'MULT':
                tokens_por_linea.append(("<Multiplicación>", token.value))
            elif token.type == 'DIV':
                tokens_por_linea.append(("<División>", token.value))
            elif token.type == 'POTENCIA':
                tokens_por_linea.append(("<Potencia>", token.value))
            elif token.type == 'MODULO':
                tokens_por_linea.append(("<Módulo>", token.value))
            elif token.type == 'UMINUS':
                tokens_por_linea.append(("<Signo menos unario>", token.value))
            elif token.type == 'PARIZQ':
                tokens_por_linea.append(("<Paréntesis izquierdo>", token.value))
            elif token.type == 'PARDER':
                tokens_por_linea.append(("<Paréntesis derecho>", token.value))
            elif token.type == 'LLAIZQ':
                tokens_por_linea.append(("<Corchete izquierdo>", token.value))
            elif token.type == 'LLADER':
                tokens_por_linea.append(("<Corchete derecho>", token.value))
            elif token.type == 'CORIZQ':
                tokens_por_linea.append(("<Llave izquierda>", token.value))
            elif token.type == 'CORDER':
                tokens_por_linea.append(("<Llave derecha>", token.value))
            elif token.type == 'COMDOB':
                tokens_por_linea.append(("<Comillas dobles>", token.value))
            elif token.type == 'ENTERO':
                tokens_por_linea.append(("<Entero>", token.value))
            elif token.type == 'AND':
                tokens_por_linea.append(("<Y lógico>", token.value))
            elif token.type == 'OR':
                tokens_por_linea.append(("<O lógico>", token.value))
            elif token.type == 'NOT':
                tokens_por_linea.append(("<No lógico>", token.value))
            elif token.type == 'MENORQUE':
                tokens_por_linea.append(("<Menor que>", token.value))
            elif token.type == 'MAYORQUE':
                tokens_por_linea.append(("<Mayor que>", token.value))
            elif token.type == 'MENORIGUAL':
                tokens_por_linea.append(("<Menor o igual que>", token.value))
            elif token.type == 'MAYORIGUAL':
                tokens_por_linea.append(("<Mayor o igual que>", token.value))
            elif token.type == 'IGUAL':
                tokens_por_linea.append(("<Igual que>", token.value))
            elif token.type == 'DISTINTO':
                tokens_por_linea.append(("<Distinto que>", token.value))
            elif token.type == 'FLOAT':
                tokens_por_linea.append(("<Número flotante>", token.value))
        
        resultado.append(("LINEA {}".format(i), tokens_por_linea))
    
    return resultado