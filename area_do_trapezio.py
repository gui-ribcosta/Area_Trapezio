def calculo(Base_maior,base_menor,altura):
    area = (Base_maior+base_menor)*altura/2
    return area


Base_maior = float(input("Digite o valor da base maior do trapézio: "))
base_menor = float(input("Digite o valor da base menor do trapézio: "))
altura = float(input("Digite o valor da altura do trapézio: "))

print(f"Área: {calculo(Base_maior,base_menor,altura)} m²")