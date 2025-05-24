from grieta.campeones.campeones import mostrar_atributos
from grieta.campeones.seleccionar_campeon import elegir_campeon
from grieta.campeones.habilidades import habilidad_ult
from grieta.objetos.seleccion_objeto import elegir_objeto
from grieta.objetos.botas import equipar_botas
from grieta.objetos.espada import equipar_espada
from grieta.utilidades.menu import mostrar_menu
from grieta.utilidades.lectura import leer_opcion
from grieta.utilidades.validar_campeon import comprobar_campeon

campeon = None
estadisticas = None

while True: 
    mostrar_menu()

    opcion = leer_opcion("\nSelecciona una opcion: ", 0, 4)

    match opcion:
        case 0:
            campeon = elegir_campeon()
        case 1:
            if comprobar_campeon(campeon):
                estadisticas = mostrar_atributos(campeon)
                print(f"Las estadisticas del campeon {campeon} son: {estadisticas}")
        case 2:
            if comprobar_campeon(campeon):
                habilidad_ult(campeon)
        case 3:
            if comprobar_campeon(campeon):
                objeto = elegir_objeto()
                if objeto == "Botas":
                    equipar_botas(estadisticas)
                else:
                    equipar_espada(estadisticas)
        case 4:
            print("Cerrando programa...")
            break
        case _:
            break