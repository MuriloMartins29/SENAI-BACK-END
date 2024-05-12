vetor1 = [1,2,3]
vetor2 = [4,5,6]
soma_vetores = [a + b for a,b in zip(vetor1, vetor2)]
# Produto de matrizes 
matriz1 = [(1,2)], [(3,4)]
matriz2 = [(5,6)], [(7,8)]
produto_matrizes = [(sum(x*y for x,y in zip(matriz1, matriz2)))]