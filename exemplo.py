def calcular_calorias(tempo, intensidade):
    #
    calorias_por_minuto = 5 
    calorias_totais = tempo = calorias_por_minuto * intensidade
    
    return calorias_totais 

    # Exemplo de uso 
tempo_atividade = int(input("Digite o tempo de atividade em minutos: ")) # em minutos 
intensidade_atividade = int(input("Digite a intensidade da atividade: ")) # fator de intensidade 

calorias_gastas = calcular_calorias(tempo_atividade, intensidade_atividade)
print(f"Você queimou {calorias_gastas} calorias durante a ativiadade")
