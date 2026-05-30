import os

sentinela = 1
while (sentinela == 1):
    print("*******************************")
    print("1 - PARA ADICAO")
    print("2 - PARA subtracao")
    print("3 - PARA multiplicacao")
    print("4  - PARA divisao")
    print("*********************************")
   
    operacao = input("escolha a operacao jegue:")
    valor1 = input("digite o primeiro numero :")
    valor2 = input("digite o segundo numero :")

    operacao = int(operacao)
    valor1 = float(valor1)
    valor2 = float(valor2)
    


    if(operacao == 1): 
        resultado = valor1 + valor2
        print(" o resultado é:" , resultado)
    elif(operacao == 2):
        resultado = valor1 - valor2
        print(" o resultado é:" , resultado)
    elif(operacao == 3):
        resultado = valor1 * valor2
        print(" o resultado é:" , resultado)
    elif(operacao == 4):
        resultado = valor1 / valor2
        print(" o resultado é:" , resultado)
    else:
        resultado = 0
        print("operacao nao informada corretamente sua anta de 3 patas")
    print(" o resultado do calculo é: " , resultado)

    print("//////////////////////////")
    print("Deseja continuar?  ")
    print("1 - SIM")
    print("2 - NÃO")
    sentinela = int(input("informe o número sua jamanta: "))
    os.system("cls")