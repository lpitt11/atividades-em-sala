n = int(input("Digite o número de degraus: "))

for i in range(n):
    for j in range(i + 1):
        print("X", end="")
    print()