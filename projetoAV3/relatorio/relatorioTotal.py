def receberTotal (email, caronas):
    for car in caronas:
        if(email == car["email"]):
            print(f"Origem: {car["localOrigem"]}")
            print(f"Destino: {car["destino"]}")
            print(f"Horario: {car["horario"]}")
            print(f"Data: {car["data"]}")
            print(f"Valor da vaga: {car["valorVaga"]}")
            print(f"Quantidade de vagas restantes: {car["vagas"]}")
            total = car["valorVaga"] * car["passageiro"]
            print(f"Total a receber: {total}")
            totalcar = 0
            totalcar += total
            print(f"Total de todas as caronas: {totalcar}")
            salvar = input("Você quer salvar o relatório? s/n: ")
            if(salvar == "s"):
                print("Relatório salvo")
            elif(salvar == "n"):
                break
        else:
            print("Nenhuma carona cadastrada")