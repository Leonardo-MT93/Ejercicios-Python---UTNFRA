# Eliminar primera instancia
# Nombre de la función:
# eliminar_primer_instancia(lista, elemento)
# Objetivo:
# Eliminar la primera ocurrencia de un elemento en la lista y retornarlo.
# Tarea:
# Buscar la primera aparición de elemento en la lista, eliminarla y retornar el elemento eliminado.
# Si el elemento no existe, retornar None y dejar la lista sin cambios.
# Ejemplo: Si la lista es [5, 3, 5, 7] y se elimina 5, la lista queda [3, 5, 7] y se retorna 5.

def eliminar_primera_instancia(lista: list, elemento: int | float)-> None: 
    """
    Esta función busca la primera aparición de elemento en la lista, la elimina y retorna el elemento eliminado.
        Args:
                lista(list):         Lista donde se agregara el elemento
                elemento(int/float): Elemento que se buscará en la lista  
        Returns:
                int or float:        Esta función retorna el valor del elemento eliminado.
                None:               Retornará None si no encontro el elemento dentro de la lista.
    """
    if not isinstance(lista, list):
        print("No ha ingresado una lista como parametro.")
        return #Este return vacio no permite que se sigan ejecutando las lineas de codigo posteriores, ya que sino, habria error con len(lista) si el valor de lista no es del tipo list. 
    
    for i in range(len(lista)):
        if lista[i] == elemento:
            lista[i:i+1] = []
            return elemento
    return None


lista = [1, 4 ,5, 4]
valor_eliminado = eliminar_primera_instancia(lista, 2)

if isinstance(valor_eliminado, (int, float)):
    print(f"El elemento eliminado de la lista es: {valor_eliminado} y la lista actualizada quedo asi: {lista}")
else:
    print("El elemento no se encontró dentro de la lista.")