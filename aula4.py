numero = int(input("Digite um numero: "))

if numero > 0: 
    print("O numero é positivo.")
elif numero < 0:
    print("O numero é negativo.")
else:
    print("O numero é zero.") 

    idade = int(input("Digite sua idade: "))

if idade > 15 and idade < 15 or idade > 70: 
    print("O voto é opcional.")
elif idade < 16:
    print("Você não pode votar")
else:
    print("Você pode é obrigado a votar")