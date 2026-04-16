from datetime import datetime
import persistencia



def mostrar_productos(productos):
    print("\n--- LISTA DE PRODUCTOS ---")
    for p in productos:
        print(f"Código: {p['codigo']} | Nombre: {p['nombre']} | Precio: {p['vu']} | IVA: {p['iva']}%")

def mostrar_clientes(clientes):
    print("\n--- LISTA DE CLIENTES ---")
    for c in clientes:
        print(f"ID: {c['id']} | Nombre: {c['nombre']} | Tel: {c['telefono']} | Email: {c['email']}")

def mostrar_mesas(mesas):
    print("\n--- LISTA DE MESAS ---")
    for m in mesas:
        print(f"Código: {m['codigo']} | Nombre: {m['nombre']} | Puestos: {m['puesto']}")

        
#codigo, nombre, vu, iva
def agregar_productos (productos):
    codigo = input("Ingresa el Codigo del Producto: ")
    if codigo == (""):
      return print ("el codigo esta vacio")
    existe = False
    for producto in productos:
            if producto["codigo"] == codigo:
                existe = True
                break
            
    if existe == True:
        print("\n--Error este producto ya esta registrado!--\n")
    else:
        nombre = input("Ingresa el Nombre del Producto: ")
        if nombre == (""):
          return print ("el nombre esta vacio")
        try: 
         vu = float(input("Ingresa el valor del producto: "))
        except ValueError: 
         print ("se esperaba un valor numerico")
         return 
        try: 
         iva = float(input("Ingresa el iva del producto: "))
        except ValueError: 
            print ("se esperaba un valor numerico") 
            return
        nuevo_p = {
            'codigo': codigo,
            'nombre':nombre,
            'vu': vu,
            'iva': iva
        }
        productos.append(nuevo_p)
        
        columnas = ["codigo","nombre","vu","iva"]
        persistencia.guardar_archivo(productos,"Productos_ACME.csv",columnas)
        print("\n--Producto agregado con exito!--")
        

#identificacion, nombre, telefono, email
def agregar_cliente (clientes):
    id = input("Ingresa tu identificacion: ")
    if id == (""):
      return print ("identificacion vacia")
    existe = False
    for usuario in clientes:
        if usuario["id"] == id:
            existe = True
            break
    if existe == True:
        print("\n--Error este usuario ya existe!--")
    else:
        nombre = input("Ingresa el nombre del cliente: ")
        if nombre == (""):
          return print ("el nombre esta vacio")
        telefono = input("Ingresa el telefono del cliente: ")
        if telefono == (""):
            return print ("el numero de telofono esta vacio")
        email = input("Ingresa el email del cliente: ")
        if email == (""):
          return  ("el email esta vacio")
        nuevo_c = {
            "id": id,
            "nombre": nombre,
            "telefono": telefono,
            "email": email
        }
        
        clientes.append(nuevo_c)
        columnas = ["id","nombre","telefono","email"]
        persistencia.guardar_archivo(clientes,"Clientes_ACME.csv",columnas)
        print("\n--Cliente añadido exitosamente!--")

#codigo,nombre,puesto
def agregar_mesa(mesas):
    codigo = input("Ingresa el codigo de la mesa: ")
    if codigo == (""):
      return print ("el codigo esta vacio")
    existe = False
    for mesa in mesas:
        if mesa["codigo"] == codigo:
            existe = True
            break
    if existe == True:
        print("\n--Error esta mesa ya existe!--")
    else:
        nombre = input("Ingresa el nombre de la mesa: ")
        if nombre == (""):
          return print ("el nombre esta vacio")
        puesto = input("Ingresa el numero de puestos de la mesa: ")
        if puesto == (""):
          return print ("el puesto esta vacio")
        
        nueva_m = {
            "codigo": codigo,
            "nombre": nombre,
            "puesto": puesto
        }        
    
        mesas.append(nueva_m)
        columnas = ["codigo","nombre","puesto"]
        persistencia.guardar_archivo(mesas,"Mesas_ACME.csv",columnas)
        print("\n--Mesa agregada exitosamente!--")

def buscador_datos(lista,llave,valor_buscado):
    for dato in lista:
        if dato[llave] == valor_buscado:
            return dato
    return None
