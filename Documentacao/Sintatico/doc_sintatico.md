## Condicionais
```ruby
day = 'Sexta'

if day == 'Domingo'
    lunch = 'pizza'
elsif day == 'Sábado'
    lunch = 'panqueca'
else
    puts "Sem almoço hoje :("
```

# Estruturas de Controle (Repetição)

## While
```ruby
while players[i] != 'Neymar'
    if players[i] == 'Messi'
        puts players[i] + ' the G.O.A.T'
    end
    i += 1
end
```

## For
```ruby
players = ['Bale', 'Kanté', 'Messi', 'Aubameyang', 'Reus', 'Neymar', 'Maradona']

print '|| '
for player in players 
    print player + ' || '
end
```

## Loop do
```ruby
loop do
    if players[i] == 'Reus'
        puts players[i] + ' the IDOL'
        break #ponto de parada do loop do
    end
    i += 1
end
```

## Métodos
```ruby
def bemvindo(nome)
  "Bem vindo, #{nome}!"
end
  puts bemvindo("Thiago")
```

## 
