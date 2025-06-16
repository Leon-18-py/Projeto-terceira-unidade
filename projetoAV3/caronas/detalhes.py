def detalheCarona (caronas):
    email = str(input("Informe o email: "))
    while(not "@" in email or not email.endswith('.com') and "gmail" in email):
        print("Email inválido")
        email = input("Digite seu email: ")
    dataCarona = str(input("Informe a data da carona: "))
    for car in caronas:
        if(dataCarona == car["data"] and email == car["email"]):
            print(f"Origem: {car["localOrigem"]}")
            print(f"Destino: {car["destino"]}")
            print(f"Horário: {car["horario"]}")
            print(f"Valor da vaga: {car["valorVaga"]}")
            print(f"Vagas restantes: {car["vagas"]}")
            print(f"Quantidade de passageiros: {car["passageiro"]}")
        else:
            print("Carona não encontrada")