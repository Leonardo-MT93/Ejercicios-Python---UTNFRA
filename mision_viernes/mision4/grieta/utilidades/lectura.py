def leer_opcion(prompt, minimo, maximo): 

    while True:
        opcion_elegida = input(prompt)

        if opcion_elegida.isdigit():
            opcion_elegida = int(opcion_elegida)
            if  minimo <= opcion_elegida <= maximo:
                return opcion_elegida
            else:
                print(f"El valor ingresado debe estar en el rango: {minimo} - {maximo}")
        else:
            print("Debe ingresar un valor numerico.")