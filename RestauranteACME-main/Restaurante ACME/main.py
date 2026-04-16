import logica
import persistencia

productos = persistencia.cargar_datos("Productos_ACME.csv")
mesas = persistencia.cargar_datos("Mesas_ACME.csv")
clientes = persistencia.cargar_datos("Clientes_ACME.csv")
ventas = persistencia.cargar_datos("Ventas_ACME.csv") 

while True:
    print("------- Bienvenido al Menú de Facturación ACME!! -------\n")
    print("1. Productos")
    print("2. Mesas")
    print("3. Clientes")
    print("4. Facturación")
    print("5. Reporte de Ventas")
    print("6. Salir del sistema")
    opcion = input("\nIngresa una opción para acceder: ")
    
    match opcion:
        case "1":
            print("\n--- Administración de Productos ---")
            print("1. Agregar producto")
            print("2. Mostrar Productos")
            print("3. Volver al menú principal")
            op1 = input("Selecciona: ")
            if op1 == "1":
                logica.agregar_productos(productos)
            elif op1 == "2":
                logica.mostrar_productos(productos)

        case "2":
            print("\n--- Administración de Mesas ---")
            print("1. Agregar mesa")
            print("2. Mostrar mesas")
            print("3. Volver")
            op2 = input("Selecciona: ")
            if op2 == "1":
                logica.agregar_mesa(mesas)
            elif op2 == "2":
                logica.mostrar_mesas(mesas)

        case "3":
            print("\n--- Administración de Clientes ---")
            print("1. Agregar Cliente")
            print("2. Mostrar Clientes")
            print("3. Volver")
            op3 = input("Selecciona: ")
            if op3 == "1":
                logica.agregar_cliente(clientes)
            elif op3 == "2":
                logica.mostrar_clientes(clientes)
                
        case "4":
            logica.crear_factura(productos, clientes, mesas, ventas)


        case "5":
            print("\n--- Historial de Ventas del dia ---")
            logica.generar_reporte_diario(ventas)

        case "6":
            print("Saliendo del sistema...")
            break



#total*descuento/100