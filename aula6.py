def calcular_peso_comida():
    #Solicitar ao usuario que insira os pesos dos alimentos 
    peso_carne = float(input("Digite o peso da carne(em gramas): "))
    peso_legumes = float(input("Digite o peso da legumes(em gramas): "))
    peso_arroz = float(input("Digite o peso da arroz(em gramas): "))
    
     # Calcular o peso total da comida 
    peso_total = peso_carne + peso_arroz + peso_legumes 
     
    # Exibir o resultado 
    print(f"O peso total da comida é: {peso_total} gramas")
    
    # Chamar a função
    calcular_peso_comida() 
     