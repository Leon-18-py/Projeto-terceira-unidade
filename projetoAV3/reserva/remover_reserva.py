def cancelar_reserva(reservas, caronas):
    emailUsuario = input("Informe o email: ")
    while not ("@" in emailUsuario and emailUsuario.endswith('.com') and "gmail" in emailUsuario):
        print("Email inválido")
        emailUsuario = input("Digite seu email: ")

    dataCarona = input("Informe a data da carona: ")
    indice = -1

    for i in range(len(reservas)):
        if emailUsuario == reservas[i]["emailUsuario"] and dataCarona == reservas[i]["dataCarona"]:
            indice = i
            break  

    if indice == -1:
        print("Reserva não encontrada")
        return

    for car in caronas:
        if (car["data"] == dataCarona and car["email"] == reservas[indice]["emailUsuario"]):
            car["vagas"] += 1
            car["passageiro"] -= 1
            break

    reservas.pop(indice)
    print("Reserva cancelada com sucesso.")
