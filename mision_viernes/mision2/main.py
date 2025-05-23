from menu_principal import mostrar_menu_principal
from escenarios.primer_escenario import mostrar_escenario_1
from escenarios.segundo_escenario import mostrar_escenario_2
from escenarios.tercer_escenario import mostrar_escenario_3


while True:

    option = mostrar_menu_principal()

    match option: 
        case 1: 
            primera_opcion = mostrar_escenario_1()

            if primera_opcion == 2: 
                print("Ha resultado atrapado por Jason!!")
                print("Game Over")
                break
            else:
                print("Ha superado la primera escena exitosamente!")
                segunda_opcion = mostrar_escenario_2()
                if segunda_opcion == 1:
                    print("Ha resultado atrapado por Jason!!")
                    print("Game Over")
                    break
                else:
                    print("Ha superado la segunda escena exitosamente!")
                    tercera_opcion = mostrar_escenario_3()
                    if tercera_opcion != 3:
                        print("Ha resultado atrapado por Jason!!")
                        print("Game Over")
                        break
                    else:
                        print("Ha escapado exitosamente!! ")
                        print("Usted ha ganado eligiendo correctamente")
                        print("¡Felicidades!")
                        break
        case 2:
            print("INSTRUCCIONES")

        case 3:
            print("Finalizando Juego..")
            break
        case _:
            print("Opción no válida. Por favor, elija una opción válida del 1 al 3.")

