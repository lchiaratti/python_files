import random



def jogar():

    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    #carrega_palavra_secreta()    
    #letras_acertadas = ["_" for letra in palavra_secreta]
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    
    #enquanto não enforcou E não acertou
    while(not enforcou and not acertou):

      chute = pede_chute()

       
      if(chute in palavra_secreta): 
          marca_chute_correto(chute, letras_acertadas, palavra_secreta)
      else:
          erros += 1

      enforcou = erros == 6
      acertou = "_" not in letras_acertadas
      print(letras_acertadas)
          

      print("Jogando...")

    if(acertou):
      mensagem_vencedor()     
    else:
      mensagem_perdedor(palavra_secreta)    
    #print("Fim do jogo")


def mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    #print(palavras)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    #palavra_secreta = "maça".upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual a letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
          #print("Encontrei a letra {} na posiçao {}".format(letra, index))
          letras_acertadas[index] =  letra
        index += 1


def mensagem_vencedor():
    print("Você ganhou!!!!")
def mensagem_perdedor(palavra_secreta):
    print("Você perdeu!!!!")
    print("A palavra secreta era {}".format(palavra_secreta))

if(__name__ == "__main__"):
  jogar()