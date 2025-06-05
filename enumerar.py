# Solicita ao usuário que insira nomes separados por vírgula
nomes = input("Digite uma lista de nomes separados por vírgula: ").split(",")

# Remove espaços extras ao redor dos nomes
nomes = [nome.strip() for nome in nomes]

# Itera sobre a lista com enumerate
print("\nLista de nomes enumerada:")
for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")
