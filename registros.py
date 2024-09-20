# Classe Carro representa um carro com seus atributos e métodos
class Carro:
    def __init__(self, codigo, cor, fabricante, valor, modelo, ano):
        # Atributos da classe Carro
        self.codigo = codigo  # Código do carro
        self.cor = cor        # Cor do carro
        self.fabricante = fabricante  # Fabricante do carro
        self.valor = valor    # Valor do carro
        self.modelo = modelo  # Modelo do carro
        self.ano = ano        # Ano do carro

    # Método para calcular parcelas com base na quantidade de parcelas solicitadas
    def calcular_parcelas(self, quantidade_parcelas):
        return self.valor / quantidade_parcelas

    # Método para exibir os dados do carro
    def exibir_dados(self):
        print(f"Código: {self.codigo}, Cor: {self.cor}, Fabricante: {self.fabricante}, "
              f"Valor: R${self.valor:.2f}, Modelo: {self.modelo}, Ano: {self.ano}")

# Criando objetos da classe Carro e solicitando dados ao usuário
codigo = input("Digite o código do carro: ")
cor = input("Digite a cor do carro: ")
fabricante = input("Digite o fabricante do carro: ")
valor = float(input("Digite o valor do carro: "))
modelo = input("Digite o modelo do carro: ")
ano = input("Digite o ano do carro: ")

# Gerando um objeto da classe Carro
carro = Carro(codigo, cor, fabricante, valor, modelo, ano)

# Exibindo dados do carro
carro.exibir_dados()

# Solicitando a quantidade de parcelas e exibindo o valor de cada parcela
quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
valor_parcela = carro.calcular_parcelas(quantidade_parcelas)
print(f"Valor de cada parcela: R${valor_parcela:.2f}")
