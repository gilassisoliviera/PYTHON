import forca
import adivinhacao
import os

os.system('cls' if os.name == 'nt' else 'clear')

def escolhe_jogo():
    while True:
        print("*********************************")
        print("*******Escolha o seu jogo!*******")
        print("*********************************")

        print("(1) Forca (2) Adivinhação (0) Sair")

        jogo = input("Qual jogo? ")


        if(jogo == '1'):
            print("Jogando forca")
            forca.jogar()
        elif(jogo == '2'):
            print("Jogando adivinhação")
            adivinhacao.jogar()
        elif (jogo == '0'):
            print("\nObrigado por jogar ...\n")
            exit()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nOpção Inválida ...\n")


if(__name__ == "__main__"):
    escolhe_jogo()