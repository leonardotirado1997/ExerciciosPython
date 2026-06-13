# Escreva um algoritmo que aceite um valor numérico x de 0 a 100 como entrada e que calcule e exiba a letra correspondente à nota de acordo com a seguinte tabela:

x = int(input("Digite o valor de x: "))

if x < 0 or x > 100:
    print(f"Erro, os números validos são acima de 0 e abaixo de 100.")
    exit()
if x >= 90: 
    print(f"O valor {x}, então nota A ")
elif x >= 80:
    print(f"O valor {x}, então nota B")
elif x >= 70:
    print(f"O valor {x}, então nota C")
elif x >= 60:
    print(f"O valor {x}, então nota D")
else: 
    print(f"Valor {x}, abaixo de 60, então Nota E")

