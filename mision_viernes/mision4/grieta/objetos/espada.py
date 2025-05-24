def equipar_espada(stats):
        
    print("El daño se ha incrementado un 80%")

    valor_aumentado = stats[0] + stats[0]*0.8

    print(f"Su daño aumento: {stats[0]} => {valor_aumentado}")

    stats[2] = valor_aumentado

    print(f"Estadisticas actualizadas: {stats}")