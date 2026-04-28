a = []
for i in range(10):
    num = int(input(f"Digite o {i+1}o número inteiro: "))
    a.append(num)

print("Lista:", a)

maior = max(a)
menor = min(a)
print("Maior número:", maior)
print("Menor número:", menor)