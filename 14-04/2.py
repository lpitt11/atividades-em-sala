limite = int(input("Digite um número inteiro positivo: "))
soma = 0
contador = 0
while contador <= limite:
    if contador % 2 == 0:
        soma += contador
    contador += 1
print(f"A soma dos números pares até {limite} é: {soma}")
