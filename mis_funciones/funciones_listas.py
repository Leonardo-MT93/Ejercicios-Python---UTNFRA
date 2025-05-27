from validaciones.validaciones import es_lista, es_numero_entero, es_numero_flotante

#Correccion de listas - Tarea Obligatoria


# MÁXIMOS Y MÍNIMOS
def buscar_min_en_lista(lista : list)-> int | float:
    """
    Busca el elemento de mayor valor numérico dentro de una lista.

    Args:
        list: Lista en donde se realizará la búsqueda.

    Returns:
        int/float: El valor mínimo encontrado en la lista.
    """
    numero_min = float("inf")
    for i in range(len(lista)):
        if lista[i] < numero_min:
            numero_min = lista[i]
    return numero_min

def buscar_max_en_lista(lista: list)-> int | float:
    """
    Busca el elemento de mayor valor numérico dentro de una lista.

    Args:
        list: Lista en donde se realizará la búsqueda.

    Returns:
        int/float: El valor mínimo encontrado en la lista.
    """
    numero_max = float("-inf")
    for i in range(len(lista)):
        if lista[i] > numero_max:
            numero_max = lista[i]
    return numero_max

#MODIFICADORES DE LAS LISTAS
def agregar_elemento(lista: list,elemento: int | float)-> None: 
    """
    Esta función agrega elementos a la lista en la última posición
    
    Args:
                lista(list):        Lista donde se agregara el elemento
                elemento(int/float) Elemento que se incluirá en la lista    
    Returns:
                None:               Esta función no retorna valor.
    """
    if es_lista(lista):
        if es_numero_entero(elemento) or es_numero_flotante(elemento):
                lista[len(lista):len(lista)] = [elemento]
        else:
            print("El elemento no es un número entero o flotante.")
    else:
        print("No ha ingresado una lista.")

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
    if not es_lista(lista):
        print("No ha ingresado una lista como parametro.")
        return #Este return vacio no permite que se sigan ejecutando las lineas de codigo posteriores, ya que sino, habria error con len(lista) si el valor de lista no es del tipo list. 
    if not (es_numero_entero(elemento) or es_numero_flotante(elemento)):
        print("El elemento no es un número entero o flotante.")
        return
    for i in range(len(lista)):
        if lista[i] == elemento:
            lista[i:i+1] = []
            return elemento
    return None

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
    if not es_lista(lista):
        print("No ha ingresado una lista como parametro.")
        return #Este return vacio no permite que se sigan ejecutando las lineas de codigo posteriores, ya que sino, habria error con len(lista) si el valor de lista no es del tipo list. 
    if not (es_numero_entero(elemento) or es_numero_flotante(elemento)):
        print("El elemento no es un número entero o flotante.")
        return
    
    for i in range(len(lista) -1, -1, -1): #Recorre la lista de atras hacia adelante para evitar problemas con los indices al eliminar elementos.
        if lista[i] == elemento:
            lista[i:i+1] = []
    return None

def eliminar_ultima_instancia(lista: list)-> int | float:
    """
    Esta función eliminar el último elemento de la lista y lo retorna.

    Args:
                lista(list):         Lista donde se agregara el elemento
    Returns:
                elemento_eliminado(int/float):  Esta función retorna el valor del elemento eliminado.
    """
    if not es_lista(lista):
        print("No ha ingresado una lista como parametro.")
        return #Este return vacio no permite que se sigan ejecutando las lineas de codigo posteriores, ya que sino, habria error con len(lista) si el valor de lista no es del tipo list. 
    else:
        ultima_posicion = len(lista) -1 
        elemento_eliminado = lista[ultima_posicion]
        lista[:] = lista[:ultima_posicion ]
        return elemento_eliminado

