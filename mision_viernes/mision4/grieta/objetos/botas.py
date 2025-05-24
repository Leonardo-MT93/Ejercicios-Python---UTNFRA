

def equipar_botas(stats):
    
    print("La velocidad se ha incrementado un 50%")

    valor_aumentado = stats[2] + stats[2]*0.5

    print(f"Su velocidad aumento: {stats[2]} => {valor_aumentado}")

    stats[2] = valor_aumentado

    print(f"Estadisticas actualizadas: {stats}")
