# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Conta e exibe o número de caracteres na frase
print(f"\nNúmero de caracteres na frase: {len(frase)}")
# Conta e exibe o número de palavras na frase
print(f"\nNúmero de palavras na frase: {len(frase.split())}")
