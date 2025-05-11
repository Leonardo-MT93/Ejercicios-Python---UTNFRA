# Insertar
# Nombre de la función:
# insertar(lista, elemento, indice)
# Objetivo:
# Insertar un elemento en una posición específica de la lista.
# Tarea:
# Modificar la lista original, colocando elemento en la posición indicada por indice.
# Si el índice es mayor al tamaño de la lista, el elemento se agrega al final.
# Ejemplo: Si la lista es [10, 20, 30] y se inserta 5 en el índice 1, la lista resultante será [10, 5, 20, 30].

def insertar(lista: list, elemento: int | float, indice: int) -> None: 
    """
    Esta función agrega el elemento en el indice indicado a la lista utilizando al slice para saber la posicion exacta.
    Tambien tiene en cuenta en enviar un error si el indice esta fuera del rango permitido.

        Args:
                lista(list):         Lista donde se agregara el elemento
                elemento(int/float): Elemento que se incluirá en la lista  
                indice(int):         Indica el índice de la lista donde se ubicará al elemento 
        Returns:
                None:               Esta función no retorna valor.

    """
    if not isinstance(lista, list):
        print("No ha ingresado una lista.")
        return #Este return vacio no permite que se sigan ejecutando las lineas de codigo posteriores, ya que sino, habria error con len(lista) si el valor de lista no es del tipo list. 
    if indice < 0 or indice > len(lista):
        print("Indice fuera de rango. Ingrese un valor correcto.")
    else: 
        lista[indice:indice] = [elemento]

lista = 32
insertar(lista, 6, 2)
print(lista)