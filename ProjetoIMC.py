peso = float(input("digite seu peso em kg: "))
altura = float(input("digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "baixo peso"
elif imc < 24.9:
    classificacao = "peso adequado"
elif imc < 29.9:
    classificacao = "sobrepeso"
elif imc < 34.9:
    classificacao = "obesidade grau 1"
elif imc < 39.9:
    classificacao = "obesidade grau 2"
else:
    classificacao = "obesidade grau 3"

print(f"seu IMC é {imc:.2f}. calssificação: {classificacao}")