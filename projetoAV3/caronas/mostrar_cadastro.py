def caronasCadastradas (email, caronas):
    for car in caronas:
        if(email == car["email"]):
            print(f"Origem: {car["localOrigem"]}")
            print(f"Destino: {car["destino"]}")
            print(f"Horario: {car["horario"]}")
            print(f"Quantidade de vagas restantes: {car["vagas"]}")
            print(f"Valor da vaga: {car["valorVaga"]}")
            print(f"Passageiros: {car["passageiro"]}")
        else:
            print("Nenhuma carona cadastrada")