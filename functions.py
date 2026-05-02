import csv
import os

def crear_archivo(nombre):
    header = ['Nombre', 'Poblacion', 'Superficie', 'Continente']
    with open(nombre, mode='w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(header)
    print(f'Archivo {nombre} creado correctamente!')

def validacion_archivo(ruta):
    if os.path.exists(ruta):
        print("Archivo localizado")
        return True
    else:
        return False

def main(nombre, ruta):
    response = validacion_archivo(ruta) 
    if not response:
        crear_archivo(nombre)

main(nombre='paises.csv', ruta='paises.csv')