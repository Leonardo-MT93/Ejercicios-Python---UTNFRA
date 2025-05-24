def elegir_objeto():
    opciones = ["Espada", "Botas"]
    while True:
        objeto_elegido = input("\nSeleccione un objeto: Botas / Espada.  ")
        if objeto_elegido in opciones:
            print(f"\nUsted selecciono el objeto: {objeto_elegido}")
            return objeto_elegido
        print("Debe ingresar el nombre del objeto correctamente.")