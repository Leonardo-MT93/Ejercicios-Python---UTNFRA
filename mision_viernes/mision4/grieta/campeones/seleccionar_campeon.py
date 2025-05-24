def elegir_campeon():
    opciones = ["Trish", "Lux", "Kamille"]
    while True:
        campeon_elegido = input("\nSeleccione su campeon: Trish / Lux / Kamille.  ")
        if campeon_elegido in opciones:
            print(f"\nUsted selecciono al campeon: {campeon_elegido}")
            return campeon_elegido
        print("Debe ingresar el nombre correctamente.")
            
    

    