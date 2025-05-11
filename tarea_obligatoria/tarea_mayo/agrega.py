# Agregar
# Nombre de la función:
# agregar(lista, elemento)
# Objetivo:
# Agregar un elemento al final de la lista.
# Tarea:
# Modificar la lista original, añadiendo elemento como su último elemento.
# No es necesario retornar un valor (solo modificar la lista).

def agregar(lista: list,elemento: int | float)-> None: 
    """
    Esta función agrega elementos a la lista en la última posición
    
        Args:
                lista(list):        Lista donde se agregara el elemento
                elemento(int/float) Elemento que se incluirá en la lista    
        Returns:
                None:               Esta función no retorna valor.
    """
    if isinstance(lista, list):
        lista[len(lista):len(lista)] = [elemento]
    else:
        print("No ha ingresado una lista.")

lista = [1, 2, 3]
agregar(lista, 5)
print(lista)