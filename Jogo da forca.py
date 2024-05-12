import random 

def escolher_palavra():
    palavras = ['python', 'desenvolvimento', 'programação', 'computador', 'algoritimo','openai',]
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6
    
    while True:
        palavra_escondida = ''.join([letra if letra in letras_corretas else '_' for letra in palavra])
        print('\nPalavra: ', palavra_escondida)
        print('letras usadas: ',','.join(letras_corretas))
        print('Tentativa Restantes:', tentativas)
        
        if palavra_escondida == palavra:
            print("\nParabéns você venceu!")
            break
        
        if tentativas == 0:
            print("\nGame Over! a palavra era:", palavra)
            break
        
        letra = input("\nDigite um Letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print('Por favor, digite apenas uma letra.')
            continue
        
        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra, Tente outra.")
            continue 
        
        if letra in palavra:
            print("Letra correta!") 
            letras_corretas.append(letra)
            
        else:
            print("Letra errada!")
            letras_erradas.append(letra)
            tentativas -= 1
            
if __name__ == '__main__':
    print('Bem vindo ao jogo da forca!')
    jogar_forca()
        
        
            