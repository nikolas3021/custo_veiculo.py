# Solicita ao usuário que insira as coordenadas separadas por vírgula
entrada = input("Digite a latitude e longitude separadas por vírgula: ")

# Converte a entrada em uma tupla de floats
coordenadas = tuple(map(float, entrada.split(",")))

# Desempacota a tupla
latitude, longitude = coordenadas

# Exibe as coordenadas
print(f"\nCoordenadas geográficas:")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
