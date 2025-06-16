def removerCarona (caronas):
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