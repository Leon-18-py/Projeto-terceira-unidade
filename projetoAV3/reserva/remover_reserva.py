def cancelar_reserva(reservas,caronas):
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
        for car in caronas:
            if(vagas == car["vagas"] and passageiro == car["passageiro"]):
              vagas += 1
              passageiro -= 1
              print("Reserva excluída")
              reservas.pop(indice)