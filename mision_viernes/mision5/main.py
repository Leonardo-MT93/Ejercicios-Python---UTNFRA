from westeros.utilidades.menu import mostrar_menu
from westeros.utilidades.menu import leer_opcion
from westeros.casas.lannister import mostrar_informacion as mostrar_info_lannister
from westeros.casas.stark import mostrar_informacion as mostrar_info_stark
from westeros.casas.targaryen import mostrar_informacion as mostrar_info_targaryen
from westeros.utilidades.manejo_listas import concatenar_listas
from westeros.casas.lannister import miembros_lannister
from westeros.casas.stark import miembros_stark
from westeros.casas.targaryen import miembros_targaryen

casas = ["Lannister", "Stark", "Targaryen"]

while True:

    mostrar_menu()

    opcion = leer_opcion("Ingrese una opción: ", 1, 3)

    match opcion:
        case 1:
            elegir_casa = leer_opcion("Elige una casa:  \n1. Lannister\n2.Stark\n3. Targaryen ", 1, 3)    
            if elegir_casa == 1:
                mostrar_info_lannister()
            elif elegir_casa == 2:
                mostrar_info_stark()
            else:
                mostrar_info_targaryen()
        case 2: 
            opc1 = leer_opcion("Elige la 1er casa: \n1. Lannister\n2.Stark\n3. Targaryen ", 1, 3) 
            if opc1 == 1:
                casa1 = miembros_lannister
            elif opc1 == 2:
                casa1 = miembros_stark
            else:
                casa1 = miembros_targaryen  
            opc2= leer_opcion("Elige la 2da casa: \n1. Lannister\n2.Stark\n3. Targaryen ", 1, 3)   
            if opc2 == 1:
                casa2 = miembros_lannister
            elif opc2 == 2:
                casa2 = miembros_stark
            else:
                casa2 = miembros_targaryen  

            familias_unidas = concatenar_listas(casa1, casa2)
            print(familias_unidas)
        case 3:
            print("Finalizando programa...")
            break

