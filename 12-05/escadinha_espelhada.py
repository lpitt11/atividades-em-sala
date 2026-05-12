n = int(input("Digite o número de degraus: "))

for i in range(1, n + 1):
    espaco = n - i
    x = i * 2
    print(" " * espaco + "X" * x)