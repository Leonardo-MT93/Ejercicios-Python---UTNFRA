casa_lannister = "Lannister"

miembros_lannister = [" - Veyra - ", " - Malrik - ", " - Saria - "]

lema_lannister = "El veneno es paciencia"

def obtener_miembros():
    return miembros_lannister

def obtener_lema():
    return lema_lannister

def obtener_integrantes_por_indice():
    integrantes = ""
    for i in range(len(miembros_lannister)):
        integrantes += f"\nLannister {i} - {miembros_lannister[i]}"
    return integrantes

def mostrar_informacion():

    print(f"\nCasa: {casa_lannister}")
    print(f"\nEl lema de la familia Lannister - {lema_lannister}")
    print(f"\nIntegrantes: {obtener_integrantes_por_indice()}")




