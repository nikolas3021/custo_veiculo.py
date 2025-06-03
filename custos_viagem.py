class Veiculo:
    def __init__(self, modelo, consumo_km_por_litro, preco_combustivel):
        self.modelo = modelo
        self.consumo_km_por_litro = consumo_km_por_litro
        self.preco_combustivel = preco_combustivel

    def calcular_custo_viagem(self, distancia_km):
        litros_necessarios = distancia_km / self.consumo_km_por_litro
        return litros_necessarios * self.preco_combustivel

class Carro(Veiculo):
    def __init__(self, modelo, consumo_km_por_litro, preco_combustivel, portas):
        super().__init__(modelo, consumo_km_por_litro, preco_combustivel)
        self.portas = portas

class Moto(Veiculo):
    def __init__(self, modelo, consumo_km_por_litro, preco_combustivel, cilindradas):
        super().__init__(modelo, consumo_km_por_litro, preco_combustivel)
        self.cilindradas = cilindradas

class Caminhao(Veiculo):
    def __init__(self, modelo, consumo_km_por_litro, preco_combustivel, capacidade_carga):
        super().__init__(modelo, consumo_km_por_litro, preco_combustivel)
        self.capacidade_carga = capacidade_carga

# Criando uma lista de veículos
veiculos = [
    Carro("Sedan", 12, 6.50, 4),
    Moto("Esportiva", 20, 6.50, 600),
    Caminhao("Caminhão Grande", 5, 6.50, 2000)
]

# Calculando o custo total da viagem de 200 km
distancia_viagem = 200
custo_total = 0

print("Custos individuais da viagem de 200 km:")
for veiculo in veiculos:
    custo = veiculo.calcular_custo_viagem(distancia_viagem)
    print(f"{veiculo.modelo}: R$ {custo:.2f}")
    custo_total += custo

print(f"\nCusto total da viagem para todos os veículos: R$ {custo_total:.2f}")
