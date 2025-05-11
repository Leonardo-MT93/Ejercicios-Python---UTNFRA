# Eliminar el último elemento
# Nombre de la función:
# eliminar(lista)
# Objetivo:
# Eliminar el último elemento de la lista y retornarlo.
# Tarea:
# Modificar la lista original, removiendo su último elemento.
# Retornar el elemento eliminado.
# Ejemplo: Si la lista es ["a", "b", "c"], al llamar a eliminar(), se retorna "c" y la lista queda ["a", "b"].

def eliminar(lista: list)-> int | float:
    """
    Esta función eliminar el último elemento de la lista y lo retorna.

        Args:
                lista(list):         Lista donde se agregara el elemento
        Returns:
                elemento_eliminado(int/float):  Esta función retorna el valor del elemento eliminado.
    """
    if not isinstance(lista, list):
        print("No ha ingresado una lista como parametro.")
        return #Este return vacio no permite que se sigan ejecutando las lineas de codigo posteriores, ya que sino, habria error con len(lista) si el valor de lista no es del tipo list. 
    else:
        ultima_posicion = len(lista) -1 
        elemento_eliminado = lista[ultima_posicion]
        lista[:] = lista[:ultima_posicion ]
        return elemento_eliminado
    

lista = [1, 3, 4, 7.4]
ultimo_elemento = eliminar(lista)
if isinstance(ultimo_elemento, int) or isinstance(ultimo_elemento, float):
    print(f"El último elemento eliminado es: {ultimo_elemento}. Mi lista quedó: {lista}")