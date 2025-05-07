# FUNCIONES RECURSIVAS
# Realizar una función recursiva que calcule la suma de los primeros números naturales:
"""
def sumar_naturales(numero: int) -> int:

    if numero == 1:
        return 1
    else:
        return sumar_naturales(numero - 1) + numero   

print(sumar_naturales(3))
"""
# Realizar una función recursiva que calcule la potencia de un número:
"""
def calcular_potencia(base: int, exponente: int) -> int:
    
    if exponente == 0:
        return 1
    else:
        return calcular_potencia(base, exponente - 1) * base
    
base = 3 
exponente = 3   
print(calcular_potencia(base, exponente))
"""
# Realizar una función recursiva que permita realizar la suma de los dígitos de un número:
"""
def sumar_digitos(numero: int) -> int:

    if numero == 0:
        return 0
    else:
        return sumar_digitos(numero // 10) + (numero % 10)
        
print(sumar_digitos(1234))
"""


# Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

# Definición:
# La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:
"""
def calcular_fibonacci(numero: int) -> int:

    if numero == 0:
        return 0 
    elif numero == 1:
        return 1
    else:

        return calcular_fibonacci(numero - 1 ) + calcular_fibonacci( numero - 2)

print(calcular_fibonacci(4))
"""
