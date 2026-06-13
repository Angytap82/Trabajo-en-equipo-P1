import csv
import os

# --- FUNCIONES DE CARGA Y GUARDADO DE ARCHIVOS ---

def cargar_datos(ruta_archivo="paises.csv"):
    """Lee el archivo CSV y retorna una lista de diccionarios con los tipos corregidos."""
    lista_paises = []
    if not os.path.exists(ruta_archivo):
        print(f"⚠️ Error: El archivo '{ruta_archivo}' no existe. Se iniciará vacío.")
        return lista_paises
    
    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Validar y castear tipos de datos requeridos por la cátedra
                lista_paises.append({
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip()
                })
        print("✅ Datos cargados correctamente desde el CSV.")
    except (ValueError, KeyError):
        print("❌ Error de formato: El CSV contiene datos inválidos o corruptos.")
    return lista_paises


def guardar_datos(lista_paises, ruta_archivo="paises.csv"):
    """Guarda la lista de diccionarios en el archivo CSV."""
    try:
        with open(ruta_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(lista_paises)
        print("💾 Cambios guardados en el archivo CSV de forma exitosa.")
    except Exception as e:
        print(f"❌ No se pudieron guardar los datos: {e}")


# --- FUNCIONES AUXILIARES DE VALIDACIÓN ---

def solicitar_entero_positivo(mensaje):
    """Solicita un número entero por consola asegurando que sea positivo."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("⚠️ El número debe ser mayor a cero.")
        except ValueError:
            print("⚠️ Entrada inválida. Ingrese un número entero válido.")


def mostrar_tabla_paises(lista):
    """Muestra una lista de países en formato de tabla limpia por consola."""
    if not lista:
        print("🔍 No se encontraron países que coincidan con la búsqueda.")
        return
    print(f"\n{'Nombre':<15} | {'Población':<12} | {'Superficie (km²)':<16} | {'Continente':<12}")
    print("-" * 62)
    for p in lista:
        print(f"{p['nombre']:<15} | {p['poblacion']:<12} | {p['superficie']:<16} | {p['continente']:<12}")
    print()


# --- FUNCIONES PRINCIPALES DEL SISTEMA ---

def agregar_pais(lista_paises):
    """Añade un nuevo país a la lista validando campos no vacíos."""
    print("\n--- AGREGAR NUEVO PAÍS ---")
    nombre = input("Nombre del país: ").strip()
    if not nombre:
        print("❌ Error: El nombre no puede estar vacío.")
        return
    
    # Evitar duplicados simples
    for p in lista_paises:
        if p["nombre"].lower() == nombre.lower():
            print("❌ Error: Este país ya se encuentra registrado.")
            return

    poblacion = solicitar_entero_positivo("Cantidad de población: ")
    superficie = solicitar_entero_positivo("Superficie en km²: ")
    continente = input("Continente: ").strip()
    if not continente:
        print("❌ Error: El continente no puede estar vacío.")
        return

    nuevo = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    lista_paises.append(nuevo)
    print(f"✅ ¡{nombre} ha sido agregado con éxito!")


def actualizar_pais(lista_paises):
    """Modifica la población y superficie de un país existente."""
    print("\n--- ACTUALIZAR DATOS DE PAÍS ---")
    nombre = input("Ingrese el nombre del país a modificar: ").strip().lower()
    
    for p in lista_paises:
        if p["nombre"].lower() == nombre:
            print(f"📍 País encontrado: {p['nombre']}")
            p["poblacion"] = solicitar_entero_positivo("Nueva población: ")
            p["superficie"] = solicitar_entero_positivo("Nueva superficie en km²: ")
            print("✅ Datos actualizados correctamente.")
            return
    print("❌ El país ingresado no existe en los registros actuales.")


def buscar_pais(lista_paises):
    """Busca países mediante coincidencia exacta o parcial."""
    print("\n--- BUSCAR PAÍS ---")
    termino = input("Ingrese el nombre o parte del nombre a buscar: ").strip().lower()
    resultados = [p for p in lista_paises if termino in p["nombre"].lower()]
    mostrar_tabla_paises(resultados)


def filtrar_paises(lista_paises):
    """Menú secundario para filtrar los países bajo diferentes criterios."""
    print("\n--- OPCIONES DE FILTRADO ---")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    opcion = input("Seleccione una opción de filtrado: ")

    match opcion:
        case "1":
            cont = input("Ingrese el continente: ").strip().lower()
            res = [p for p in lista_paises if p["continente"].lower() == cont]
            mostrar_tabla_paises(res)
        case "2":
            min_p = solicitar_entero_positivo("Población mínima: ")
            max_p = solicitar_entero_positivo("Población máxima: ")
            res = [p for p in lista_paises if min_p <= p["poblacion"] <= max_p]
            mostrar_tabla_paises(res)
        case "3":
            min_s = solicitar_entero_positivo("Superficie mínima (km²): ")
            max_s = solicitar_entero_positivo("Superficie máxima (km²): ")
            res = [p for p in lista_paises if min_s <= p["superficie"] <= max_s]
            mostrar_tabla_paises(res)
        case _:
            print("⚠️ Opción de filtrado inválida.")


def ordenar_paises(lista_paises):
    """Ordena dinámicamente la lista por nombre, población o superficie."""
    print("\n--- OPCIONES DE ORDENAMIENTO ---")
    print("1. Por Nombre")
    print("2. Por Población")
    print("3. Por Superficie")
    criterio_opc = input("Seleccione el campo para ordenar: ")
    
    match criterio_opc:
        case "1": criterio = "nombre"
        case "2": criterio = "poblacion"
        case "3": criterio = "superficie"
        case _:
            print("⚠️ Criterio inválido.")
            return

    sentido = input("¿Desea orden Ascendente (A) o Descendente (D)?: ").strip().upper()
    reversa = True if sentido == "D" else False

    # Usamos ordenamiento lambda integrado respetando si el campo es string o numérico
    if criterio == "nombre":
        lista_ordenada = sorted(lista_paises, key=lambda x: x[criterio].lower(), reverse=reversa)
    else:
        lista_ordenada = sorted(lista_paises, key=lambda x: x[criterio], reverse=reversa)
        
    mostrar_tabla_paises(lista_ordenada)


def mostrar_estadisticas(lista_paises):
    """Calcula y expone métricas sobre el dataset cargado."""
    if not lista_paises:
        print("⚠️ No hay datos suficientes para calcular estadísticas.")
        return
    
    print("\n================ INDICADORES ESTADÍSTICOS ================")
    
    # 1. Mayor y menor población
    p_max = max(lista_paises, key=lambda x: x["poblacion"])
    p_min = min(lista_paises, key=lambda x: x["poblacion"])
    print(f"País con MAYOR población: {p_max['nombre']} ({p_max['poblacion']:,} hab.)")
    print(f"País con MENOR población: {p_min['nombre']} ({p_min['poblacion']:,} hab.)")
    
    # 2. Promedios
    prom_pob = sum(p["poblacion"] for p in lista_paises) / len(lista_paises)
    prom_sup = sum(p["superficie"] for p in lista_paises) / len(lista_paises)
    print(f"Promedio global de población: {prom_pob:,.2f} habitantes")
    print(f"Promedio global de superficie: {prom_sup:,.2f} km²")
    
    # 3. Cantidad por continente
    conteo_continentes = {}
    for p in lista_paises:
        cont = p["continente"]
        conteo_continentes[cont] = conteo_continentes.get(cont, 0) + 1
        
    print("\nCantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f" * {continente}: {cantidad}")
    print("==========================================================")


# --- MENÚ PRINCIPAL INTERACTIVO ---

def menu_principal():
    paises = cargar_datos()
    
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE PAÍSES =====")
        print("1. Mostrar todos los países")
        print("2. Agregar un país")
        print("3. Actualizar población y superficie")
        print("4. Buscar país por nombre")
        print("5. Filtrar países")
        print("6. Ordenar países")
        print("7. Mostrar indicadores estadísticos")
        print("8. Guardar cambios y Salir")
        
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        # Implementación estructural con Match Case (Python 3.10+)
        match opcion:
            case "1":
                mostrar_tabla_paises(paises)
            case "2":
                agregar_pais(paises)
            case "3":
                actualizar_pais(paises)
            case "4":
                buscar_pais(paises)
            case "5":
                filtrar_paises(paises)
            case "6":
                ordenar_paises(paises)
            case "7":
                mostrar_estadisticas(paises)
            case "8":
                guardar_datos(paises)
                print("👋 ¡Gracias por utilizar el sistema! Éxito en la entrega del TPI.")
                break
            case _:
                print("❌ Opción inválida. Intente ingresando un número del 1 al 8.")

if __name__ == "__main__":
    menu_principal()
