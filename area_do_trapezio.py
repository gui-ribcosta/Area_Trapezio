def calculo(Base_maior,base_menor,altura):
    area = (Base_maior+base_menor)*altura/2
    return area


B = float(input("Digite o valor da base maior do trapézio: "))
b = float(input("Digite o valor da base menor do trapézio: "))
h = float(input("Digite o valor da altura do trapézio: "))

print(f"Área: {calculo(Base_maior,base_menor,altura)} m²")