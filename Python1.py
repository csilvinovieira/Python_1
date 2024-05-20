def calculadora (num1, num2, operacao):
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 + num2
    elif operacao == "*":
        resultado = num1 + num2
    elif operacao == "/":
        if num2 == 0:
            print("Erro:Divisão por zero.")
            return 0
        else:
            resultado = num1 / num2
    else:
        print("Operacao inválida.")
        return 0
    return resultado

