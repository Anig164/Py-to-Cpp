import ply.lex as lex

# Reserved keywords, including True and False
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'print': 'PRINT',
    'for': 'FOR',
    'in': 'IN',
    'range': 'RANGE',
    'True': 'TRUE',  # Reserved keyword for boolean True
    'False': 'FALSE',  # Reserved keyword for boolean False
}

# Tokens to include ID, numbers, operators, commas, and reserved keywords
tokens = (
    'ID', 'NUMBER', 'FLOAT', 'EQUALS',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'EQEQ', 'NEQ', 'AND', 'OR',
    'GT', 'LT', 'COLON', 'NEWLINE', 'STRING',
    'GEQ', 'LEQ', 'COMMA'
) + tuple(reserved.values())  # Include reserved keywords like TRUE and FALSE

# Token rules for operators and symbols
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GT = r'>'
t_LT = r'<'
t_COLON = r':'
t_COMMA = r','  # Rule for comma
t_ignore = ' \t'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQEQ = r'=='
t_NEQ = r'!='
t_GEQ = r'>='
t_LEQ = r'<='

# Rule for strings
def t_STRING(t):
    r'\".*?\"|\'.*?\''
    return t

# Rule for identifiers (variables and reserved keywords)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Rule for floating-point numbers
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)  # Convert matched string to float
    return t

# Rule for integer numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Rule for newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Rule for handling comments (ignore everything after #)
def t_COMMENT(t):
    r'\#.*'
    pass  # Ignore comments

# Rule for errors
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Create the lexer instance
lexer = lex.lex()