def organizar_lista(lista_baguncada):
 
    lista_agrupada = list(set(lista_baguncada))
    
    crescente = sorted(lista_agrupada)
    decrescente = sorted(lista_agrupada, reverse=True)
    
    return crescente, decrescente

print("Sistema de Agrupamento e Ordenação")
print("Digite os números que deseja adicionar à lista.")
print("Quando terminar, digite 'fim'.\n")

numeros_digitados = []

while True:
    entrada = input("Digite um número (ou 'fim' para concluir): ")
    
    if entrada.strip().lower() == 'fim':
        break
        
    try:
       
        numero = int(entrada)
        
     
        numeros_digitados.append(numero)
        
    except ValueError:
        print("Inválida. Por favor, digite apenas números inteiros ou 'fim'.")

if len(numeros_digitados) > 0:
    print("\nVerificando\n")
    
    lista_crescente, lista_decrescente = organizar_lista(numeros_digitados)
    
    print("Resultados")
    print(f"Lista: {numeros_digitados}")
    print(f"Agrupada em Crescente:   {lista_crescente}")
    print(f"Agrupada em Decrescente: {lista_decrescente}")
else:
    print("\nNenhum número foi detectado.")