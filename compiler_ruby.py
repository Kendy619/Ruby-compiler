import ply.lex as lex # importando a biblioteca ply para o léxico
#Definindo Tokens e seus ptadroes

tokens = ['PLUS', 'MINUS', 'TIMES', 'DIV', 'NOT', 'AND', 'BEGIN', 'DEF', 'ELSE', 'END', 'IF', 
'RETURN', 'TRUE', 'BIGGEST', 'EQ', 'DIFF', 'BREAK', 'ELSIF', 'FALSE','IN', 'NIL', 'OR', 'THEN', 
'WHILE','SMALL','DOUBLEEQUAL', 'NUMBER', 'NAME', 'COMMENT', 'ID', 'CLASS', 'FOR', 'MODULE', 'SELF', 
'SUPER', 'EXPO', 'REST', 'TRIPLEEQ', 'SMALLEQ', 'BIGGESTEQ', 'POINTRANGE', 'DOUBLEBAR', 'DOUBLEE',
'EXCLAMATION','SIMPLEBAR', 'SIMPLEE', 'CIRCUMFLEX', 'NEGATION', 'ID_GLOBAL','ID_INSTANCE',
'ID_CLASS', 'OPENKEY', 'CLOSEKEY', 'COMMENTMULTI', 'STRING', 'LPAREN', 'RPAREN','DO', 'BIGGSMALLEQ','LSHIFT', 'RSHIFT', 'PONTOVIRGULA', 'BARN','VIRGULA']
#ADCIONEI LPAREN E RPAREN ASS: THIAGO
#adicionei DO, BIGGSMALLEQ, LSHIFT, RSHIFT
#ADD quebra de linha "BARN", "VIRGULA"


t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES  = r'\*'
t_DIV  = r'\\'
t_EXPO = r'\*\*'
t_REST = r'\%'
t_ignore = ' \t'
t_AND = r'and'
t_BREAK = r'break'
t_ELSIF = r'elsif'
t_FALSE = r'false'
t_IN = r'in'
t_NIL = r'nil'
t_OR = r'or'
t_THEN = r'then'
t_DO = r'do'
t_WHILE = r'while'
t_FOR = r'for'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_OPENKEY = r'\{'
t_CLOSEKEY = r'\}'
t_PONTOVIRGULA = r'\;'
t_VIRGULA = r'\,'

t_SMALLEQ = r'<\='
t_BIGGESTEQ = r'>\='
t_BIGGSMALLEQ = r'<\=>'

t_SIMPLEBAR = r'\|'
t_SIMPLEE = r'&'
t_CIRCUMFLEX = r'\^'
t_NEGATION = r'~' 
t_DOUBLEBAR = r'\|\|'
t_DOUBLEE = r'\&\&'
t_EXCLAMATION = r'\!'
t_LSFHIT = r'<<'
t_RSHIFT = r'>>'

t_SMALL = r'<'
t_TRIPLEEQ = r'\=\=\='
t_DOUBLEEQUAL = r'\=\= '
t_POINTRANGE = r'\.\.'

t_BEGIN = r'begin '
t_DEF = r'def '
t_ELSE = r'else '
t_END = r'end '
t_CLASS = r'class'
t_MODULE = r'module'
t_SELF = r'self'
t_SUPER = r'super'
t_IF = r'if '
t_NOT = r'not'
t_RETURN = r'return '
t_TRUE = r'true '
t_BIGGEST = r' > '
t_EQ = r' = '
t_DIFF = r' != '


#Criando analisador Lexico e realizando analise lexica

def t_BARN(t):
    r'(.|\s)*'


def t_COMMENTMULTI(t):
  r'\=begin(.*)\n(.|\n)*?\=end' 


def t_STRING(t):
   r'\".*?\"|\'.*?\''
   return t


def t_error(t):
   print('Illegal character ""%s"' % t.value[0])
   t.lexer.skip(1)

def t_newline(t): #Adiciona a função t_newline
     r'\n+' 
     t.lexer.lineno += len(t.value) 

def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t

'''def t_NAME(t):'''

#NFT nosso no marketplace ;)


def t_COMMENT(t):
  r'\#.*' 
  

def t_ID_GLOBAL(t):
  r'\$[a-zA-Z_][a-zA-Z_0-9]*'
  for key in tokens:
    if key == (t.value).upper():
      t.type = key
      return t
  return t


def t_ID_INSTANCE(t):
  r'\@[a-zA-Z_][a-zA-Z_0-9]*'
  for key in tokens:
    if key == (t.value).upper():
      t.type = key
      return t
  return t


def t_ID_CLASS(t):
  r'\@\@[a-zA-Z_][a-zA-Z_0-9]*'
  for key in tokens:
    if key == (t.value).upper():
      t.type = key
      return t
  return t


def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  for key in tokens:
    if key == (t.value).upper():
      t.type = key
      return t
  return t


lexer = lex.lex()

lexer.input('''+-\n\*notnome_jogador=>
           
            #testandocomentario
            menino ney
            "teste de string""teste aspas"
            'bacco'
            ***
            #
            ;
            #sada
            adfd
            =begin defrefgrtgtrgegergerfgerf
            frgtgtrgr
            =end
          sada;
            ;
            

            =begin asgasd =end
            =end
            ""
           ==
           === ("#aseef",dedefr,121,"sdefdref")
            ("swdefr")
            
            ''')

for tok in lexer:
  print(f'Chave:{tok.type}\t\t Valor:{tok.value}\t\t Linha:{tok.lineno}\t\t Posicao:{tok.lexpos}')
