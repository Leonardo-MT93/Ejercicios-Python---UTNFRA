from funciones.menu_principal import iniciar_menu
from funciones.validacion_de_codigo import validar_codigo

seguir = True

while seguir: 

    option = iniciar_menu()

    match option:
        case 1:
            acceso = validar_codigo()
            if not acceso:
                print("No tiene los permisos necesarios para realizar estas operaciones.")
                seguir = False
            else: 
                print("La compuerta ha sido abierta exitosamente!!!")
        case 2:
            acceso = validar_codigo()
            if not acceso:
                print("No tiene los permisos necesarios para realizar estas operaciones.")
                seguir = False
            else: 
                print("Se ha realizado el despegue exitosamente!!!")
        case 3:
            print("Apagando sistemas en...")
            print("3...2...1...")
            print("Sistema apagado.")
        case 4:
            print("Saliendo de los sistemas...")
            seguir = False
        case _:
            print("Ingrese una opción válida.")