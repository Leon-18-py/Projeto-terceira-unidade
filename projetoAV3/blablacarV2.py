import os
import caronas.adcionar_carona as addcar
import caronas.listar_carona as listca
import caronas.buscarCarona as busca
import usuarios.cadastrarUsuario as cadastro
import usuarios.login as login
import reserva.reserva as reserva
import reserva.remover_reserva as remover
import caronas.remover_carona as removerca
import caronas.detalhes as detalhe
import caronas.mostrar_cadastro as mostrar
import relatorio.relatorioTotal as rela
caminho = "C:\\Users\\COMPUTER\\Downloads\\Python_VS_code\\projetoAV3\\usuarios\\usuarios.txt"
usuarios = list()
caronas = list()
reservas = list()

print("*"*50)
print("Bem vindo!")
print("*"*50)
while(True):
    opcao = input("Escolha uma das opções\n\n" \
     "1 - Cadastrar usuário\n"\
     "2 - Login\n"\
     "0 - Sair\n\n Opção: ")
    if(opcao == '0'):
        break
    elif(opcao == '1'):
        cadastro.cadastrarUsuario(usuarios)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif(opcao == '2'):
        for ind in usuarios:
         senha = ind['senha']
         email = ind['email']
        login.logar()
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
                    print("6 - Remover carona")
                    print("7 - Mostrar detalhes de carona")
                    print("8 - Mostrar caronas cadastradas")
                    print("0 - Voltar menu inicial")
                    print("Escolha a opcao\n")
                    op=input("Informe a opcao: ")
                    if(op == '1'):
                       addcar.adicionar_carona(caronas, email)
                    elif(op == '2'):
                        listca.listar_carona(caronas)
                    elif(op == '3'):
                        origemBusca = input("Digite um local de origem para busca: ")
                        destinoBusca = input("Digite um destino para busca: ")
                        busca.buscarCarona(origemBusca, destinoBusca, caronas)
                    elif(op == '4'):
                        reserva.reservar_carona(caronas, reservas)
                    elif(op == '5'):
                        remover.cancelar_reserva(reservas, caronas)
                    elif(op == '6'):
                        removerca.removerCarona(caronas)
                    elif(op == '7'):
                        detalhe.detalheCarona(caronas)
                    elif(op == '8'):
                      mostrar.caronasCadastradas(email, caronas)
                    elif(op == '9'):
                        rela.receberTotal(email, caronas)
                    elif(op == '0'):
                        print("Voltando ao menu cadastro")
                        break
        else:
         print("Login inválido!")
    else:
        print("Opção inválida")

