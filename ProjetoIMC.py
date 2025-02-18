def calcular_imc(peso, altura):
    imc = peso / (altura **2)

    if imc < 18.5:
        return f"seu IMC é {imc:.2f}. classificação: baixo peso."
    elif 18.5 <= imc < 24.9:
        return f"Seu IMC é {imc:.2f}. classificação: peso adequado."
    elif 25 <= imc < 29.9:
        return f"seu IMC é {imc:.2f}. classificação: sobrepeso."
    elif 30 <= imc < 34.9:
        return f"seu IMC é {imc:.2f}. classificação: Obessidade Grau 1."
    elif 35 <= imc < 39.9:
        return f"seu IMC é {imc:.2f}. classificação: Obessidade Grau 2."
    else:
        return f"seu IMC é {imc:.2f}. classificação: Obessidade Grau 3."
peso = float(input("digite seu peso em kg: "))

altura = float(input("digite sua altura em metros: "))

resultado = calcular_imc(peso, altura)

print(resultado)