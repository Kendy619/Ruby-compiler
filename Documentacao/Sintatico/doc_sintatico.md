<a href="https://github.com/Kendy619/Ruby-compiler/blob/main/GLCRuby.txt" target="_blank">Gramática Completa</a>
# 1. Condicionais
### Gramática
```
stm -> IF exp body 
    |  IF exp "then" body 
    |  IF "(" exp ")" body 
    |  IF "(" exp ")" "then" body 
```
### Exemplo
```ruby
day = 'Sexta'

if day == 'Domingo' #Se dia for Domingo
    lunch = 'pizza'
elsif day == 'Sábado' #Se dia for Sábado
    lunch = 'panqueca'
else # Senão
    puts "Sem almoço hoje :("
```

# 2. Estruturas de Controle (Repetição)

## For
### Gramática
```
stm -> FOR ID "in" exp "do" body 
    |  FOR ID "in" exp body 
```
### Exemplo
```ruby
players = ['Bale', 'Kanté', 'Messi', 'Aubameyang', 'Reus', 'Neymar', 'Maradona']

print '|| '
for player in players #para cada elemento na lista faça
    print player + ' || '
end
```
## While
### Gramática
```
stm -> WHILE exp body 
    |  WHILE "(" exp ")" body 
```
### Exemplo
```ruby
while players[i] != 'Neymar' #Enquanto elemento diferente de 'Neymar' faça
    if players[i] == 'Messi'
        puts players[i] + ' the G.O.A.T'
    end
    i += 1
end
```

# 3. Métodos
## Assinatura
### Gramática
```
signature -> "def" ID "(" sigParams ")"
          |  "def" ID  "(" ")" 
          |  "def" ID 
          |  "def" ID sigParams
```
### Exemplo
```ruby
def comprar()

def comprar

def comprar(Produto)

def comprar Produto
```
## Chamada
### Gramática
```
call -> ID "(" params ")" 
     |  ID "(" ")"
```
### Exemplo
```ruby
comprar("Nintendo Switch")
comprar()
```
# 4. Classes
### Gramática
```
class -> "class" ID funcdecl bodyclass 
      |  "class" ID  stms  bodyclass  
bodyclass -> funcdecl "end"
          |  attrdecl "end"
          |  funcdecl bodyclass 
```
### Exemplo
```ruby
class Cachorro #o nome da classe deve iniciar com letra maiúscula

 def falar
  puts "Latir!"
 end

 def mover(destino)
   puts "Correndo para o #{destino}."
 end
 
end
```
# 5. Programa Completo
### Gramática
```
program -> funcdecl  
        |  funcdecl program 
        |  class 
        |  class program 
        |  stm 
        |  stm program 
```

### Exemplo
```ruby
day = 'Sexta'

if day == 'Domingo'
    lunch = 'pizza'
elsif day == 'Sábado'
    lunch = 'panqueca'
else
    puts "Escolha o que vai querer almoçar hoje"
    puts "1-panqueca\n2-lanche do bk\n3-feijoada"
    print "->"
    lunch = gets.chomp.to_i
    case lunch
    when 1
        lunch = "panqueca"
    when 2
        lunch = "lanche do bk"
    when 3..4
        lunch = "feijoada"
    else
        puts "Opção incorreta"
    end

end

#se dia não é sábado == (if not)
unless day == 'Sábado'
    puts "Hoje não é Sábado, na real hoje é #{day}"
end

puts "Hoje meu almoço vai ser -> #{lunch}"
```
<a href="https://github.com/Kendy619/Ruby-compiler/blob/main/GLCRuby.txt" target="_blank">Gramática Completa</a>
