import random

# Definições de constantes
ALFABETO = 'ABCDEFGHIJ'

CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}


def criar_tabuleiro(N):
    tabuleiro = []
    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(' ')
        tabuleiro.append(linha)
    return tabuleiro

def verificar_posicao(tabuleiro, blocos, linha, coluna, orientacao):
    tamanho_tabuleiro = len(tabuleiro)

    if orientacao == 'v':
        if linha + blocos > tamanho_tabuleiro:
            return False
        for i in range(linha, linha + blocos):
            if tabuleiro[i][coluna] != ' ':
                return False
    elif orientacao == 'h':
        if coluna + blocos > tamanho_tabuleiro:
            return False
        for j in range(coluna, coluna + blocos):
            if tabuleiro[linha][j] != ' ':
                return False
    else:
        return False

    return True

def alocar_navios(tabuleiro, frota):
    tamanho_tabuleiro = len(tabuleiro)
    for navio, quantidade in frota.items():
        for _ in range(quantidade):
            while True:
                linha = random.randint(0, tamanho_tabuleiro - 1)
                coluna = random.randint(0, tamanho_tabuleiro - 1)
                orientacao = random.choice(['h', 'v'])
                if verificar_posicao(tabuleiro, CONFIGURACAO[navio], linha, coluna, orientacao):
                    if orientacao == 'v':
                        for i in range(linha, linha + CONFIGURACAO[navio]):
                            tabuleiro[i][coluna] = 'N'
                    elif orientacao == 'h':
                        for j in range(coluna, coluna + CONFIGURACAO[navio]):
                            tabuleiro[linha][j] = 'N'
                    break
    return tabuleiro

def alocar_navios_jogador(tabuleiro, frota):
    print("\nPosicione seus navios:")
    tamanho_tabuleiro = len(tabuleiro)
    for navio, quantidade in frota.items():
        print(f"\nAlocando {quantidade} navios do tipo {navio}:")
        for _ in range(quantidade):
            while True:
                exibir_tabuleiros(tabuleiro, criar_tabuleiro(tamanho_tabuleiro))
                posicao = input(f"\nEscolha a posição para o navio {navio} (ex: A1): ")
                orientacao = input("Escolha a orientação do navio (h para horizontal, v para vertical): ").lower()
                linha = int(posicao[1:]) - 1 if posicao[1:].isdigit() and 1 <= int(posicao[1:]) <= tamanho_tabuleiro else -1
                coluna = ALFABETO.index(posicao[0].upper()) if posicao[0].upper() in ALFABETO else -1
                if 0 <= linha < tamanho_tabuleiro and 0 <= coluna < tamanho_tabuleiro and verificar_posicao(tabuleiro, CONFIGURACAO[navio], linha, coluna, orientacao):
                    if orientacao == 'v':
                        for i in range(linha, linha + CONFIGURACAO[navio]):
                            tabuleiro[i][coluna] = 'N'
                    elif orientacao == 'h':
                        for j in range(coluna, coluna + CONFIGURACAO[navio]):
                            tabuleiro[linha][j] = 'N'
                    break
                else:
                    print("Posição inválida! Tente novamente.")

def exibir_tabuleiros(tabuleiro_jogador, tabuleiro_oponente, ocultar_navios=False):
    tamanho_tabuleiro = len(tabuleiro_jogador)
    
    print('  Seu Tabuleiro\t\t\t\t\tTabuleiro do Oponente')
    print('   ' + ' '.join(ALFABETO[:tamanho_tabuleiro]) + ' ' * 8 + '   ' + ' '.join(ALFABETO[:tamanho_tabuleiro]))
    
    for i in range(tamanho_tabuleiro):
        print(f'{i+1:2} ', end='')
        for j in range(tamanho_tabuleiro):
            if tabuleiro_jogador[i][j] == 'O':
                print(CORES['blue'] + '██' + CORES['reset'], end='')
            elif tabuleiro_jogador[i][j] == 'X':
                print(CORES['red'] + '██' + CORES['reset'], end='')
            elif tabuleiro_jogador[i][j] == 'N':
                print(CORES['green'] + '██' + CORES['reset'], end='')
            else:
                print('  ', end='')
        
        print(' ' * 8, end='')
        
        print(f'{i+1:2} ', end='')
        for j in range(tamanho_tabuleiro):
            if ocultar_navios and tabuleiro_oponente[i][j] == 'N':
                print(' ' + ' ', end='')
            else:
                if tabuleiro_oponente[i][j] == 'O':
                    print(CORES['blue'] + '██' + CORES['reset'], end='')
                elif tabuleiro_oponente[i][j] == 'X':
                    print(CORES['red'] + '██' + CORES['reset'], end='')
                elif tabuleiro_oponente[i][j] == 'N':
                    print(CORES['green'] + '██' + CORES['reset'], end='')
                elif tabuleiro_oponente[i][j] == ' ':
                    print('  ', end='')  
                else:
                    print('  ', end='')
        print()

