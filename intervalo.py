# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Gera a sequência utilizando range
sequencia = list(range(numero + 1))

# Exibe a sequência
print("\nSequência gerada:")
print(sequencia)
for num in sequencia:
    print(num)
