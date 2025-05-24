

def contar_elementos(lista):
    return len(lista)

def obtener_elemento(lista, indice):

    if 0 <= indice <= len(lista):
        for i in range(len(lista)):
            if i == indice:
                return lista[i]
    else:
        print("Indique un valor de indice válido.")
    
def concatenar_listas(lista1, lista2):

    nueva_lista = lista1[:]

    for i in range(len(lista2)):
        append_manual(nueva_lista, lista2[i])
    
    return nueva_lista


def append_manual(lista, elemento):

    
    if type(lista) == list:
        lista[len(lista):len(lista)] = [elemento]
    else:
        print("No ha ingresado una lista.")

