def cadastrarUsuario (usuarios):
    caminho = "C:\\Users\\COMPUTER\\Downloads\\Python_VS_code\\projetoAV3\\usuarios\\usuarios.txt"
    with open(caminho, '+a', encoding='utf-8') as arquivo:
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
        for usu in usuario:
            arquivo.write(usuarios + '\n')