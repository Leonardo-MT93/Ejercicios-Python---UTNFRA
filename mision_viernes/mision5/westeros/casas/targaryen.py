casa_targaryen = "Targaryen"

miembros_targaryen = [" - Draeth - ", " - Selene - ", " - Vorn - "]

lema_targaryen = "Nacidos del fuego, forjados en hierro"


def obtener_miembros():
    return miembros_targaryen

def obtener_lema():
    return lema_targaryen

def obtener_integrantes_por_indice():
    integrantes = ""
    for i in range(len(miembros_targaryen)):
        integrantes += f"\nTargaryen {i} - {miembros_targaryen[i]}"
    return integrantes

def mostrar_informacion():

    print(f"\nCasa: {casa_targaryen}")
    print(f"\nEl lema de la familia Targaryen - {lema_targaryen}")
    print(f"\nIntegrantes: {obtener_integrantes_por_indice()}")





