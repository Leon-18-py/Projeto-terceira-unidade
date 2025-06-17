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
                with open(caminho, 'w', encoding='utf-8') as arquivo:
                    arquivo.write(f"Origem: {car["localOrigem"]}")
                    arquivo.write(f"Destino: {car["destino"]}")
                    arquivo.write(f"Horario: {car["horario"]}")
                    arquivo.write(f"Data: {car["data"]}")
                    arquivo.write(f"Valor da vaga: {car["valorVaga"]}")
                    arquivo.write(f"Quantidade de vagas restantes: {car["vagas"]}")
                    arquivo.write(f"Total a receber: {total}")
                    arquivo.write(f"Total de todas as caronas: {totalcar}")
                break
            elif(salvar == "n"):
                break
        else:
            print("Nenhuma carona cadastrada")
