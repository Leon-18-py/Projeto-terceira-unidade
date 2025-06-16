def buscarCarona(origemBusca, destinoBusca, caronas):
    encontrado = False
    for car in caronas:
      if(origemBusca == car["localOrigem"] and destinoBusca == car["destino"] ):
        encontrado = True
        print("Encontrou a(s) carona(s)\n\n")
        print("-"*50)
        print(f"Nome do motorista: {car["nomeMotorista"]}")
        print(f"Local de origem: {car["localOrigem"]}")
        print(f"Destino: {car["destino"]}")
        print(f"Data: {car["data"]}")
        print(f"Horario: {car["horario"]}")
        print(f"Quantidade de vagas: {car["vagas"]}")
        print(f"Valor da vaga: {car["valorVaga"]}")
        print("-"*50)
    if(not encontrado):
        print("Carona não existe")