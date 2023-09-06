import random
import jogos
import os
def jogar():
    imprime_mensagem_abertura()
    desc_tema = escolhe_tema()

    letras_erradas = []

    palavra_secreta = carrega_palavra_secreta(desc_tema)

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    #print(letras_acertadas)
    print("\nTema: {0}".format(desc_tema))
    print(*letras_acertadas, sep=' ')

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute(erros)
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            letras_erradas.append(chute)
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        #print(letras_acertadas)
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("\nTema: {}".format(desc_tema))
        print("Letras usadas: {}\n".format(letras_erradas))
        print(*letras_acertadas, sep=' ')

    if(acertou):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(*letras_acertadas, sep=' ')
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    #jogos.escolhe_jogo()
    jogar()
def desenha_forca(erros):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |       |    ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    #print("\n")
    input('')
    

    os.system('cls' if os.name == 'nt' else 'clear')

def imprime_mensagem_perdedor(palavra_secreta):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \\\    ")
    print("\|   XXXX     XXXX   |/     ")
    print(" |   XXXX     XXXX   |      ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    #print("\n\n")
    
    input('')
        
    os.system('cls' if os.name == 'nt' else 'clear')

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
def pede_chute(erros):
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    os.system('cls' if os.name == 'nt' else 'clear')
    desenha_forca(erros)
    return chute

def inicializa_letras_acertadas(palavra):
    #return ["_" for letra in palavra]
    retorno = []
    for letra in palavra:
        if letra == "-":
            retorno.append("-")
        elif letra == " ":
            retorno.append(" ")
        else:
            retorno.append("_")

    return retorno

def imprime_mensagem_abertura():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta(tema):

    if (tema == 'Animais'):
        arquivo = open("animais.txt", "r")
    elif (tema == 'Frutas'):
            arquivo = open("frutas.txt", "r")
    elif (tema == 'Lugares'):
            arquivo = open("lugares.txt", "r")
    else:
        arquivo = open("clubes.txt", "r")


    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def escolhe_tema():
    while True :
        print("Escolha um tema:")
        print("(1) Animais (2) Frutas (3) Lugares (4) Clubes (0) Voltar")
        tema = input(": ")
        if tema == '1':
            return "Animais"
        elif tema == '2':
            return "Frutas"
        elif tema == '3':
            return "Lugares"
        elif tema == '4':
            return "Clubes"
        elif tema == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            jogos.escolhe_jogo()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Entrada invalida!!!\n")

if(__name__ == "__main__"):
    jogar()