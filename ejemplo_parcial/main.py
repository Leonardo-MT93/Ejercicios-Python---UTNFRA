""" 
Pendiente:

Crear modulos y estructura de carpetas
Realizar validaciones
Implementar funcionalidad de la opcion 3 - Sorting

"""


inventario = []

def mostrar_menu_principal():
    print("\n*** Menú Principal ***")
    print("1 - Cargar productos")
    print("2 - Buscar producto")
    print("3 - Ordenar inventario")
    print("4 - Mostrar producto más caro y más barato")
    print("5 - Mostrar producto con precio mayor a 15000")
    print("0 - Salir")
    return int(input("Ingrese una opción: "))

def cargar_productos(inventario):
    seguir = "s"

    while seguir == "s": 
        
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad: "))

        producto = [nombre] + [precio] + [cantidad]

        inventario[len(inventario):] = [producto]

        seguir = input("Desea seguir ingresando datos?: s/n ")

def buscar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    for i in range(len(inventario)):
        for j in range(len(inventario[i])):
            if j == 0 and inventario[i][0] == nombre:
                print(f"Producto encontrado! Nombre: {inventario[i][0]}, Precio: {inventario[i][1]}, Cantidad: {inventario[i][2]}") 
                encontrado = True
    if encontrado == False:
        print("Producto no encontrado..")

def mostrar_producto_mas_caro(inventario):
    precio_mas_caro = 0
    producto_mas_caro = []

    for i in range(len(inventario)):
        for j in range(len(inventario[i])):
            if j == 1 and inventario[i][j] > precio_mas_caro:
                precio_mas_caro = inventario[i][j]
                producto_mas_caro = inventario[i]

    return producto_mas_caro

def mostrar_producto_mas_barato(inventario):
    precio_mas_barato = None
    producto_mas_barato = None

    for i in range(len(inventario)):
        precio_actual = inventario[i][1]

        if precio_mas_barato == None or precio_mas_barato > precio_actual:
            precio_mas_barato = precio_actual
            producto_mas_barato = inventario[i]
    
    return producto_mas_barato

def mostrar_prod_mayor_15000(inventario):
    precio_fijo = 15000
    producto_encontrado = None

    for i in range(len(inventario)):
        if inventario[i][1] > precio_fijo:
            producto_encontrado = inventario[i]
    return producto_encontrado


while True:

    option = mostrar_menu_principal()

    match option:
        case 0:
            print("Finalizando programa.")
            break
        case 1:
            cargar_productos(inventario)
                
        case 2:
            if inventario == []:
                print("No hay productos ingresados en el sistema para realizar esta operacion.")
            else: 
                buscar_producto(inventario)
        case 3:
            print("Función no implementada.")
            # ordenar_inventario()
        case 4:
            if inventario == []:
                print("No hay productos ingresados en el sistema para realizar esta operacion.")
            else: 
                producto_mas_caro = mostrar_producto_mas_caro(inventario)
                print("El producto más caro es: ", producto_mas_caro)
                producto_mas_barato = mostrar_producto_mas_barato(inventario)
                print("El producto más barato es: ", producto_mas_barato)
        case 5:
            if inventario == []:
                print("No hay productos ingresados en el sistema para realizar esta operacion.")
            else: 
                producto_mayor_a_15000 = mostrar_prod_mayor_15000(inventario)
                if producto_mayor_a_15000:
                    print(producto_mayor_a_15000)
                else:
                    print("No se encontró un producto mayor a $15000")
        case _:
                print("La opcion ingresada no es valida. Por favor reintente nuevamente.")

