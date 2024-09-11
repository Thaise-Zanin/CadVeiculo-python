from Veiculo import Veiculo
from Moto import Moto

#Instânciando a classe moto
falcon = Moto("Honda", "Falcon NX4", "abc", 2005, 400)
#Exibir uma informação na tela
#Vai imprimir o RETORNO do método "__str__()"
print(falcon.__str__())

#Instânciando a classe veículo
cerato = Veiculo("Kia", "Cerato", "IRL", 2011)

print(cerato.__str__())

