#Imports
import random
from os import system, name


# Função para limpar a tela a cada execução
def limpa_tela():
    
    # Windows
    if name == 'nt':
        _= system('cls')
    
    # Mac ou linux
    else:
        _= system('clear')

# Função iniciar game
def game():
    
    limpa_tela()
    print('\nBem vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')

    # Lista de palavras para o jogo
    palavras = ["abacaxi", "banana", "caju", "kiwi", "laranja", "manga", "morango", "pera", "uva", "melancia"]

    # Escolher randomicamente uma palavra
    palavra = random.choice(palavras)

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 10

    # Lista para as letras erradas
    letras_erradas = []

    # Loop enquanto número de chances for maior do que zero
    while chances > 0:

        #print
        print(" ".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("Letras erradas: ", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\n Digite uma letra: ").lower()

        #Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        #Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era: ", palavra)
            break

    # Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era: ", palavra)

#Bloco main
if __name__ == "__main__":
    game()