import random
import jogos
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    escolhe_nivel = True
    while escolhe_nivel:
        print("Qual nível de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil (0) Voltar")
        nivel = input(": ")
        if(nivel == '1'):
            total_de_tentativas = 20
            escolhe_nivel = False
        elif(nivel == '2'):
            total_de_tentativas = 10
            escolhe_nivel = False
        elif(nivel == '3'):
            total_de_tentativas = 5
            escolhe_nivel = False
        elif (nivel == '0'):
            jogos.escolhe_jogo()
            escolhe_nivel = False
        else:
            print("Entrada invalida!!!\n")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        try:
            chute = int(chute_str)
        except:
            print("Você deve digitar um número entre 1 e 100!")
            #rodada -= 1
            continue

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.\n")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    if (chute != numero_secreto):
        print("O numero correto é {}".format(numero_secreto))

    print("Fim do jogo\n\n")
    #jogos.escolhe_jogo()
    jogar()

if(__name__ == "__main__"):
    jogar()
