def mostrar_menu_principal()-> None:
    """
    Esta funcion muestra el menú principal de la aplicación.

    No recibe argumentos ni tampoco devuelve nada ya que su única función es mostrar el menú de opciones
    """
    print("\n*** Menú Principal ***")
    print("1 - Cargar productos")
    print("2 - Buscar producto")
    print("3 - Ordenar inventario")
    print("4 - Mostrar producto más caro y más barato")
    print("5 - Mostrar producto con precio mayor a 15000")
    print("0 - Salir")

def leer_opcion(prompt: str, minimo: int, maximo: int) -> int:
    """
    Esta funcion lee una opción del menú y verifica que esté dentro de un rango válido.

    Args:
        prompt (str): Mensaje a mostrar al usuario.
        minimo (int): Valor mínimo permitido.
        maximo (int): Valor máximo permitido.

    Returns:
        int: Opción válida ingresada por el usuario.
    """
    while True:
        opcion_elegida = input(prompt)

        if opcion_elegida.isdigit():
            opcion_elegida = int(opcion_elegida)
            if minimo <= opcion_elegida <= maximo:
                return opcion_elegida
            else:
                print(f"El valor ingresado debe estar en el rango: {minimo} - {maximo}")
        else:
            print("Debe ingresar un valor numerico.")

# TEST
""" opcion = -1

while opcion != 0:

    mostrar_menu_principal()
    opcion = leer_opcion("Ingrese una opción: ", 0, 5)
    match opcion:
        case 0:
            print("Saliendo del programa...")
        case 1:
            print("Cargando productos...")
        case 2:
            print("Buscando producto...")
        case 3:
            print("Ordenando inventario...")
        case 4:
            print("Mostrando producto más caro y más barato...")
        case 5:
            print("Mostrando producto con precio mayor a 15000...")
        case _:
            print("Opción no válida. Intente nuevamente.") """
        