""" Ejercicio 1
Escribir un programa que almacene la cadena de caracteres prog1Div777 en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable
 """

""" contraseña = "prog1Div777"

ingreso_contraseña = input("Ingrese una contraseña: ")

if contraseña == ingreso_contraseña:
    print("Contraseña ingresada correctamente!!!")
else:
    print("Contraseña erronea. Ingrese nuevamente")
 """


""" Ejercicio 2
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

 """

""" numero_ingresado = int(input("Ingrese un numero: "))

if numero_ingresado % 2 == 0:
    print("El numero ingresado es PAR.")
else:
    print("El numero ingresado por el usuario es IMPAR") """




""" Ejercicio 3
Para pagar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a 20000 ARS mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que pagar un impuesto o no.
 """

""" edad = int(input("Ingrese su edad: "))

ingresos_mensuales = int(input("Indique sus ingresos mensuales: "))

if edad > 18 and ingresos_mensuales >= 20000:
    print("USTED DEBE PAGAR IMPUESTOS!")
else: 
    print("Usted no paga impuestos..") """

""" Ejercicio 4
Cree un programa que calcule el IMC (Índice de masa corporal). Fórmula --> IMC=Peso/Altura2 (Peso sobre altura al cuadrado).
El usuario deberá ingresar su peso y su altura (su nombre si quieren y después imprimirlo concatenado) y el programa además de calcular el IMC deberá decir en qué clasificación se encuentra. La clasificación la encontraran en la siguiente tabla:
 """

""" nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

imc = peso / (altura * altura)

print(f"Usted se llama {nombre} y su imc calculado es: {imc}")

match True:
    case _ if imc < 18.5:
        print("Su peso es bajo")
    case _ if imc > 18.5 and imc < 24.9:
        print("Su peso es el adecuado")
    case _ if imc > 25 and imc < 29.9:
        print("Usted tiene sobrepeso")
    case _ if imc > 30 and imc < 34.9:
        print("Usted tiene una obesidad de grado 1")
    case _ if imc > 35 and imc < 39.9:
        print("Usted tiene una obesidad de grado 2")
    case _:
        print("Usted tiene una obesidad de grado 2") """

""" Ejercicio 5
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 80 ARS y si es mayor de 18 años, 150 ARS.

 """
edad = int(input("Ingrese su edad para indicarle el valor de su entrada: "))

match True:
    case _ if edad < 4:
        print("Usted ingresa gratis!! ")
    case _ if edad >= 4 and edad <= 18:
        print("Usted debe pagar 80 ARS")
    case _:
        print("Usted debe pagar 150 ARS")

""" Ejercicio 6
Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario introduce el divisor cero debera imprimir un mensaje de error.
 """



""" Ejercicio 7
Crea una variable numérica y si está entre 0 y 10, mostrar un mensaje indicándolo.
 """
