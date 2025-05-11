# vaciar_lista(lista)
# Nombre de la función:
# [
# Objetivo:
# Eliminar todos los elementos de la lista, dejándola vacía.
# Tarea:
# Modificar la lista original, removiendo todos sus elementos.
# No es necesario retornar un valor (solo modificar la lista).
# Ejemplo: Si la lista es [1, 2, 3], al llamar a vaciar_lista(), la lista quedará [].

def vaciar_lista(lista: list) -> None:
    """
    Esta función vacia toda la lista  eliminando todos su contenido.
        Args:
                lista(list):         Lista donde se agregara el elemento
        Returns:
                None:               No retorna nada.
    """
    if not isinstance(lista, list):
        print("No ha ingresado una lista como parametro.")
        return #Este return vacio no permite que se sigan ejecutando las lineas de codigo posteriores, ya que sino, habria error con len(lista) si el valor de lista no es del tipo list. 
    lista[:] = []

lista = [1, 2, 3]
vaciar_lista(lista)

print(lista)


