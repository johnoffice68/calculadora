def calculadora (n1,n2,operacao):
    
        
    if operacao == 1:
         resultado = (n1 + n2)
    elif operacao == 2:
        resultado = (n1 - n2)
    elif operacao == 3: 
        resultado = (n1 * n2)
    elif operacao == 4:
        resultado = (n1 / n2)
    else:
        resultado = ("operacao nao intentificada!! ou 0")
    return resultado
print("<--------calculadora ----------->")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
print(" lembrando que (1) e para somar, (2) para diminuir (3) para multiplicar e (4) para dividir:  ")
operacao_escolhida = int(input("Digite o número da operação desejada: "))
resultado_calculo = calculadora(numero1, numero2, operacao_escolhida)
print("Resultado:", resultado_calculo)