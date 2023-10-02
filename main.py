import random

def rolar_dado():
    valor_minimo = 1
    valor_maximo = 6
    resultado_rolagem = random.randint(valor_minimo, valor_maximo)

    return resultado_rolagem

while True:
    jogadores = input("Qual é o número de jogadores (2 - 4): ")
    if jogadores.isdigit():
        jogadores = int(jogadores)
        if 2 <= jogadores <=4:
            break
        else:
            print("O número de jogadores deve ser entre 2 - 4.")
    else:
        print("Número inválido! Tente novamente.")

pontuacao_maxima = 50
pontuacao_jogadores = [0 for _ in range(jogadores)]

while max(pontuacao_jogadores) < pontuacao_maxima:
    for indice_jogadores in range(jogadores):
        print("\nO turno do jogador número", indice_jogadores + 1, "começou!" )
        print("Sua pontuação total é: ", pontuacao_jogadores[indice_jogadores], "\n")
        pontuacao_atual = 0

        while True:
            deseja_rolar_dados = input("Gostaria de rolar o dado (y)? ")
            if deseja_rolar_dados.lower() != "y":
                break

            valor = rolar_dado()
            if valor == 1:
                print("Você rolou um número 1! O seu turno acabou.")
                pontuacao_atual = 0
                break
            else:
                pontuacao_atual += valor
                print("Você rolou um:" , valor)

            print("A sua pontuação atual é: ", pontuacao_atual)

        pontuacao_jogadores[indice_jogadores] += pontuacao_atual
        print("Sua pontuação atual: ", pontuacao_jogadores[indice_jogadores])

pontuacao_maxima = max(pontuacao_jogadores)
indice_ganhador = pontuacao_jogadores.index(pontuacao_maxima)
print("O jogador número", indice_ganhador + 1, 
      "é o vencedor com uma pontuação de: ", pontuacao_maxima)

