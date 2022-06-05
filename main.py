from compiler_ruby import *
from sintaticruby2 import *
from visitor import *
#import GLCRuby.txt
#import sintaticruby.py

lexer = lex.lex()

# # Test it out
data = '''

  imprimir()


  #def puts()
  #  mostrar("oi")
  #end
  #def print(a,b,c)
  #  printar("oi")
  #end
  #def print
  #  print2("oi")
  #end

#while (b>=3)
      #if (text2 === tsxx2) then
        #puts "Olá mundo"
      #end
    #end
    #for player in players
      #dormir2("amem")
    #end
 '''

data2 = '''
    class Cachorro
      def falar
        puts ("Latir!")
      end
      def mover(destino)
         puts ("Correndo")
      end
      a = 1
   
      if 1 == 1
         puts("sa")
      end

     class Peido
       if 1 == 1
         puts("s1a")
       end
      end
    end
'''

lexer.input(data)
parser = yacc.yacc()
result = parser.parse(debug=True)
visitor = Visitor()
for item in result:
  item.accept(visitor)

#lexer = lex.lex()
#lexer.input("")
#parser = yacc.yacc()
#parser.parse(debug=False)


print("Hello world!")