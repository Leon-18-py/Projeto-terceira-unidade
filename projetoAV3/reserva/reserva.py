import webbrowser
def reservar_carona(caronas, reservas):
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