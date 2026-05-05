quantidade_de_numeros = int(input("Digite a quantidade de números que deseja inserir: "))
sequencia_de_numeros = []
esta_repetindo = False
numero_repetindo = 0
quantidade_de_repeticao = 0

for i in range(quantidade_de_numeros):
    sequencia_de_numeros.append(int(input(f"Digite o número {i + 1}: ")))

for i in range(1, quantidade_de_numeros):
    if sequencia_de_numeros[i] == sequencia_de_numeros[i - 1]:
        esta_repetindo = True
    else:
        esta_repetindo = False
        numero_repetindo = 0
        quantidade_de_repeticao = 0

if esta_repetindo:
    print(f"Existe sequência de números iguais consecutivos? {True}")
else:
    print(f"Existe sequência de números iguais consecutivos? {False}")
