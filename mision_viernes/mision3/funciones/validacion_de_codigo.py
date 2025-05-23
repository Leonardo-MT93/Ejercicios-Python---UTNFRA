def validar_codigo():

    codigo = int(input("Ingrese el código válido para realizar la operación: "))

    if codigo == 1138 and 1000 <= codigo <= 9999:
        return True
    else: 
        print("Codigo incorrecto. Ingrese el código correctamente.")
        return False
    