opcion = 1
def crear_factura(productos, clientes, mesas, ventas):
    cod_mesa = input("Ingresa el codigo de la mesa: ")
    mesa = buscador_datos(mesas, "codigo", cod_mesa)
    if not mesa:
        print("La mesa buscada no existe!")
        return
        
    id_cliente = input("Ingresa la identificacion del cliente: ")
    cliente = buscador_datos(clientes, "id", id_cliente)
    if not cliente:
        print("El cliente no existe!")
        return


    fecha_auto = datetime.now().strftime("%d-%m-%Y")
    detalle_datos = []
    total_factura = 0
    while True:
        cod_producto = input("Ingrese el codigo del producto: ")
        producto = buscador_datos(productos, "codigo", cod_producto)
        
        if producto:
            cantidad = int(input(f"Cantidad de {producto['nombre']}: "))
            vu = float(producto['vu'])
            iva_porcentaje = float(producto['iva']) / 100 
            valor_iva_por_unidad = vu * iva_porcentaje
            subtotal = (vu + valor_iva_por_unidad) * cantidad

            detalle_datos.append({
                "codigo": cod_producto,
                "nombre": producto['nombre'],
                "cantidad": cantidad,
                "vu": vu,
                "iva_valor": valor_iva_por_unidad,
                "subtotal": subtotal
            })
            decision = input ("¿desea agregar un descuento?").lower()
        if decision : "si"
        descuento = float(input("¿de cuanto?"))
        if descuento > 50: 
            return print ("el descuento no puede superar el 50%")
        elif descuento < 50: 
         factura_descuento = (total_factura * descuento /100)
         total_factura += subtotal
         print(f"Agrego {producto['nombre']} al carrito - Subtotal: ${subtotal:,.2f}")
        else:
            print("El producto no se encontro verifica el codigo.!")
            
        if input("\n¿Desea agregar un nuevo producto? (si/no): ").lower() != "si":
            break
        elif decision : "no"
        break 
   
        

    #vista de factura en la consola
    factura_texto = f"""
   


------------------------------------------
          FACTURA DE VENTA
------------------------------------------
FECHA: {fecha_auto}
MESA:  {mesa['nombre']} (Puestos: {mesa['puesto']})
------------------------------------------
DATOS DEL CLIENTE:
ID:       {cliente['id']}
Nombre:   {cliente['nombre']}
Teléfono: {cliente['telefono']}
Email:    {cliente['email']}
------------------------------------------
DETALLE DE PRODUCTOS:
"""
    
    for dato in detalle_datos:
        factura_texto += f"Cod: {dato['codigo']} - {dato['nombre']}\n"
        factura_texto += f"Cant: {dato['cantidad']} | VU: ${dato['vu']:.0f} | IVA: ${dato['iva_valor']:.0f} | Sub: ${dato['subtotal']:,.2f}\n"
        print("------------------------------------------------")
        
    factura_texto += f"TOTAL A PAGAR: ${total_factura:,.2f}\n"
    factura_texto += "==========================================\n"
    factura_descuento += f"total a pagar nuevo: ${factura_descuento}\n"

    print(factura_texto)

    
    if input("¿Desea guardar esta factura? (si/no): ").lower() == "si":
        total_iva_factura = 0
        total_productos_factura = 0


        for dato in detalle_datos:
            total_iva_factura = total_iva_factura + (dato['iva_valor'] * dato['cantidad'])
            total_productos_factura = total_productos_factura + dato['cantidad']

        
        total_bruto_factura = total_factura - total_iva_factura

        nueva_venta = {
            "fecha": datetime.now().strftime("%d-%m-%Y"),
            "mesa": mesa["nombre"],
            "total_productos": total_productos_factura,
            "subtotal_bruto": total_bruto_factura,
            "subtotal_iva": total_iva_factura,
            "total": total_factura
        }

        ventas.append(nueva_venta)
        
        columnas_ventas = ["fecha", "mesa", "total_productos", "subtotal_bruto", "subtotal_iva", "total"]
        persistencia.guardar_archivo(ventas, "Ventas_ACME.csv", columnas_ventas)
        print("\n-- Venta guardada con éxito --")



def generar_reporte_diario(ventas):
    fecha_busqueda = input("Ingresa la fecha para el reporte (dd-mm-aaaa): ")
    
    gran_total_bruto = 0
    gran_total_iva = 0
    gran_total_ventas = 0
    encontro_ventas = False

    print("\n---------------------------------")
    print(f"REPORTE DE VENTAS - FECHA: {fecha_busqueda}")
    print("\n---------------------------------")

    for v in ventas:
        if v["fecha"] == fecha_busqueda:
            encontro_ventas = True
            
            bruto_v = float(v["subtotal_bruto"])
            iva_v = float(v["subtotal_iva"])
            total_v = float(v["total"])
            cant_v = v["total_productos"]

            print(f"Mesa: {v['mesa']} | Cant: {cant_v} | Bruto: ${bruto_v:,.0f} | IVA: ${iva_v:,.0f} | Subtotal: ${total_v:,.0f}")
            
            gran_total_bruto = gran_total_bruto + bruto_v
            gran_total_iva = gran_total_iva + iva_v
            gran_total_ventas = gran_total_ventas + total_v

    if encontro_ventas == False:
        print("No se encontraron ventas para ese día.")
    else:
        print("----------------------------------------------")
        print(f"TOTAL VENTA BRUTA: ${gran_total_bruto:,.2f}")
        print(f"TOTAL IVA:         ${gran_total_iva:,.2f}")
        print(f"TOTAL VENTAS:      ${gran_total_ventas:,.2f}")
        print("-----------------------------------------------")


#El restaurante lanza promociones, por lo cual se debe modificar el proceso de facturación para aceptar un porcentaje de descuento sobre el total.
#El comando debe:
#Solicitar código de mesa y cliente como siempre.
#Preguntar si aplica descuento (ej. 10%, 15%).
#Calcular total con descuento aplicado.
#Reflejar descuento en la factura en pantalla y en archivo JSON.

#Requisitos
#Función: facturar_con_descuento()
#Validar que el descuento sea entre 0% y 50%.
#Mostrar total antes y después del descuento.
#Entrega
#Módulo/función y ejemplo de archivo en el repo.

         


         