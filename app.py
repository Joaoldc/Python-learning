print ("olá mundo") #referente ao curso de 5hs
print("apenas um")
print("teste")
print("gol"*3)
print("codigo virando comentário ao add #")

#essa linha não será lida, # para comentários

#Variáveis
idade = 12
idade = 7
# idade é uma variável e nesse momento, de 12 passou a ser 7
print(idade)

#python tem 4 tipos de variáveis simples

idade = 16 #integer inteiro
altura = 1.54 #float decimal
nome = "catia" #string ou texto
casado = False #boolean lógica booleana v/f

print(type(idade))
print(type(altura))
print(type(nome))
print(type(casado))

print(type(idade))
print(type(altura))
#pode-se utilizar comentários em qualquer lugar usando #
print(type(nome))
print(type(casado))

#string usar "" ou ''


nome = "In today's lessons" #concordando com o sinal inicial
print (nome)

#escrever frases ocupando várias linhas ''' *****'''

carta = '''
Caro funcionário,

Por meio desta, informamos sua

nova promoção'''

print (carta)

# imprimir apenas as letras da posição requerida 0,1,2,3 ou (-1,-2 de traz para frente)etc
#posição 3 = r de Caro.
print(carta[3])

print(carta[2:5]) #imprimirá apenas ao da palavra Ca(2)ro(5) começando do 0

#String formatadas

nome = "joana"
apelido = "Silva"
idade = 36

# escrever: a Joana (Silva) tem 36 anos
frase1 = "A " + nome + " (" + apelido +") " + "tem " + str(idade) + " anos!"
print (frase1)

#muito difícil de fazer (utilizar strings formatadas)

frase2 = f"A {nome} ({apelido}) tem {idade} anos"
print(frase2)




