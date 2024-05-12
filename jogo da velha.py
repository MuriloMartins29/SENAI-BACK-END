def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' | '.join(linha))
        print("-" * 9)
        
def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verificar Diagonais 
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True 

    return False

def jogo_da_velha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogadores = ['X', 'O']
    jogador_atual = 0
    
    print("Bem vindo ao jogo da velha!")
    imprimir_tabuleiro(tabuleiro)
    
    for _ in range(9):
        while True:
            try:
                linha = int(input(f'jogador {jogadores[jogador_atual]}, digite a linha (0-2): '))
                coluna = int(input(f'jogador {jogadores[jogador_atual]}, digite a coluna (0-2): '))
        
                if linha <= 0 or coluna <= 0 or (linha == 0 or coluna == 0):
                    print("Por favor, digite um número inteiro positivo...")
                    continue       
        
                if tabuleiro[linha][coluna] != " ":
                    print("Posição ocupada, tente novamente...")
                    continue
        
                break
            except ValueError:
                print("Por favor, Digite um número inteiro.")

        tabuleiro[linha][coluna] = jogadores[jogador_atual]
        imprimir_tabuleiro(tabuleiro)
        
        if verificar_vitoria(tabuleiro, jogadores[jogador_atual]):
            print(f"Parabéns! Jogador {jogadores[jogador_atual]} venceu!")
            return
        
      
        jogador_atual = (jogador_atual + 1) % 2 
    
            
    else:
        print("Empate!")
            
if __name__ == '__main__':
    jogo_da_velha()
                
            