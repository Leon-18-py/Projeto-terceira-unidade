def logar ():
    email = str(input("Digite o seu email: "))
    while(not "@" in email or not email.endswith('.com') and "gmail" in email):
        print("Email inválido")
        email = input("Digite seu email: ")
    senha = input("Digite a sua senha: ")