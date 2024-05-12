class Pessoa:
    def __init__(self, nome, idade, altura) -> None:
        self.nome = nome
        self.idade = idade
        self.altura = altura 
#Criando instâncias da classe Pessoa
pessoa1 = Pessoa("Dean","20","1,86")
pessoa2 = Pessoa("Alice","35","1,65")
pessoa3 = Pessoa("Bob","40","1,80")

# #Acessando os atributos
# print(pessoa1.nome)

resposta = input("Escreva seu nome: ").lower

if resposta == "Dean".lower():
    print(pessoa1.nome, pessoa1.idade, pessoa1.altura)
    
elif resposta == "Alice".lower():
    print(pessoa2.nome, pessoa2.idade, pessoa2.altura)
elif resposta == "Bob".lower():
    print(pessoa3.nome, pessoa3.idade, pessoa3.altura)
else:
    print("Nenhuma pessoa encontrada.")