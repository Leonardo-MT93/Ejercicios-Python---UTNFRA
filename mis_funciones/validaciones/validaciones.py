def es_lista(lista: list) -> bool:
    """
    Esta función valida si el parametro recibido es una lista.
    
    Args:
            list:        Lista a validar
    Returns:
            True/False:  True si es una lista, False en caso contrario.
    """
    if type(lista) == list:
        return True
    else:
        return False
    
def lista_vacia(lista: list) -> bool:
    """
    Esta función valida si el parametro recibido es una lista vacia.
    
    Args:
            list:        Lista a validar
    Returns:
            True/False:  True si es una lista vacia, False en caso contrario.
    """
    if type(lista) == list and len(lista) == 0:
        return True
    else:
        return False
def es_numero_entero(elemento: int) -> bool:
    """
    Esta función valida si el parametro recibido es un número entero.
    
    Args:
            elemento(int): Elemento a validar
    Returns:
            True/False:  True si es un número, False en caso contrario.
    """
    if type(elemento) == int:
        return True
    else:
        return False
    
def es_numero_flotante(elemento: float) -> bool:
    """
    Esta función valida si el parametro recibido es un número flotante.
    
    Args:
            elemento(float): Elemento a validar
    Returns:
            True/False:  True si es un número, False en caso contrario.
    """
    if type(elemento) == float:
        return True
    else:
        return False
    
def es_string(elemento: str) -> bool:
    """
    Esta función valida si el parametro recibido es un string.
    
    Args:
            elemento(str): Elemento a validar
    Returns:
            True/False:  True si es un string, False en caso contrario.
    """
    if type(elemento) == str:
        return True
    else:
        return False