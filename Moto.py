from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa, ano)
        self.__cilindradas = cilindradas
    def __str__(self):
        #Invoco o método __str__() da SUPERCLASSE (Veículo)
        #Armazeno o retono na variável "retorno"
        retorno = super().__str__()
        #Retorno a concatenação do valor da variável
        # "retorno" com as "__cilidradas"
        return f'''{retorno}
- Cilindradas: {self.__cilindradas}'''

