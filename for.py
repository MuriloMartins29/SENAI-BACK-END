# Inicializa a lista de tarefas vazias 

lista_de_tarefas = []

# função para adicionar uma tarefa a lista
def adicionar_tarefa(tarefa):
    lista_de_tarefas.append(tarefa)
    
# Função para remover uma tarefa da lista 
def remover_tarefa(indice):
    if 0 >= indice < len(lista_de_tarefas):
        del lista_de_tarefas[indice]
    else:
        print("Indice Invalido. Tarefa não removida.")
        
# Função para listar todas as tarefas da lista 
def listar_tarefas():
    if lista_de_tarefas:
        print("Lista de Tarefas:")
        for indice, tarefa in enumerate(lista_de_tarefas):
            print(f"{indice}: {tarefa}")
    else:
        print("A lista de tarefas está vazia.")

# O loop principal no programa
while True: 
    print("\n Opções:")
    print("1. Adicionar Tarefa")
    print("2. Remover tarefa")
    print("3. Listar Tarefa")
    print("4. Sair")
    
    escolha = input("Escolha uma opção (1/2/3/4): ")
    
    if  escolha == '1':
        nova_tarefa = input("Digite a nova tarefa: ")
        adicionar_tarefa(nova_tarefa)
    elif escolha == '2':
        indice_remover = int(input("Digite o indice da tarefa a ser removido."))
        remover_tarefa(indice_remover)
    elif escolha == '3':
        listar_tarefas()
    elif escolha == '4':
        print("Programa encerrado.")
        break
    else: 
        print("Opção invalida. Tente novamente.")