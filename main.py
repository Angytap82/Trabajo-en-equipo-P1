import csv
import os

# --- FUNCIONES DE CARGA Y GUARDADO DE ARCHIVOS ---

def cargar_datos(ruta_archivo="paises.csv"):
    # Lee el archivo CSV y retorna una lista de diccionarios con los tipos corregidos.
    # creamos la una lista inicial vacia
    lista_paises = []
    # aplicamos una validacion para verificar si el archivo csv inicial existe
    if not os.path.exists(ruta_archivo):
        print(f"⚠️ Error: El archivo '{ruta_archivo}' no existe. Se iniciará vacío.")
        # si falla retornamos la lista vacia
        return lista_paises
    
    # aplicamos un try/except para capturar posibles errores
    try:
        # utilizamos open() en modo lectura con la codificacion universal utf-8 para leer el archivo
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            # Utilizamos la clase DictReader de csv para leer y convertir cada fila del archivo en un diccionario
            lector = csv.DictReader(archivo)
            # Realizamos un iteracion con un bucle for de cada fila
            for fila in lector:
                # Validar y castear tipos de datos requeridos por la cátedra
                # Y agregarlos a la lista
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
    # Guarda la lista de diccionarios en el archivo CSV.

    # aplicamos un try/except para capturar posibles errores
    try:
        # utilizamos open() en modo escritura con la codificacion universal utf-8 para escribir en el archivo
        with open(ruta_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            # columnas que tendra el archivo csv resultante
            campos = ["nombre", "poblacion", "superficie", "continente"]
            # Utilizamos la clase DictWriter de csv para escribir cada fila en el archivo especificado en el parametro "ruta_archivo" 
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            # Funcion para escribir la primer fila con los nombres de las columnas
            escritor.writeheader()
            # Funcion para escribir los datos 
            escritor.writerows(lista_paises)
        print("💾 Cambios guardados en el archivo CSV de forma exitosa.")
    except Exception as e:
        print(f"❌ No se pudieron guardar los datos: {e}")


# --- FUNCIONES AUXILIARES DE VALIDACIÓN ---

def solicitar_entero_positivo(mensaje):
    # Solicita un número entero por consola asegurando que sea positivo.

    # Utilizamos un bucle while para permitir reingreso de datos 
    while True:
        # utilizamos try/except para capturar el error en el casteo a entero
        try:
            # solicitamos que se ingrese un valor y casteamos a entero
            valor = int(input(mensaje))
            # validamos que el valor sea un numero mayor a 0
            if valor > 0:
                return valor
            print("⚠️ El número debe ser mayor a cero.")
        except ValueError:
            print("⚠️ Entrada inválida. Ingrese un número entero válido.")


def mostrar_tabla_paises(lista):
    # Muestra una lista de países en formato de tabla limpia por consola.
    # Validamos la existencia de la lista, si no existe salimos de la funcion
    if not lista:
        print("🔍 No se encontraron países que coincidan con la búsqueda.")
        return
    # si existe mostramos en pantalla los datos
    print(f"\n{'Nombre':<15} | {'Población':<12} | {'Superficie (km²)':<16} | {'Continente':<12}")
    print("-" * 62)
    for p in lista:
        print(f"{p['nombre']:<15} | {p['poblacion']:<12} | {p['superficie']:<16} | {p['continente']:<12}")
    print()

# --- FUNCIONES PRINCIPALES DEL SISTEMA ---

def agregar_pais(lista_paises):
    # Añade un nuevo país a la lista validando campos no vacíos.
    print("\n--- AGREGAR NUEVO PAÍS ---")
    
    # Uso de while para permitir reingreso de datos
    while True:
        # Solicitamos el ingreso del nombre del pais
        nombre = input("Nombre del país: ").strip()

        # Validamos que se ingrese un nombre
        if not nombre:
            print("❌ Error: El nombre no puede estar vacío.")
            continue
    
        # Evitar duplicados simples
        # Creamos una variable bandera
        duplicado = False
        for p in lista_paises:
            if p["nombre"].lower() == nombre.lower():
                print("❌ Error: Este país ya se encuentra registrado.")
                # Si hay duplicado actualizamos la variable a True
                duplicado = True
                break 

        # Si es true reiniciamos el bucle
        if duplicado:
           continue 

        # si todo sale bien salimos del bucle
        break

    # llamamos a la funcion auxiliar 'solicitar_entero_positivo' que nos pedira ingresar un numero y
    # nos retornara un valor numerico entero
    poblacion = solicitar_entero_positivo("Cantidad de población: ")
    superficie = solicitar_entero_positivo("Superficie en km²: ")

    # Aplicamos otro bucle while 
    while True:
        # Solicitamos que se ingrese un Continente
        continente = input("Continente: ").strip()

        # Validamos que se haya ingresado el dato
        if not continente:
            print("❌ Error: El continente no puede estar vacío.")
            continue
        break

    # Si los datos son validos procedemos a crear un diccionario con los valores correspondientes
    # e insertarlos en la lista
    nuevo = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    lista_paises.append(nuevo)
    print(f"✅ ¡{nombre} ha sido agregado con éxito!")


def actualizar_pais(lista_paises):
    # Modifica la población y superficie de un país existente.
    print("\n--- ACTUALIZAR DATOS DE PAÍS ---")

    while True:
        # Solicitamos que se ingrese un nombre 
        nombre = input("Ingrese el nombre del país a modificar (o 'salir'): ").strip().lower()

        # Validamos que se ingrese un nombre
        if not nombre:
            print("❌ Error: El nombre no puede estar vació")
            continue

        if nombre == 'salir':
            print("Operación cancelada.")
            return

        # Creamos una variable para almacenar el pais si es encontrado
        pais_encontrado = None
        # Iteramos la lista de paises con un for
        for p in lista_paises:
            # Si hay coincidencia agregamos el pais a la variable anteriormente declarada 
            if p["nombre"].lower() == nombre:
                pais_encontrado = p
                # break para salir del bucle for
                break

        # aplicamos un condicional para ejecutar la correspondiente accion
        if pais_encontrado:
                print(f"📍 País encontrado: {pais_encontrado['nombre']}")
                pais_encontrado["poblacion"] = solicitar_entero_positivo("Nueva población: ")
                pais_encontrado["superficie"] = solicitar_entero_positivo("Nueva superficie en km²: ")
                print("✅ Datos actualizados correctamente.")
                return
        else:
            print("❌ El país ingresado no existe en los registros actuales.")
            return


def buscar_pais(lista_paises):
    # Busca países mediante coincidencia exacta o parcial.
    print("\n--- BUSCAR PAÍS ---")
    termino = input("Ingrese el nombre o parte del nombre a buscar: ").strip().lower()

    # Validamos que se hayan ingresados datos
    if not termino:
        print("⚠️ No ingresaste ningún término de búsqueda.")
        return

    # Generamos una lista con los datos encontrados (metodo: compresion de lista)
    resultados = [p for p in lista_paises if termino in p["nombre"].lower()]

    # Si existen datos se lo pasamos como argumento a la funcion 'mostrar_tabla_paises'
    if resultados:
        mostrar_tabla_paises(resultados)
    else:
        print(f"❌ No se encontraron países que coincidan con '{termino}'.")


def filtrar_paises(lista_paises):
    # Menú secundario para filtrar los países bajo diferentes criterios.
    print("\n--- OPCIONES DE FILTRADO ---")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")

    # Solicitamos el ingreso de una opcion
    opcion = input("Seleccione una opción de filtrado: ")

    # Aplicamo un match case para el manejo de ejecucion de las opciones
    match opcion:
        case "1":
            # Pedimos el continente
            cont = input("Ingrese el continente: ").strip().lower()
            # Validamos el dato
            if not cont:
                print("⚠️ El continente no puede estar vacío.")
                return

            # Obtenemos una lista con el dato encontrado o vacia de no existir
            res = [p for p in lista_paises if p["continente"].lower() == cont]

            # Validamos su existencia
            if res:
                # Ejecutamos la funcion pasandole como argumento la lista
                mostrar_tabla_paises(res)
            else:
                print(f"❌ No se encontraron países en el continente '{cont.title()}'.")

        case "2":
            # Solicitamos que se ingrese la poblacion minima
            min_p = solicitar_entero_positivo("Población mínima: ")

            # Bucle while para permitir el reingreso de datos
            while True:
                # Solicitamos que se ingrese la poblacion maxima 
                max_p = solicitar_entero_positivo("Población máxima: ")
                # Validamos que la maxima sea mayor o igual que la minima
                if max_p >= min_p:
                    break
                print(f"⚠️ La población máxima debe ser mayor o igual a la mínima ({min_p}).")

            # Obtenemos una lista con el dato encontrado o vacia de no existir
            res = [p for p in lista_paises if min_p <= p["poblacion"] <= max_p]
            
            # Validamos su existencia
            if res:
                # Ejecutamos la funcion pasandole como argumento la lista
                mostrar_tabla_paises(res)
            else:
                print("❌ No hay países en ese rango de población.")

        case "3":
            # Solicitamos la superficie minima
            min_s = solicitar_entero_positivo("Superficie mínima (km²): ")
            # Bucle while para permitir el reingreso de datos
            while True:
                # Solicitamos la superficie maxima
                max_s = solicitar_entero_positivo("Superficie máxima (km²): ")
                # Validamos que la maxima sea mayor o igual que la minima
                if max_s >= min_s:
                    break
                print(f"⚠️ La superficie máxima debe ser mayor o igual a la mínima ({min_s} km²).")

            # Obtenemos una lista con el dato encontrado o vacia de no existir
            res = [p for p in lista_paises if min_s <= p["superficie"] <= max_s]

            # Validamos su existencia
            if res:
                # Ejecutamos la funcion pasandole como argumento la lista
                mostrar_tabla_paises(res)
            else:
                print("❌ No hay países en ese rango de superficie.")
        case _:
            print("⚠️ Opción de filtrado inválida.")

def ordenar_paises(lista_paises):
    # Ordena dinámicamente la lista por nombre, población o superficie.
    print("\n--- OPCIONES DE ORDENAMIENTO ---")
    print("1. Por Nombre")
    print("2. Por Población")
    print("3. Por Superficie")
    criterio_opc = input("Seleccione el campo para ordenar: ")
    
    # Match case para manejar las opciones
    match criterio_opc:
        case "1": criterio = "nombre"
        case "2": criterio = "poblacion"
        case "3": criterio = "superficie"
        case _:
            print("⚠️ Criterio inválido.")
            return

    # Bucle while para permitir el reingreso de datos en caso de ser incorrectos
    while True:
        sentido = input("¿Desea orden Ascendente (A) o Descendente (D)?: ").strip().upper()
        # Si esta dentro del rango de opciones salimos del bucle
        if sentido in ["A", "D"]:
            break 
        print("⚠️ Entrada inválida. Por favor, ingrese solo 'A' o 'D'.\n")

    reversa = True if sentido == "D" else False

    # Usamos ordenamiento lambda integrado respetando si el campo es string o numérico
    if criterio == "nombre":
        # dentro del sorted utilizamos una funcion lambda que extrae el criterio de ordenamiento en minuscula
        lista_ordenada = sorted(lista_paises, key=lambda x: x[criterio].lower(), reverse=reversa)
    else:
        lista_ordenada = sorted(lista_paises, key=lambda x: x[criterio], reverse=reversa)
        
    mostrar_tabla_paises(lista_ordenada)

def mostrar_estadisticas(lista_paises):
    # Calcula y expone métricas sobre el dataset cargado.

    # Validamos la existencia de la lista
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
    # Realizamos una iteracion con un for de la lista
    for p in lista_paises:
        # almacenamos el continente en la variable
        cont = p["continente"].strip().title()
        # Actualizamos el diccionario previamente creado
        conteo_continentes[cont] = conteo_continentes.get(cont, 0) + 1
        
    print("\nCantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f" * {continente}: {cantidad}")
    print("==========================================================")

# --- MENÚ PRINCIPAL INTERACTIVO ---

def menu_principal():
    # Ejecutamos la funcion cargar_datos y guardamos el retorno en una variable
    paises = cargar_datos()
    
    # Aplicamos un while para el reingreso de datos
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

        # capturamos la opción ingresada por el usuario
        opcion = input("Seleccione una opción (1-8): ").strip()

        # Utilizamos un match case para el manejo de la ejecucion de las opciones ingresadas por el usuario 
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