def insertar_por_indice(lista: list, elemento: int | float, indice: int) -> None: 
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
    if not es_lista(lista):
        print("No ha ingresado una lista.")
        return 
    if not (es_numero_entero(elemento) or es_numero_flotante(elemento)):
        print("El elemento no es un número entero o flotante.")
        return
    if not es_numero_entero(indice):
        print("El indice no es un número entero.")
        return
    if indice < 0 or indice > len(lista):
        print("Indice fuera de rango. Ingrese un valor correcto.")
    else: 
        lista[indice:indice] = [elemento]

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
    if not es_lista(lista):
        print("No ha ingresado una lista como parametro.")
        return 
    if not (es_numero_entero(elemento) or es_numero_flotante(elemento)):
        print("El elemento no es un número entero o flotante.")
        return
    if len(lista) == 0:
        print("Error! La lista está vacía.")
        return -1
    for i in range(len(lista)):
            if(lista[i] == elemento):
                return i
    return -1
        
def vaciar_lista(lista: list) -> None:
    """
    Esta función vacia toda la lista  eliminando todos su contenido.
    Args:
                lista(list):         Lista donde se agregara el elemento
    Returns:
                None:               No retorna nada.
    """
    if not es_lista(lista):
        print("No ha ingresado una lista como parametro.")
        return 
    lista[:] = []

def ordenar_lista_ascendente(lista: list)-> list:
    """
    Esta función ordena la lista de menor a mayor utilizando el ordenamiento burbuja y usando una variable auxiliar.
    Args:
                lista(list):         Lista donde se ordenaran los elementos
    Returns:
                list:               Retorna los elementos ordenados.
    """
    if not es_lista(lista):
        print("No ha ingresado una lista como parametro.")
        return 
    n = len(lista)
    
    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if lista[j] > lista[j+1]:
                aux = lista[j+1] #Guarda en la variable auxiliar el menor valor
                lista[j+1] = lista[j] #Sobreescribe e intercambia los valores
                lista[j] = aux #Reemplaza con el valor guardado en nuestra variable auxiliar.
    return lista

def ordenar_lista_descendente(lista: list)-> list:
    """
    Esta función ordena la lista de mayor a menor utilizando el ordenamiento burbuja y usando una variable auxiliar.
    Args:
                lista(list):         Lista donde se ordenaran los elementos
    Returns:
                list:               Retorna los elementos ordenados.
    """
    if not es_lista(lista):
        print("No ha ingresado una lista como parametro.")
        return 
    n = len(lista)
    
    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if lista[j] < lista[j+1]:
                aux = lista[j+1] #Guarda en la variable auxiliar el menor valor
                lista[j+1] = lista[j] #Sobreescribe e intercambia los valores
                lista[j] = aux #Reemplaza con el valor guardado en nuestra variable auxiliar.
    return lista

def acumular_lista(lista: list)-> int | float:
    """
    Esta función acumula todos los elementos de la lista y devuelve el resultado.
    Args:
                lista(list):         Lista donde se ordenaran los elementos
    Returns:
                int/float:          Retorna la suma de todos los elementos.
    """
    if not es_lista(lista):
        print("No ha ingresado una lista como parametro.")
        return 
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

def promedio_lista(lista: list)-> int | float:
    """
    Esta función calcula el promedio de todos los elementos de la lista y devuelve el resultado.
    Args:
                lista(list):         Lista donde se ordenaran los elementos
    Returns:
                int/float:          Retorna el promedio de todos los elementos.
    """
    if not es_lista(lista):
        print("No ha ingresado una lista como parametro.")
        return 
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma / len(lista)
 
def mostrar_datos(lista: list)-> None:



    """
    Esta función muestra los datos de la lista en un string.
    
    Args:
            lista(list):    Lista donde se extraen los elementos
    Returns:
            None:    Utiliza print para mostrar los datos de la lista en un formato específico.
    
    """
    if not es_lista(lista):
        print("No ha ingresado una lista como parametro.")
        return 
    return print(f"El producto es: {lista[0]}, el precio es: {lista[1]:.2f} y la cantidad es: {lista[2]}")
