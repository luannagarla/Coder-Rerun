pesquisasFeitas = int(input('Pesquisas Feitas: '))
pesquisasFeitasinput = []

for var in range (pesquisasFeitas):
    pesquisasFeitasinput.append(input('Suas Pesquisas Feitas: '))
print('{}'.format(pesquisasFeitasinput))

pesquisasAFazer = int(input('Pesquisas a Fazer: '))
pesquisasAFazerInput = []

for var in range (pesquisasAFazer):
    pesquisasAFazerInput.append(input('Suas Pesquisas a Fazer: '))
print('{}'.format(pesquisasAFazerInput))

contador = 0
temp = 0
contadorIgualdade = 0

maxstring = []

while contador != pesquisasFeitas :  

    maxstring.append(len(pesquisasFeitasinput[contador]))
    maiorstring = max(maxstring)

    if pesquisasAFazerInput[temp] in pesquisasFeitasinput[contador]:
        contadorIgualdade+= 1
    if contador == pesquisasFeitas :

        temp+= 1
        contador = 0
    contador += 1


for contador in range (pesquisasFeitas):

    if pesquisasAFazerInput[temp] in pesquisasFeitasinput[contador]:
        contadorIgualdade+= 1
    if contador == pesquisasFeitas :
   
        temp+= 1
        contador = 0
    contador += 1
        
contadorReal = contadorIgualdade - 1        
print('igualdade {}'.format(contadorReal))
print('maior {}'.format(maiorstring))