
def mostrar_menu():
    print("\n--- Forjando tu Casa de Westeros ---")
    print("1 - Mostrar información de una Casa")
    print("2 - Unir miembros de dos Casas")
    print("3 - Salir")

def leer_opcion(prompt, minimo, maximo): 

    while True:
        opcion_elegida = input(prompt)

        if opcion_elegida.isdigit():
            opcion_elegida = int(opcion_elegida)
            if  minimo <= opcion_elegida <= maximo:
                return opcion_elegida
            else:
                print(f"El valor ingresado debe estar en el rango: {minimo} - {maximo}")
        else:
            print("Debe ingresar un valor numerico.")

