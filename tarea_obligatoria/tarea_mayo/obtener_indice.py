# Nombre de la función:
# obtener_indice(lista, elemento)
# Objetivo:
# Encontrar el índice de la primera ocurrencia de un elemento en la lista.
# Tarea:
# Buscar en la lista el elemento recibido y retornar su posición (índice).
# Si el elemento no existe en la lista, retornar -1.

def obtener_indice(lista: list, elemento: int | float)-> int:
    """
    Esta función busca el índice de la primera ocurrencia de un elemento en la lista, si lo encuentra devuelve el índice y sino, devuelve -1.

        Args:
                lista(list):         Lista donde se agregara el elemento
                elemento(int/float): Elemento que se incluirá en la lista  
        Returns:
                i(int):               Esta función retorna el valor del índice encontrado.
                -1:                   Esta función devuelve -1 si no se encontro al elemento en la lista.

    """
    if not isinstance(lista, list):
        print("No ha ingresado una lista como parametro.")
        return #Este return vacio no permite que se sigan ejecutando las lineas de codigo posteriores, ya que sino, habria error con len(lista) si el valor de lista no es del tipo list. 
    else:
        for i in range(len(lista)):
            if(lista[i] == elemento):
                return i
        return -1
lista = [1, 2, 3]
print(obtener_indice(lista, 4))