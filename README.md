# Sistema de Gestión de Países

## Descripción

Sistema desarrollado en Python para la gestión de información de países utilizando persistencia de datos en archivos CSV. Permite registrar, consultar, actualizar, filtrar, ordenar y analizar información relacionada con países, incluyendo nombre, población, superficie y continente.

El programa funciona mediante una interfaz interactiva por consola y almacena los datos en un archivo denominado `paises.csv`.

---

## Características

* Carga automática de datos desde un archivo CSV.
* Almacenamiento persistente de información en CSV.
* Alta de nuevos países.
* Validación de datos ingresados por el usuario.
* Prevención de registros duplicados.
* Actualización de población y superficie de países existentes.
* Búsqueda de países por nombre o coincidencia parcial.
* Filtrado de países por:

  * Continente.
  * Rango de población.
  * Rango de superficie.
* Ordenamiento de países por:

  * Nombre.
  * Población.
  * Superficie.
* Generación de indicadores estadísticos.
* Visualización tabular de resultados.

---

## Requisitos

### Python

* Python 3.10 o superior.

### Librerías utilizadas

El proyecto utiliza únicamente librerías estándar de Python:

* `csv`
* `os`

No requiere instalación de dependencias externas.

---

## Instalación

1. Clonar o descargar el proyecto.

```bash
git clone <repositorio>
```

o copiar los archivos manualmente.

2. Verificar que Python esté instalado:

```bash
python --version
```

3. Ubicar el archivo principal del programa y el archivo de datos `paises.csv` en el mismo directorio.

Estructura mínima requerida:

```text
proyecto/
│
├── main.py
├── paises.csv
└── README.md
```

---

## Uso

Ejecutar el programa desde una terminal:

```bash
python main.py
```

Al iniciar, el sistema cargará automáticamente los datos almacenados en `paises.csv`.

### Menú principal

```text
===== SISTEMA DE GESTIÓN DE PAÍSES =====

1. Mostrar todos los países
2. Agregar un país
3. Actualizar población y superficie
4. Buscar país por nombre
5. Filtrar países
6. Ordenar países
7. Mostrar indicadores estadísticos
8. Guardar cambios y Salir
```

Los cambios realizados durante la ejecución se almacenan al seleccionar la opción:

```text
8. Guardar cambios y Salir
```

---

## Ejemplos de Entrada y Salida

### Agregar un país

#### Entrada

```text
Nombre del país: Argentina
Cantidad de población: 47000000
Superficie en km²: 2780400
Continente: América
```

#### Salida

```text
✅ ¡Argentina ha sido agregado con éxito!
```

---

### Buscar país

#### Entrada

```text
Ingrese el nombre o parte del nombre a buscar: arg
```

#### Salida

```text
Nombre          | Población     | Superficie (km²) | Continente
--------------------------------------------------------------
Argentina       | 47000000      | 2780400          | América
```

---

### Estadísticas

#### Salida

```text
================ INDICADORES ESTADÍSTICOS ================

País con MAYOR población: India (1400000000 hab.)
País con MENOR población: Uruguay (3500000 hab.)

Promedio global de población: 250000000.00 habitantes
Promedio global de superficie: 1200000.00 km²

Cantidad de países por continente:
 * América: 5
 * Europa: 4
 * Asia: 3

==========================================================
```

*Los valores mostrados dependen de los datos contenidos en `paises.csv`.*

---

## Estructura del Proyecto

```text
proyecto/
│
├── main.py          # Programa principal
├── paises.csv       # Archivo de almacenamiento de datos
└── README.md        # Documentación del proyecto
```

### Componentes principales

* **Carga y guardado de datos**

  * `cargar_datos()`
  * `guardar_datos()`

* **Validaciones**

  * `solicitar_entero_positivo()`

* **Visualización**

  * `mostrar_tabla_paises()`

* **Gestión de países**

  * `agregar_pais()`
  * `actualizar_pais()`
  * `buscar_pais()`

* **Consultas**

  * `filtrar_paises()`
  * `ordenar_paises()`

* **Estadísticas**

  * `mostrar_estadisticas()`

* **Interfaz principal**

  * `menu_principal()`

---

## Participación de los Integrantes

| Integrante | Participación                                              |
| ---------- | ---------------------------------------------------------- |
| Facundo    | Desarrollo, análisis, pruebas y documentación del proyecto |
| Maria      | Desarrollo, análisis, pruebas y documentación del proyecto |

---

## Consideraciones Técnicas

* Los datos se almacenan utilizando el formato CSV.
* Se emplea `csv.DictReader` para la lectura de registros.
* Se utiliza `csv.DictWriter` para la escritura de datos.
* El sistema valida que los valores numéricos sean enteros positivos.
* Se evita el registro de países duplicados mediante comparación de nombres.
* El programa utiliza estructuras de datos basadas en listas y diccionarios.
* El menú interactivo está implementado mediante la instrucción `match-case`.
* La persistencia de datos se realiza únicamente cuando el usuario selecciona la opción de guardar y salir.
* El sistema incluye manejo básico de errores para archivos inexistentes y formatos inválidos.

---

## Conclusión

El Sistema de Gestión de Países es una aplicación de consola que permite administrar información geográfica básica mediante registros, consultas, filtros, ordenamientos y generación de estadísticas. La utilización de archivos CSV como mecanismo de persistencia simplifica el almacenamiento de datos y facilita la portabilidad del proyecto.

## Enlaces

* Video: https://drive.google.com/file/d/1O1NF3KOnEjqbxebGSZe5j-t8M3OXRqTh/view?usp=sharing
* PDF: 