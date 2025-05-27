def mostrar_menu_principal()-> None:
    """
    Esta funcion muestra el menú principal de la aplicación.

    No recibe argumentos ni tampoco devuelve nada ya que su única función es mostrar el menú de opciones
    """
    print("\nSistema de Gestión de Clínica")
    print("1. Cargar pacientes")
    print("2. Mostrar todos los pacientes")
    print("3. Buscar pacientes por numero de historia clinica")
    print("4. Ordenar pacientes por numero de historia clinica")
    print("5. Mostrar paciente con más dias de internacion")
    print("6. Mostrar paciente con menos dias de internacion")
    print("7. Cantidad de pacientes con más de 5 dias de internacion")
    print("8. Promedio de días de internacion de todos los pacientes")
    print("9. Salir")

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
            print("Debe ingresar un valor numerico entero.")