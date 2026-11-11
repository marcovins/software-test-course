class ALUNO_ACADEMIA:
    def __init__(self, nome, sexo, peso, altura, idade):
        self.nome = nome
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.idade = idade

    def calcular_imc(self):
        if self.peso <= 0 or self.altura <= 0:
            raise ValueError("Peso e altura devem ser maiores que zero.")
        return self.peso / (self.altura * self.altura)

    def is_vip(self):
        imc = self.calcular_imc()
        sexo = self.sexo.strip().lower()
        if sexo in ("m", "masculino", "homem"):
            limite = 30 if self.idade >= 40 else 28
        elif sexo in ("f", "feminino", "mulher"):
            limite = 28 if self.idade >= 40 else 26
        else:
            raise ValueError("Sexo deve ser masculino ou feminino.")
        return imc < limite
