from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    @abstractmethod
    def exibir_info(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, "Cachorro")
        self.raca = raca

    def exibir_info(self):
        return f"Cachorro: {self.nome}, Idade: {self.idade}, Raça: {self.raca}"

class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade, "Gato")
        self.cor = cor

    def exibir_info(self):
        return f"Gato: {self.nome}, Idade: {self.idade}, Cor: {self.cor}"

# Criando o cadastro de animais
cadastro_animais = []

# Adicionando animais ao cadastro
cadastro_animais.append(Cachorro("Rex", 5, "Labrador"))
cadastro_animais.append(Gato("Mia", 3, "Preto"))

# Exibindo informações dos animais cadastrados
for animal in cadastro_animais:
    print(animal.exibir_info())
