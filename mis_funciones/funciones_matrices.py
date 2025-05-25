from validaciones.validaciones import *
from utilidades.menu import leer_opcion
from funciones_listas import mostrar_datos

inventario = [
    ["Arroz", 1500.50, 10],
    ["Fideos", 200.99, 20],
    ["Aceite", 3000.75, 5],
    ["Sal", 50.00, 30],
    ["Azucar", 100.00, 15],
    ["Cafe", 500.00, 8],
    ["Leche", 80.00, 25],
    ["Pan", 30.00, 50],
    ["Carne", 1200.00, 12],
    ["Pescado", 1500.00, 7]
]

# Agregar validaciones de matriz y enteros. 

def buscar_max_en_matriz(matriz: list[list])-> int | float:
    """
    Busca el elemento de mayor valor numérico dentro de una matriz (lista de listas).

    Args:
        matriz (list[list]): Matriz en donde se realizará la búsqueda.

    Returns:
        int/float: El valor máximo encontrado en la matriz.
        None: Si la matriz no es válida, devuelve None.
    """
    if not es_lista(matriz):
        print("No ha ingresado una lista como parametro.")
        return None
    
    numero_max = float("-inf")

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > numero_max:
                numero_max = matriz[i][j]
    return numero_max

def buscar_min_en_matriz(matriz: list[list])-> int | float:
    """
    Busca el elemento de menor valor numérico dentro de una matriz (lista de listas).

    Args:
        matriz (list[list]): Matriz en donde se realizará la búsqueda.

    Returns:
        int/float: El valor mínimo encontrado en la matriz.
        None: Si la matriz no es válida, devuelve None.
    """
    if not es_lista(matriz):
        print("No ha ingresado una lista como parametro.")
        return
    numero_min = float("inf")

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < numero_min:
                numero_min = matriz[i][j]
    return numero_min

def precio_max_en_matriz(matriz: list[list])-> list:
    """
    Busca el producto más caro dentro de una matriz en donde el precio se encuentra en el índice 1.

    Args:
        matriz (list[list]): Matriz en donde se realizará la búsqueda del producto mas caro.

    Returns:
        list: Devuelve el producto mas caro encontrado en la matriz
    """
    if not es_lista(matriz):
        print("No ha ingresado una lista como parametro.")
        return

    producto_con_precio_max = float("-inf")
    producto_max = []
    
    for i in range(len(matriz)):
        if matriz[i][1] > producto_con_precio_max:
            producto_con_precio_max = matriz[i][1]
            producto_max = matriz[i]
    
    return producto_max

def precio_min_en_matriz(matriz: list[list])-> list:
    """
    Busca el producto más barato dentro de una matriz en donde el precio se encuentra en el índice 1.

    Args:
        matriz (list[list]): Matriz en donde se realizará la búsqueda del producto mas barato.

    Returns:
        list: Devuelve el producto mas barato encontrado en la matriz
    """
    if not es_lista(matriz):
        print("No ha ingresado una lista como parametro.")
        return
    producto_con_precio_min = float("inf")
    producto_min = []
    
    for i in range(len(matriz)):
        if matriz[i][1] < producto_con_precio_min:
            producto_con_precio_min = matriz[i][1]
            producto_min = matriz[i]
    
    return producto_min

def prod_cant_max(inventario: list[list])-> list:
    """
    Busca el producto con la cantidad máxima dentro de una matriz de inventario.
    
    Args:
        inventario (list[list]): Matriz de inventario en donde se realizará la búsqueda del producto con cantidad máxima.
    Returns:
        list: Devuelve el producto con la cantidad máxima encontrado en la matriz.
        None: Si la matriz no es válida, devuelve None.
    """
    if not es_lista(inventario):
        print("No ha ingresado una lista como parametro.")
        return
    
    cantidad_max = float("-inf")
    producto_max = []
    for i in range(len(inventario)):
        if inventario[i][2] > cantidad_max:
            cantidad_max = inventario[i][2]
            producto_max = inventario[i]
    return producto_max

#CARGA EN MATRIZ
def cargar_inventario(matriz: list[list]) -> None:
    """
    Carga productos en una matriz de inventario.
    
    Args:
        matriz (list[list]): Matriz en donde se cargarán los productos.
    Returns:
        None: No devuelve nada, solo carga los productos en la matriz.
    """

    if not es_lista(matriz):
        print("Debe ingresar un inventario.")
        return
    cantidad_productos = leer_opcion("Ingrese la cantidad de productos a cargar: ", 1, 100)

    salir = 0

    while salir < cantidad_productos:
        nombre = input("Ingrese el nombre del producto: ")
        
        precio = float(input("Ingrese el precio del producto: "))

        cantidad = int(input("Ingrese la cantidad del producto: "))

        matriz += [[nombre, precio, cantidad]]
        print("Usted cargo correctamente el producto.")

        salir += 1

#ORDENAR MATRIZ
def ordenar_matriz_descendente(inventario: list[list])-> list[list]:
    """
    Ordena una matriz de inventario en orden descendente según el precio del producto.
    
    Args:
        inventario (list[list]): Matriz de inventario en donde se realizará el ordenamiento.
    Returns:
        inventario (list[list]): Devuelve la matriz ordenada en orden descendente por el precio del producto.

    """
    n = len(inventario)
    for i in range(n):
        for j in range(n - i - 1):
            if inventario[j][1] < inventario[j + 1][1]:
                aux = inventario[j + 1]
                inventario[j + 1] = inventario[j]
                inventario[j] = aux
    return inventario

def ordenar_matriz_ascendente(inventario: list[list])-> list[list]:
    """
    Ordena una matriz de inventario en orden ascendente según el precio del producto.
    
    Args:
        inventario (list[list]): Matriz de inventario en donde se realizará el ordenamiento.
    Returns:
        inventario (list[list]): Devuelve la matriz ordenada en orden ascendente por el precio del producto.
    """
    n = len(inventario)
    for i in range(n):
        for j in range(n - i - 1):
            if inventario[j][1] > inventario[j + 1][1]:
                aux = inventario[j + 1]
                inventario[j + 1] = inventario[j]
                inventario[j] = aux
    return inventario

def buscar_en_matriz(inventario: list[list], nombre_producto: str) -> list:
    """
    Busca un producto en una matriz de inventario por su nombre siempre que su indice sea 0
    
    Args:
        inventario (list[list]): Matriz de inventario en donde se realizará la búsqueda.
        nombre_producto (str): Nombre del producto a buscar.
    Returns:
        list: Devuelve el producto encontrado en la matriz
        None: Si no se encuentra el producto, devuelve None.
    """
    if not es_lista(inventario):
        print("No ha ingresado una lista como parametro.")
        return
    if not es_string(nombre_producto):
        print("El nombre del producto debe ser un string.")
        return

    for i in range(len(inventario)):
        if inventario[i][0] == nombre_producto:
            return inventario[i]
    return "Producto no encontrado."

def mostrar_matriz(matriz: list[list]) -> None:
    """
    Muestra los elementos de una matriz (lista de listas) de manera prolija.
    
    Args:
        matriz (list[list]): Matriz a mostrar con formatos de producto, precio y cantidad.
    Returns:
        None: Utiliza print para mostrar los datos de la matriz.
    """
    if not es_lista(matriz):
        print("No ha ingresado una lista como parametro.")
        return
    for i in range(len(matriz)):
        print(f"Producto: {matriz[i][0]}, Precio: {matriz[i][1]:.2f}, Cantidad: {matriz[i][2]}")
            
    print("===================================")

