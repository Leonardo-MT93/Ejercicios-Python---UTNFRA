from utilidades.menu import leer_opcion
from validaciones.validar_entrada import es_lista, es_numero_entero

def cargar_pacientes(listado_pacientes: list[list]) -> None:
    """
    Carga pacientes manualmente en una matriz de pacientes.
    
    Args:
        listado_pacientes (list[list]): Matriz en donde se cargarán los pacientes.
    Returns:
        None: No devuelve nada, solo carga los productos en la matriz.
    """

    if not es_lista(listado_pacientes):
        print("Debe ingresar un listado de pacientes.")
        return
    cantidad_pacientes = leer_opcion("Ingrese la cantidad de pacientes a cargar: ", 1, 100)

    salir = 0

    while salir < cantidad_pacientes:

        num_historia_clinica = int(input("Ingrese el numero de historia clinica del paciente: "))
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        edad_paciente = int(input("Ingrese la edad del paciente: "))
        diagnostico_paciente = input("Ingrese el diagnostico del paciente: ")
        dias_internacion = int(input("Ingrese la cantidad de días de internacion: "))

        listado_pacientes += [[num_historia_clinica, nombre_paciente, edad_paciente, diagnostico_paciente, dias_internacion]]
        print("Usted cargo correctamente el paciente.")

        salir += 1

def mostrar_listado_pacientes(listado_pacientes: list[list]) -> None:
    """
    Muestra los los pacientes de la matriz de manera prolija.
    
    Args:
        listado_pacientes (list[list]): Matriz a mostrar.
    Returns:
        None: Utiliza print para mostrar los datos de la matriz.
    """
    if not es_lista(listado_pacientes):
        print("Debe ingresar un listado de pacientes.")
        return
    print("===================================")
    for i in range(len(listado_pacientes)):
        print(f"Num. Hist. Clínica: {listado_pacientes[i][0]}, Nombre del paciente: {listado_pacientes[i][1]}, Edad: {listado_pacientes[i][2]}, Diagnóstico: {listado_pacientes[i][3]}, Dias de internación: {listado_pacientes[i][4]}")
            
    print("===================================")

def mostrar_un_paciente(lista: list)-> None:
    """
    Esta función muestra los datos de un paciente en un string.
    
    Args:
            lista(list):    Lista donde se extraen los elementos
    Returns:
            None:    Utiliza print para mostrar los datos de la lista en un formato específico.
    
    """
    if not es_lista(lista):
        print("No ha ingresado una lista como parametro.")
        return 
    return print(f"\nPaciente encontrado: \nNum. Hist. Clínica: {lista[0]}, Nombre del paciente: {lista[1]}, Edad: {lista[2]}, Diagnóstico: {lista[3]}, Dias de internación: {lista[4]}")

def buscar_paciente(listado_pacientes: list[list], num_hc: str) -> list:
    """
    Busca un paciente en un listado de pacientes por su numero de historia clinica
    
    Args:
        listado_pacientes (list[list]): Matriz de pacientes en donde se realizará la búsqueda.
        nombre_paciente (str): Nombre del paciente a buscar.
    Returns:
        list: Devuelve el paciente buscado.
    """
    if not es_lista(listado_pacientes):
        print("Debe ingresar un listado de pacientes.")
        return

    for i in range(len(listado_pacientes)):
        if listado_pacientes[i][0] == num_hc:
            return listado_pacientes[i]
    return None

def ordenar_pacientes_ascendente(listado_pacientes: list[list])-> list[list]:
    """
    Ordena una matriz de listado de pacientes en orden ascendente según el numero de historia clinica.
    
    Args:
        listado_pacientes (list[list]): Matriz de listado de pacientes en donde se realizará el ordenamiento.
    Returns:
        listado_pacientes (list[list]): Devuelve la matriz ordenada en orden ascendente.
    """
    if not es_lista(listado_pacientes):
        print("Debe ingresar un listado de pacientes.")
        return
    #Utilizo Bubble Sort para realizar el ordenamiento ascendente
    n = len(listado_pacientes)
    for i in range(n):
        for j in range(n - i - 1):
            if listado_pacientes[j][0] > listado_pacientes[j + 1][0]:
                aux = listado_pacientes[j + 1]
                listado_pacientes[j + 1] = listado_pacientes[j]
                listado_pacientes[j] = aux
    return listado_pacientes

def buscar_paciente_mayor_dias_internacion(listado_pacientes: list[list])-> list:
    """
    Busca el paciente con mayor cantidad de dias de internacion el la matriz de pacientes.

    Args:
        listado_pacientes (list[list]): Matriz en donde se realizará la búsqueda del paciente

    Returns:
        list: Devuelve el paciente encontrado con mayor cant de dias de internacion
    """
    if not es_lista(listado_pacientes):
        print("Debe ingresar un listado de pacientes.")
        return

    cantidad_max_dias_internacion = float("-inf")
    paciente_mayor_dias = []
    
    for i in range(len(listado_pacientes)):
        if listado_pacientes[i][4] > cantidad_max_dias_internacion:
            cantidad_max_dias_internacion = listado_pacientes[i][4]
            paciente_mayor_dias = listado_pacientes[i]
    
    return paciente_mayor_dias

def buscar_paciente_menor_dias_internacion(listado_pacientes: list[list])-> list:
    """
    Busca el paciente con menor cantidad de dias de internacion el la matriz de pacientes.

    Args:
        listado_pacientes (list[list]): Matriz en donde se realizará la búsqueda del paciente

    Returns:
        list: Devuelve el paciente encontrado con menor cant de dias de internacion
    """
    if not es_lista(listado_pacientes):
        print("Debe ingresar un listado de pacientes.")
        return

    cantidad_min_dias_internacion = float("inf")
    paciente_min_dias = []
    
    for i in range(len(listado_pacientes)):
        if listado_pacientes[i][4] < cantidad_min_dias_internacion:
            cantidad_min_dias_internacion = listado_pacientes[i][4]
            paciente_min_dias = listado_pacientes[i]
    
    return paciente_min_dias

def pacientes_dias_sup_internacion(listado_pacientes: list[list], dias: int)-> int:
    """
    Busca los pacientes que superan la cantidad determinada de dias de internacion

    Args:
        listado_pacientes (list[list]): Matriz en donde se realizará la búsqueda de los pacientes

    Returns:
        int: Devuelve la cantidad de pacientes encontrados.
    """



    if not es_lista(listado_pacientes):
        print("Debe ingresar un listado de pacientes.")
        return
    if not es_numero_entero(dias):
        print("Debe ingresar un valor correcto de dias")
        return
    
    pacientes_encontrados = 0

    for i in range(len(listado_pacientes)):
        if listado_pacientes[i][4] > dias:
            pacientes_encontrados += 1
    return pacientes_encontrados

def promedio_dias_internacion(listado_pacientes: list[list])-> int | float:
    """
    Busca el promedio de dias de internacion de todos los pacientes

    Args:
        listado_pacientes (list[list]): Matriz en donde se realiza el conteo de dias de todos los pacientes ingresados

    Returns:
        int/float: Devuelve la cantidad de pacientes encontrados.
    """

    if not es_lista(listado_pacientes):
        print("Debe ingresar un listado de pacientes.")
        return

    acumulador_dias = 0
    
    for i in range(len(listado_pacientes)):
        acumulador_dias += listado_pacientes[i][4]
    return acumulador_dias / len(listado_pacientes)