def adicionar_carona(caronas, email):
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
    "horario": horario,
    "data": data,
    "vagas": vagas,
    "valorVaga": valorVaga,
    "email": email,
    "passageiro": passageiro
         }   
  caronas.append(carona)
  print("Carona cadastrada com sucesso")