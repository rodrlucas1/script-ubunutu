#Definindo a operação
num1 = input("Digite o primeiro número:")
operador = input ("Escolha a operação: (+, -, *, /): ")
num2 = input("Digite o segundo número: ")

#Trocando tipo da variavel
num1 = int(num1)
num2 = int(num2)

#Codigo para realizar a operação escolhida
if operador == '+':
    resultado = num1 + num2
    print('Resultado da operação:', resultado)
elif operador == '-':
    resultado = num1 - num2
    print('Resultado da operação:', resultado)
elif operador == '*':
    resultado = num1 * num2
    print('Resultado da operação:', resultado)
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
        print('Resultado da operação:', resultado)
    else:
        print('Erro! Divisão por 0!')
