import string


nome = 'Pedro'
idade = 25
altura = 1.82

filhos = input('quantos filhos você tem?')


print (nome, 'tem', idade, 'anos e', altura, 'de altura')
print (nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura')

print (nome, 'tem,', idade, 'anos, eu sou mais jovem')

# Existindo necessidade de adicionar pontuação, colocar dentro de ""/''
# concatenar dados formando frases. Pode-se usar virgula ou + porwm, com 
#+ não será adicionado espaço e será necessário transformar numeros inteiros
#inte em string (texto)

print (filhos)
