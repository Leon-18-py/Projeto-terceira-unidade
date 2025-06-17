import os
import webbrowser

usuarios = list()
caronas = list()
reservas = list()

print("*"*50)
print("Bem vindo!")
print("*"*50)
while(True):
    opcao = input("Escolha uma das opções\n\n" \
     "1 - Cadastrar usuário\n"\
     "2 - Listar usuários\n" \
     "3 - Buscar usuário por email\n" \
     "4 - Remover usuário por email\n" \
     "5 - Atualizar usuário por email\n" \
     "6 - Login\n"\
     "0 - Sair\n\n Opção: ")
    if(opcao == '0'):
        break
    elif(opcao == '1'):
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        while(not "@" in email or not email.endswith('.com') and "gmail" in email):
            print("Email inválido")
            email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        usuario = {
            "nome": nome,
            "email": email,
            "senha": senha
        }     
        emailRepetido = email
        encontrado = False
        for usu in usuarios:
            while(email == usu["email"]):
                encontrado = True
                print("Email já existente. Tente outro: ")
                email = input("Digite seu email: ")
                while(not "@" in email or not email.endswith('.com') and "gmail" in email):
                 print("Email inválido")
                 email = input("Digite seu email: ")
            usuario = {"nome": nome,
                 "email": email,
                 "senha": senha
                    }    
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif(opcao == '2'):
        print("\nLista de usuários\n")
        for usu in usuarios:
            print(f"Nome: {usu["nome"]}")
            print(f"Email: {usu["email"]}")     
            print("-" * 50) 
        print("\n")
    elif(opcao == '3'):
        emailBusca = input("Digite um email para busca: ")
        encontrado = False
        for usu in usuarios:
            if(emailBusca == usu["email"]):
                encontrado = True
                print("Encontrou o usuário\n\n")
                print("-" * 50)
                print(f"Nome: {usu["nome"]}")
                print(f"Email: {usu["email"]}")
                print("-" * 50)
        if(not encontrado):
            print("Usuário não existe!\n\n")
    elif(opcao == '4'):
        emailBusca = input("Digite um email para remover: ")
        indice = -1
        for ind in range(len(usuarios)):
            if(emailBusca == usuarios[ind]["email"]):
                indice = ind

        if(indice == -1):
            print("Não encontrou o usuário!")
        else:
            usuarios.pop(indice)
    elif(opcao == '5'):
        emailBusca = input("Digite um email para atualizar: ")
        indice = -1
        for ind in range(len(usuarios)):
            if(emailBusca == usuarios[ind]["email"]):
                indice = ind

        if(indice == -1):
            print("Não encontrou o usuário!")
        else:
            nomeNovo = input("Digite seu novo nome: ")
            senhaNova = input("Digite sua nova senha: ")

            usuarios[indice]["nome"] = nomeNovo
            usuarios[indice]["senha"] = senhaNova
    elif(opcao == '6'):
        email = str(input("Digite o seu email: "))
        while(not "@" in email or not email.endswith('.com') and "gmail" in email):
            print("Email inválido")
            email = input("Digite seu email: ")
        senha = input("Digite a sua senha: ")
        for ind in range(len(usuarios)):
            if(email == usuarios[ind]['email'] and senha == usuarios[ind]['senha']):
                print("Login efetivado")
                loggado = -1
                while(loggado != 0):
                    print("Menu Login")
                    print("1 - Cadastro de carona")
                    print("2 - Listar caronas")
                    print("3 - Buscar carona por origem e destino")
                    print("4 - Reservar vaga em carona")
                    print("5 - Cancelar reserva")
                    print("6 - Remover reserva")
                    print("7 - Mostrar detalhes de carona")
                    print("8 - Mostrar caronas cadastradas")
                    print("0 - Voltar menu inicial")
                    print("Escolha a opcao\n")
                    op=input("Informe a opcao: ")
                    if(op == '1'):
                        print("Cadastrando carona")
                        nomeMotorista = str(input("Digite seu nome: "))
                        localOrigem = str(input("Informe o local de origem: "))
                        destino = str(input("Informe o destino da carona: "))
                        data = str(input("Informe a data: "))
                        horario = str(input("Informe o horário: "))
                        vagas = int(input("Informe a quantidade de vagas: "))
                        valorVaga = float(input("Informe o valor da vaga: "))
                        passageiro = 0
                        carona = {
                           "nomeMotorista": nomeMotorista,
                           "localOrigem": localOrigem,
                           "destino": destino,
                           "data": data,
                           "horario": horario,
                           "vagas": vagas,
                           "valorVaga": valorVaga,
                           "email": email,
                           "passageiro": passageiro
                            }   
                        caronas.append(carona)
                        print("Cadastra feito com sucesso")
                    elif(op == '2'):
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
                    elif(op == '3'):
                        origemBusca = input("Digite um local de origem para busca: ")
                        destinoBusca = input("Digite um destino para busca: ")
                        encontrado = False
                        for car in caronas:
                            if(origemBusca == car["localOrigem"] and destinoBusca == car["destino"]):
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
                    elif(op == '4'):
                        reserv = False
                        print("Reservar a sua carona:\n")
                        emailUsuario = str(input("Informe seu email:"))
                        while(not "@" in emailUsuario or not emailUsuario.endswith('.com') and "gmail" in emailUsuario):
                            print("Email inválido")
                            emailUsuario = input("Digite seu email: ")
                        localOrigem = input("Digite o local de origem: ")
                        localDestino = input("Digite o destino da carona: ")
                        dataCarona = str(input("Informe a data da carona: "))
                        passageiro = 0
                        for car in caronas:
                            if(car["data"] == dataCarona):
                                if(car["vagas"] > 0):
                                    car["vagas"] -= 1
                                    passageiro += 1
                                    reserva = {"emailUsuario": emailUsuario,
                                               "dataCarona": dataCarona}
                                    caronas.append(passageiro)
                                    reservas.append(reserva)
                                    print("Reserva feito com sucesso\n")
                                    url_origem = localOrigem.replace("", "+")
                                    url_destino = localDestino.replace("", "+")
                                    url = f"https://www.google.com/maps/dir/{url_origem}/{url_destino}"
                                    print("Abrindo rota no Google Maps")
                                    webbrowser.open(url)
                                    reserv = True
                                    break
                                else:
                                    print("Não há vagas disponíveis")
                        
                        if (not reserv):
                            print("Carona não encontrada")
                    elif(op == '5'):
                        emailUsuario = str(input("Informe o email:"))
                        while(not "@" in emailUsuario or not emailUsuario.endswith('.com') and "gmail" in emailUsuario):
                            print("Email inválido")
                            emailUsuario = input("Digite seu email: ")
                        dataCarona = str(input("Informe a data da carona: "))
                        indice = -1
                        for ind in range(len(reservas)):
                            if(emailUsuario == reservas[ind]["emailUsuario"] and dataCarona == reservas[ind]["dataCarona"]):
                                indice = ind
                            if(indice == -1):
                                print("Reserva não encontrada")
                            else:
                                car["vagas"] += 1
                                passageiro -= 1
                                print("Reserva excluída")
                                reservas.pop(indice)
                    elif(op == '6'):
                        dataCarona = str(input("Informe a data da carona: "))
                        indice = -1
                        for ind in range(len(caronas)):
                            if(dataCarona == caronas[ind]["data"]):
                                indice = ind
                            if(indice == -1):
                                print("Carona não encontrada")
                            else:
                                print("Carona Removida")
                                caronas.pop(indice)
                    elif(op == '7'):
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
                    elif(op == '8'):
                      if(email == carona["email"]):
                        for car in caronas:
                            print(f"Origem: {car["localOrigem"]}")
                            print(f"Destino: {car["destino"]}")
                            print(f"Horario: {car["horario"]}")
                            print(f"Quantidade de vagas restantes: {car["vagas"]}")
                            print(f"Valor da vaga: {car["valorVaga"]}")
                            print(f"Passageiros: {car["passageiro"]}")
                      else:
                          print("Nenhuma carona cadastrada")
                    elif(op == '0'):
                        print("Voltando ao menu cadastro")
                        break
        else:
         print("Login inválido!")
    else:
        print("Opção inválida")