from compiler_ruby import *
from sintaticruby2 import *
#import GLCRuby.txt
#import sintaticruby.py

lexer = lex.lex()

# # Test it out
data = '''
    #if (texto1 == texto2)
    #    puts("Iguais")
    #    return 1
    #end
    #if text1 == text2
    #  comer("abc",cbb)
    #end

    if text1 == text2 then
      comer("asd",sss)
    end

    if (text2 == tsxx2) then
      dormirAmem("amem")
    end


 '''
data2 = '''
int some (int a, int b){ 
    a = 88 + 44; 
    b = 70; 
    sumparabola(1, 2, 3);         
    while (true){ 
        c = 38; 
        sumparabola(5, true, false); 
        while (c){ 
            sumparabola(5, true, true); 
        } 
    } 
    soma(); 
    sumparabolac(2); 
    return true; 
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