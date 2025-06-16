def listar_carona(caronas):
    print("\nLista de caronas\n")
    for car in caronas:
        print(f"Nome do motorista: {car["nomeMotorista"]}")
        print(f"Local de origem: {car["localOrigem"]}")
        print(f"Destino: {car["destino"]}")
        print(f"Data: {car["data"]}")
        print(f"Horario: {car["horario"]}")
        print(f"Quantidade de vagas: {car["vagas"]}")
        print(f"Valor da vaga: {car["valorVaga"]}")
        print("-"*50)
    print("\n")