def switch_case(case):
    switcher = {
        1: 'Está é a execução de Case 1',
        2: 'Está é a execução de Case 2',
        3: 'Está é a execução de Case 3',
        4: 'Está é a execução de Default'
    }
    return switcher.get(case, "Opção Inválida")

opçao = int(input("Digite uma opção (1 a 4): "))
resultado = switch_case(opçao) 
print(resultado)
