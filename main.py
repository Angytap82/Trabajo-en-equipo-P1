import csv
from functions import * 

def cargar_datos(nombre_archivo):
    lista_paises = []
    response = validacion_archivo(nombre_archivo) 
    if not response:
        crear_archivo(nombre_archivo)
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Convertimos los números de texto a enteros para poder calcular
                fila['poblacion'] = int(fila['poblacion'])
                fila['superficie'] = int(fila['superficie'])
                lista_paises.append(fila)
        return lista_paises
    except FileNotFoundError:
        print("\n[Error] No se encontró el archivo 'paises.csv'.")
        return []

def buscar_pais(lista, nombre_buscar):
    for pais in lista:
        if pais['nombre'].lower() == nombre_buscar.lower():
            return pais
    return None

def main():
    paises = []
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Cargar países desde CSV")
        print("2. Buscar un país por nombre")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        match int(opcion):
            case 1:
                paises = cargar_datos("paises.csv")
                if paises:
                    print(f"\n¡Éxito! Se cargaron {len(paises)} países.")
            case 2:
                if not paises:
                    print("\n[!] Primero debes cargar los datos (Opción 1).")
                else:
                    nombre = input("Nombre del país a buscar: ")
                    resultado = buscar_pais(paises, nombre)
                    if resultado:
                        print(f"\nDatos de {resultado['nombre']}:")
                        print(f"- Población: {resultado['poblacion']}")
                        print(f"- Superficie: {resultado['superficie']} km²")
                        print(f"- Continente: {resultado['continente']}")
                    else:
                        print("\nPaís no encontrado.")
            case 3:
                print("Saliendo...")
                break
            case 4:
                print("Opción no válida.")

if __name__ == "__main__":
    main()
