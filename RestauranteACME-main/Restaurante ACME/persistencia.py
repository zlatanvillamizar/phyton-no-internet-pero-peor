import csv
import os
import json


def factura_descuento():
 print 



def guardar_archivo(lista, nombre_archivo, campos):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(lista)

def cargar_datos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lectura = csv.DictReader(archivo)
        return list(lectura)
    


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