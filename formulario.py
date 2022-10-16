nome = input('Escreva seu nome:')
idade = input('Qual é a sua idade?')
profissão = input('Qual é a sua profissão?')

print (nome, 'tem', idade, 'anos e sua profisão é:', profissão)

#input sempre traz um objeto tipo string ainda que exista float(decimal)
#e numeros inteiros. Exemplo abaixo

print (type(nome), type(idade), type(profissão))

