# Los siguientes ejercicios deben realizarse sin estructuras condicionales


"""
 Ejercicio 1
 Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):
 Si los dos números son iguales
 Si los dos números son diferentes
 Si el primero es mayor que el segundo
 Si el segundo es mayor o igual que el primero

 Resolución:

    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    print(num1 == num2, " - Los numeros son iguales")  
    print(num1 != num2, " - Los numeros son iguales")  
    print(num1 > num2, " - El primero es mayor que el segundo") 
    print(num1 <= num2, " -  El segundo es mayor o igual que el primero")  

"""




"""
Ejercicio 2
Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiente con mostrar True o False).

Resolución:
cadena = input("Introduce una cadena de texto: ")
longitud = len(cadena)
print("El resultado es -",longitud >= 3 and longitud < 10)
"""

"""
Ejercicio 3
Verificar si un número es par y positivo. Solamente mostrar si es True o False

Resolución:
num = int(input("Ingrese un numero: "))
print(num %2 == 0 and num > 0)
"""

"""
Ejercicio 4
Comprobar si una cadena contiene al menos una vocal. Solamente mostrar si es True o False

Resolución:
cadena = input("Ingrese una palabra: ")
for i in cadena:
    print("La letra analizada es: ", i, ((i == "a") or (i == "e" )or (i == "i") or (i == "o") or (i == "u")))
"""
"""
Ejercicio 5
En un laboratorio se debe trabajar en condiciones ideales. Estas son una temperatura entre 20ºC y 25ºC y humedad entre 70% y 90%.
Antes de comenzar con su trabajo el empleado debe ingresar en el sistema tanto la temperatura y humedad que se registran en el laboratorio y este le debe devolver True o False según se cumplan las condiciones ideales.

Resolución:
temperatura = int(input("Ingrese la temperatura: "))
humedad = int(input("Ingrese la humedad: "))    
print((temperatura > 20 and temperatura < 25) and (humedad > 70 and humedad < 90 ))
"""
