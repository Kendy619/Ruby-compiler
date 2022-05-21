from compiler_ruby import *
from sintaticruby import *
#import GLCRuby.txt
#import sintaticruby.py

lexer = lex.lex()
lexer.input()
parser = yacc.yacc()
parser.parse(debug=False)


print("Hello world!")