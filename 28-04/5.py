numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

maior_par = max([n for n in numeros if n% 2 == 0], default=None)
menor_impar = min([n for n in numeros if n% 2 != 0], default=None)
soma = sum(numeros)
media = soma / len(numeros) if numeros else 0

print("Maior número par:", maior_par)
print("Menor número ímpar:", menor_impar)
print("Somatório dos elementos:", soma)
print("Média dos elementos:", media)
