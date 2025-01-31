import random

def gerar_cartela(linhas, colunas, intervalos):
    cartela = []
    for i in range(colunas):
        numeros = random.sample(range(intervalos[i][0], intervalos[i][1] + 1), linhas)
        cartela.append(numeros)
    return [list(coluna) for coluna in zip(*cartela)]


def exibir_cartela(cartela, nome, numeros_sorteados):
    print(f"\nCartela de {nome}:")
    for linha in cartela:
        for numero in linha:
            if numero in numeros_sorteados:
                print(f"[{numero:2}]", end=" ")
            else:
                print(f" {numero:2} ", end=" ")
        print()


def sorteio_bingo(intervalo):
    numeros = list(range(intervalo[0], intervalo[1] + 1))
    random.shuffle(numeros)
    for numero in numeros:
        yield numero


def verificar_vitoria(cartela, numeros_sorteados):
    
    for linha in cartela:
        if not all(num in numeros_sorteados for num in linha):
            return False
    return True


def executar_bingo(modo):
    if modo == "simples":
        linhas, colunas, jogadores = 2, 3, 2
        intervalos = [(1, 10), (11, 20), (21, 30)]
    elif modo == "demorado":
        linhas, colunas, jogadores = 3, 4, 4
        intervalos = [(1, 10), (11, 20), (21, 30), (31, 40)]
    else:
        print("Modo inválido.")
        return

    cartelas = []
    for i in range(jogadores):
        nome = f"Jogador {i + 1}"
        cartela = gerar_cartela(linhas, colunas, intervalos)
        cartelas.append((nome, cartela))

    intervalo_sorteio = (1, max(i[1] for i in intervalos))
    sorteados = set()
    sorteador = sorteio_bingo(intervalo_sorteio)
    ganhadores = []

    print(f"\nModo {modo.upper()} iniciado!")
    print("Pressione ENTER para sortear o próximo número.")

    while not ganhadores:
        comando = input("\n (ou 'sair' para encerrar o jogo): ").strip().lower()
        if comando == "sair":
            print("Jogo encerrado.")
            return

        numero = next(sorteador, None)
        if numero is None:
            print("Todos os números já foram sorteados. Jogo encerrado.")
            return

        sorteados.add(numero)
        print(f"\nÚltima dezena sorteada: {numero}")
        print(f"Dezenas sorteadas (ordem crescente): {sorted(sorteados)}")

        for nome, cartela in cartelas:
            exibir_cartela(cartela, nome, sorteados)

        for nome, cartela in cartelas:
            if nome not in ganhadores and verificar_vitoria(cartela, sorteados):
                ganhadores.append(nome)

    print("\nFim do jogo!")
    print(f"Ganhador: {', '.join(ganhadores)}")


def main():
    print("Seja bem-vindo ao bingo!")
    print("Escolha o modo de jogo:")
    print("1. Modo simples")
    print("2. Modo Demorado")
escolha = input("Digite o número do modo desejado: ")

if escolha == "1":
        executar_bingo("simples")
elif escolha == "2":
        executar_bingo("demorado")
else:
        print("Escolha inválida.")


if __name__ == "_main_":
    main()