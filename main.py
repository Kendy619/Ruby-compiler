from compiler_ruby import *
from sintaticruby2 import *
#import GLCRuby.txt
#import sintaticruby.py

lexer = lex.lex()

# # Test it out
data = '''
    while (b>=3)
      if (text2 === tsxx2) then
        dormirAmem("amem")
      end
    end
    for player in players
      dormir2("amem")
    end
 '''

data2 = '''
class Cachorro

   def falar
    puts("Latir!")
   end

end
}
'''
lexer.input(data)
parser = yacc.yacc()
result = parser.parse(debug=True)



#lexer = lex.lex()
#lexer.input("")
#parser = yacc.yacc()
#parser.parse(debug=False)


print("Hello world!")