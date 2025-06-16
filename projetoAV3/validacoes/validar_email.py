def validarEmail(email):
    if("@" in email and email.endswith(".com") and "gmail" in email):
        return True
    else:
        return False

def obterEmail():
    email = input("Digite o email: ")
    while True:
        eValido = validarEmail(email)
        if(eValido):
            break
        else:
            print("Email inválido")
            email = input("Digite o email: ")