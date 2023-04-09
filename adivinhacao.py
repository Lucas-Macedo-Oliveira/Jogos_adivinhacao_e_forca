import random

def jogar():
    print('***********************************')
    print("Bem vindo ao jogo de Adivinhação!")
    print('***********************************')

    numero_secreto = random.randrange (1,101)
    total_tentativas = 0
    pontos = 1000

    print("Qual dificuldade deseja jogar?")
    print("Facil (1) / Médio (2) / Dificil (3)")

    nivel = int(input("Defina o nivel:  "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 15
    elif(nivel == 3):
        total_tentativas = 3


    for rodada in range(1, total_tentativas + 1):
        print("Voce esta na rodada {} de {}".format(rodada,total_tentativas))
        chute_str = input("Digite o seu numero, entre 1 e 100: ")
        print('voce digitou', chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print('voce deve digitar um numero entre 1 e 100')
            continue

        acertou = chute == numero_secreto
        chute_menor = chute < numero_secreto
        chute_maior = chute > numero_secreto

        if(acertou):
            print('boa, voce acertou e voce fez {}' .format(pontos))
            break 
        else:
            if(chute_menor):
                print('voce errou sue chute foi menor que o numero_secreto')
                
            else:
                if(chute_maior):
                    print('seu chute foi maior que o numero_secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            
        



    print("Fim do jogo")
    print("o numero secreto era", numero_secreto)
    print(pontos)

if(__name__=="__main__"):
    jogar()