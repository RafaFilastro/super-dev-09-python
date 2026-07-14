class Cachorro:
    # __init__ é o construtor da classe, que é executado
    # quando instaciamos um objeto da classe
    def __init__(self, apelido: str, raca: str, cor: str, peso: float, idade: int):
        self.apelido = apelido
        self.raca = raca
        self.cor = cor
        self.peso = peso
        self.idade = idade

    def apresentar_dados(self):
        print(f"Cachorro: {self.apelido}")
        print(f"Raça: {self.raca}")
        print(f"Cor: {self.cor}", end="\n\n\n")

    def fazer_aniversario(self):
        self.idade = self.idade + 1
        print("Feliz aniversário!!!", self.apelido,"fez", self.idade, "anos")

tobi = Cachorro("Tobi", "Vira-Lata", "Caramelo", 25.60, 6)
# Tobi aumentou de peso
tobi.peso = 29.34
tobi.apresentar_dados()

thor = Cachorro(cor="Capa Preta", raca="Pastor Alemão", peso=38, idade=8, apelido="Thor")
thor.fazer_aniversario()
thor.apresentar_dados()

mogli = Cachorro("Mogli", "Vira-Lata", "Preto", 30, 6)
mogli.apresentar_dados()
