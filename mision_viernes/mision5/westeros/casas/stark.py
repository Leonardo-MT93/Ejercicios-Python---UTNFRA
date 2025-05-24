casa_stark = "Stark"

miembros_stark = [" - Kaelen - ", " - Nyra - ", " - Thorne - "]

lema_stark = "Que el trueno nos guíe"

def obtener_miembros():
    return miembros_stark

def obtener_lema():
    return lema_stark

def obtener_integrantes_por_indice():
    integrantes = ""
    for i in range(len(miembros_stark)):
        integrantes += f"\nStark {i} - {miembros_stark[i]}"
    return integrantes

def mostrar_informacion():

    print(f"\nCasa: {casa_stark}")
    print(f"\nEl lema de la familia Stark - {lema_stark}")
    print(f"\nIntegrantes: {obtener_integrantes_por_indice()}")

