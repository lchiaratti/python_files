idade1 = 39
idade2 = 30
idade3 = 27
print(idade1)
print(idade2)
print(idade3)

idades = [30, 40, 50]

type(idades)
len(idades)
idades[0]
idades[1]
print(idades[1])

idades.remove(30)
idades.append(70)
print(idades)


if 50 in idades:
    idades.remove(50)

print(idades)

idades.insert(0,10)
print(idades)

#idades.append([27, 19])
#print(idades)

for elemento in idades:
    print("Recebi o elemento" , elemento)

idades.extend([27, 19])
print(idades)

#idades_no_ano_que_vem = []
#for idade in idades:
#    idades_no_ano_que_vem.append(idade+1)
#  idades_no_ano_que_vem

idades_no_ano_que_vem = [(idade+1) for idade in idades]
print(idades_no_ano_que_vem)

idade_maior = [(idade) for idade in idades if idade > 21 ]
print(idade_maior)


def faz_processamento_de_visualizaao(lista):
    print(len(lista))
    lista.append(13)


def faz_processamento_de_visualizaao(lista = []):
    print(len(lista))
    lista.append(13)
 
