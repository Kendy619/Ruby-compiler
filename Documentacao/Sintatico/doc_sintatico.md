# 1. Condicionais
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
```ruby
players = ['Bale', 'Kanté', 'Messi', 'Aubameyang', 'Reus', 'Neymar', 'Maradona']

print '|| '
for player in players #para cada elemento na lista faça
    print player + ' || '
end
```
## While
```ruby
while players[i] != 'Neymar' #Enquanto elemento diferente de 'Neymar' faça
    if players[i] == 'Messi'
        puts players[i] + ' the G.O.A.T'
    end
    i += 1
end
```
## Loop do
```ruby
loop do #Repete até encontrar um break com ou sem condicional
    if players[i] == 'Reus'
        puts players[i] + ' the IDOL'
        break #ponto de parada do loop do
    end
    i += 1
end
```

## Until
```ruby
var = 7
until var == 11 do #Enquanto for diferente faça
  puts var * 10
  var = var + 1
end
```
# 3. Métodos
## Assinatura
```ruby
def comprar()

def comprar

def comprar(Produto)

def comprar Produto

```
## Chamada
```ruby
comprar("Nintendo Switch")
comprar()
```

## Exemplo
```ruby
def printar texto1, texto2
    puts('Hello World!', texto1, texto2)
    if (texto1 == texto2) then
        puts("Iguais")
        return 1
    end
    return 2;
end

puts(printar("É melhor", "É melhosr"))
```
# 4. Classes
```ruby
class Cachorro #o nome da classe deve começar com letra maiúscula

 def falar
  puts "Latir!"
 end

 def mover(destino)
   puts "Correndo para o #{destino}."
 end
 
end
```
