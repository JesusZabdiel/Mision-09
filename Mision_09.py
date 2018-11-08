#Jesús Zabdiel Sánchez Chávez A01374964

#Mioson 09

def extraerPares(lista):
    listaNueva = []
    for x in lista:
        if x % 2 == 0:
            listaNueva.append(x)
    return listaNueva

def extraerMayoresPrevio(lista):
    listaNueva = []
    for x in range (len(lista)):
        if x+1 < len(lista):
            if lista[x+1] > lista[x]:
                listaNueva.append(lista[x+1])
    return listaNueva


def intercambiarParejas(lista):
    listaNueva = []
    if len(lista) > 1:
        for x in range(0, len(lista), 2):

            if x + 2 < len(lista):
                listaNueva.append(lista[x+1])
                listaNueva.append(lista[x])
            elif x == len(lista):
                listaNueva.append(lista[x])
        listaNueva.append(lista[len(lista)-1])

    elif len(lista) <= 1:
        listaNueva = lista[:]

    return listaNueva


def intercambiarMM(lista):
    numeroMenor = lista[0]
    numeroMayor = lista[0]
    for x in range(len(lista)):
        if x + 1 <= len(lista):
            if lista[x] <= numeroMenor:
                numeroMenor = lista[x]
                indiceMenor  = x
            if lista [x] >= numeroMayor:
                numeroMayor = lista[x]
                indiceMayor = x

    lista.remove(numeroMayor)
    lista.insert(indiceMayor,numeroMenor)
    lista.remove(numeroMenor)
    lista.insert(indiceMenor,numeroMayor)
    return lista


def promediarCentro(lista):
    listaNueva = lista[:]
    numeroMenor = lista[0]
    numeroMayor = lista[0]

    for x in range(len(lista)):
        if x + 1 <= len(lista):
            if lista[x] <= numeroMenor:
                numeroMenor = lista[x]

            if lista[x] >= numeroMayor:
                numeroMayor = lista[x]

    listaNueva.remove(numeroMayor)
    listaNueva.remove(numeroMenor)

    centro = sum(listaNueva)//len(listaNueva)

    return centro

def calcularEstadistica(lista):
    if len(lista) > 1:
        mean = sum(lista) / len(lista)
        sumaT = 0
        for x in lista:
            sumaR = ((x-mean)**2)
            sumaT += sumaR

        deviation = (sumaT/(len(lista)-1))**.5


        return  mean , deviation
    elif len(lista) ==1:
        return lista[0] , 0
    else:
        return 0 , 0


def calcularSuma (lista):
    listaNueva = lista[:]

    for x in range (len(lista)):
        if lista[x] == 13:
            if len(lista) > 2 and len(lista) > x+1 :
                listaNueva.remove(lista[x+1])
                listaNueva.remove(lista[x-1])
                listaNueva.remove(lista[x])


            else:
                if len(lista) - 1 == x:
                    listaNueva.remove(lista[x])
                    listaNueva.remove(lista[x - 1])

                    return sum(listaNueva)


                for x in lista:
                    if x == 13:
                        return 0
                return sum(listaNueva)



    return sum(listaNueva)
