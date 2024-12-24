def exibir_losango(n):
    # Parte superior do losango
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
    # Parte inferior do losango
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Defina o tamanho do losango
n = int(input("Digite o tamanho do losango (metade da altura): "))
exibir_losango(n)
input()