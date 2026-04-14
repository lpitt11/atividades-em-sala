#Média de uma lista de números:
#Peça ao usuário para fornecer uma lista de números e então calcule a média
#desses números utilizando um loop (for).

numeros = input("Digite uma lista de números separados por espaço: ")
lista_numeros = [int(num) for num in numeros.split()]
soma = 0
for num in lista_numeros:
    soma += num
media = soma / len(lista_numeros) if lista_numeros else 0
print(f"A média dos números fornecidos é: {media}")
