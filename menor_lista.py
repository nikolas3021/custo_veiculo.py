# Função para encontrar o menor número na lista de forma segura e eficiente
def encontrar_menor(lista):
    if not lista:  # Verifica se a lista não está vazia
        raise ValueError("A lista não pode estar vazia")
    return min(lista)  # Usa a função embutida `min()`

# Lista de números
numeros = [5, 3, 9, 1, 4]

# Encontrando e exibindo o menor número na lista
try:
    menor_numero = encontrar_menor(numeros)
    print("Menor número na lista:", menor_numero)
except ValueError as e:
    print("Erro:", e)