def realizar_ataque(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 'N':
        tabuleiro[linha][coluna] = 'X'
        print("Acertou um navio!")
    elif tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = 'O'
        print("Errou o alvo!")
    else:
        print("Posição já foi atacada! Escolha outra.")

def verificar_vitoria(tabuleiro):
    for linha in tabuleiro:
        if 'N' in linha:
            return False
    return True

def selecionar_nacao():
    print("\nEscolha o número da nação para sua frota:")
    for numero, nacao in enumerate(PAISES, start=1):
        print(f"{numero}: {nacao}")
        print("   Barcos disponíveis:")
        for navio, quantidade in PAISES[nacao].items():
            print(f"      {quantidade} {navio}")
    while True:
        escolha = input("Número da nação: ")
        if escolha.isdigit() and 1 <= int(escolha) <= 5:
            return int(escolha)
        else:
            print("Número inválido! Escolha um número de 1 a 5.")

def jogar_batalha_naval():
    tamanho_tabuleiro = 10
    tabuleiro_jogador1 = criar_tabuleiro(tamanho_tabuleiro)
    tabuleiro_jogador2 = criar_tabuleiro(tamanho_tabuleiro)

    nacao_jogador = selecionar_nacao()
    frota_jogador = list(PAISES.values())[nacao_jogador - 1]
    alocar_navios_jogador(tabuleiro_jogador1, frota_jogador)

    print("\nComputador está alocando os navios de guerra...")
    alocar_navios(tabuleiro_jogador2, PAISES['Japão'])

    print("\nComputador já está em posição de batalha!\n")

    vez_do_jogador1 = True

    while True:
        if vez_do_jogador1:
            print("\nVez do Jogador:")
            while True:
                exibir_tabuleiros(tabuleiro_jogador1, tabuleiro_jogador2, ocultar_navios=True)
                ataque = input("Escolha a posição para atacar (ex: A1): ")
                linha = int(ataque[1:]) - 1 if ataque[1:].isdigit() and 1 <= int(ataque[1:]) <= tamanho_tabuleiro else -1
                coluna = ALFABETO.index(ataque[0].upper()) if ataque[0].upper() in ALFABETO else -1
                if 0 <= linha < tamanho_tabuleiro and 0 <= coluna < tamanho_tabuleiro:
                    if tabuleiro_jogador2[linha][coluna] == 'X' or tabuleiro_jogador2[linha][coluna] == 'O':
                        print("Posição já foi atacada! Escolha outra.")
                    else:
                        realizar_ataque(tabuleiro_jogador2, linha, coluna)
                        if verificar_vitoria(tabuleiro_jogador2):
                            print("\nParabéns! Você venceu!")
                            return
                        break
                else:
                    print("Posição inválida! Tente novamente.")
        else:
            print("\nVez do Computador:")
            linha = random.randint(0, tamanho_tabuleiro - 1)
            coluna = random.randint(0, tamanho_tabuleiro - 1)
            print(f"O computador ataca a posição {ALFABETO[coluna]}{linha + 1}")
            realizar_ataque(tabuleiro_jogador1, linha, coluna)
            if verificar_vitoria(tabuleiro_jogador1):
                print("\nO Computador venceu!")
                return

        vez_do_jogador1 = not vez_do_jogador1

def main():
    while True:
        jogar_batalha_naval()
        resposta = input("Deseja jogar novamente? (s/n): ").lower()
        if resposta != 's':
            print("Obrigado por jogar! Até a próxima!")
            break

if __name__ == "__main__":
    main()