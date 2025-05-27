from funciones.funciones_de_programa import cargar_pacientes, mostrar_listado_pacientes, buscar_paciente, mostrar_un_paciente, ordenar_pacientes_ascendente, buscar_paciente_mayor_dias_internacion, buscar_paciente_menor_dias_internacion, pacientes_dias_sup_internacion, promedio_dias_internacion
from utilidades.menu import mostrar_menu_principal, leer_opcion
from validaciones.validar_entrada import lista_vacia


pacientes = []
opcion = -1

while opcion != 9:

    mostrar_menu_principal()
    opcion = leer_opcion("Ingrese una opción: ", 1, 9)
    match opcion:
        case 1:
            cargar_pacientes(pacientes)
        case 2:
            if lista_vacia(pacientes):
                print("No hay pacientes registrados para la operacion solicitada.")
            else:
                mostrar_listado_pacientes(pacientes)
        case 3:
            if lista_vacia(pacientes):
                print("No hay pacientes registrados para la operacion solicitada.")
            else:
                numero_hc = leer_opcion("Ingrese el numero de historia clinica a buscar: ", 0, 9999)
                busqueda = buscar_paciente(pacientes, numero_hc)
                if not busqueda:
                    print("El paciente no ha sido encontrado.")
                else:
                    mostrar_un_paciente(busqueda)
            
        case 4:
            if lista_vacia(pacientes):
                print("No hay pacientes registrados para la operacion solicitada.")
            else:
                mostrar_listado_pacientes(ordenar_pacientes_ascendente(pacientes))
        case 5:
            if lista_vacia(pacientes):
                print("No hay pacientes registrados para la operacion solicitada.")
            else:
                paciente_buscado = buscar_paciente_mayor_dias_internacion(pacientes)
                if paciente_buscado:
                    mostrar_un_paciente(paciente_buscado)
        case 6: 
            if lista_vacia(pacientes):
                print("No hay pacientes registrados para la operacion solicitada.")
            else:
                paciente_buscado = buscar_paciente_menor_dias_internacion(pacientes)
                if paciente_buscado:
                    mostrar_un_paciente(paciente_buscado)
        case 7: 
            if lista_vacia(pacientes):
                print("No hay pacientes registrados para la operacion solicitada.")
            else:
                pacientes_encontrados = pacientes_dias_sup_internacion(pacientes, 5)
                if pacientes_encontrados:
                    print(f"Los pacientes que superan los 5 dias de internacion son: {pacientes_encontrados}")
        case 8: 
            if lista_vacia(pacientes):
                print("No hay pacientes registrados para la operacion solicitada.")
            else:
                promedio = promedio_dias_internacion(pacientes)
                if promedio:
                    print(f"El promedio de dias de internacion de todos los pacientes es: {promedio:.2f}")
        case 9: 
            print("Finalizando programa...")
            print("Programa terminado.")
        case _:
            print("Opción no válida. Intente nuevamente.") 