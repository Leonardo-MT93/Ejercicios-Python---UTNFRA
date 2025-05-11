# Eliminar todas las instancias
# Nombre de la función:
# eliminar_todos(lista, elemento)
# Objetivo:
# Eliminar todas las ocurrencias de un elemento en la lista.
# Tarea:
# Modificar la lista original, removiendo todos los elementos iguales al valor recibido.
# No es necesario retornar un valor (solo modificar la lista).
# Ejemplo: Si la lista es [4, 8, 4, 4, 10] y se eliminan todas las instancias de 4, la lista resultante será [8, 10].

def eliminar_todos(lista: list, elemento: int | float)-> None:
    """
    Esta función busca todas las apariciones del elemento en la lista y las elimina.
    Se realiza el recorrido con un bucle for de manera inversa para no tener problemas con los indices ya que se van eliminando las coincidencias a medida que el bucle se esta realizando. 
        Args:
                lista(list):         Lista donde se agregara el elemento
                elemento(int/float): Elemento que se buscará en la lista  
        Returns:
                None:               Retornará None si no encontro el elemento dentro de la lista.
    """
    if not isinstance(lista, list):
        print("No ha ingresado una lista como parametro.")
        return #Este return vacio no permite que se sigan ejecutando las lineas de codigo posteriores, ya que sino, habria error con len(lista) si el valor de lista no es del tipo list. 
    
    for i in range(len(lista) -1, -1, -1):
        if lista[i] == elemento:
            lista[i:i+1] = []

    
        
lista = [1, 3, 5, 2, 4, 5, 3]

eliminar_todos(lista, 2)