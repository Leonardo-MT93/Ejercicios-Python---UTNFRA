"""def contar_iterativo(numero):
    for i in range(numero, -1, -1):
        print(i)

contar_iterativo(10)        
"""
"""
def contar_recursivo(numero):
    if numero < 0:
        return
    print(numero)
    contar_recursivo(numero - 1)

contar_recursivo(10)
"""
"""def factorial_iterativo(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial
print(factorial_iterativo(-5))
"""

"""def factorial_recursivo(numero): 

    if numero < 0:
        return "El factorial no está definido para números negativos"
    return numero * factorial_recursivo(numero - 1)

print(factorial_recursivo(5))
"""
