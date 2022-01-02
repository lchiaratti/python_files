import random


def jogar():
  print("*********************************")
  print("Bem vindo ao jogo de Adivinhação!")
  print("*********************************")

  numero_secreto =  round(random.random() * 100)
  total_de_tentativas = 0
  pontos = 1000
  #rodada = 1

  print("Qual nível de dificuldade")
  print("(1) Fácil (2) Médio (3) Difícil")

  nivel = int(input("Defina o nível:"))

  if(nivel == 1):
    total_de_tentativas = 10
  elif(nivel == 2):
    total_de_tentativas = 5
  else:
    total_de_tentativas = 1

  #while(rodada <= total_de_tentativas):
  for rodada in range(1, total_de_tentativas + 1):
      print("Tentativa {} de {}".format(rodada, total_de_tentativas))
      #print("Tentativa", rodada, "de", total_de_tentativas)
      chute_str = input("Digite o seu número entre 1 e 100: ")
      print("Você digitou ", chute_str)
      chute = int(chute_str)

      if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

      acertou = chute == numero_secreto
      maior = chute > numero_secreto
      menor = chute < numero_secreto

      if(acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
      else:
        if(maior):
          print("Você errou! O Numero foi maior que o numero secreto.")
        elif(menor):
          print("Você errou! O Numero foi menor que o numero secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        
      #total_de_tentativas = total_de_tentativas - 1
      #rodada = rodada + 1

  print("Fim do jogo")

if(__name__ == "__main__"):
  jogar()