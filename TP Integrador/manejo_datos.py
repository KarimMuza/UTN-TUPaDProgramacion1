# Importaciones para tipado y robustez del código
from typing import List, Dict, Any, Optional

# Alias para el tipo de dato principal (Lista de Diccionarios)
Catalogo = List[Dict[str, Any]]

# --- Función Auxiliar para mostrar resultados ---

def imprimir_paises(paises: Catalogo) -> None:
    """
    Imprime una lista de países de forma clara.
    
    Args:
        paises (Catalogo): La lista de países a imprimir.
    """
    if not paises:
        print("\n[AVISO]: No se encontraron resultados que cumplan los criterios.")
        return
        
    print(f"\n--- Resultados ({len(paises)} encontrados) ---")
    for i, pais in enumerate(paises):
        # Usamos : , para formato de miles
        print(f"{i+1}. {pais['nombre']}: Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km² | Continente: {pais['continente']}")
    print("-" * 40)


# --- 1. Agregar y Actualizar (Funcionalidad CRUD) ---

def agregar_pais(catalogo: Catalogo) -> None:
    """
    Permite al usuario agregar un nuevo país al catálogo (Requisito Agregar).
    Implementa manejo de errores para Población/Superficie.
    """
    print("\n--- AGREGAR PAÍS ---")
    
    nombre = input("Ingrese el Nombre del país (no vacío): ").strip().capitalize()
    if not nombre:
        print("❌ Error: El nombre no puede estar vacío.")
        return

    # Manejo de Errores para entradas numéricas
    try:
        poblacion = int(input("Ingrese la Población (solo números): "))
        superficie = int(input("Ingrese la Superficie en km² (solo números): "))
    except ValueError:
        print("❌ Error de formato: Población y Superficie deben ser números enteros.")
        return

    continente = input("Ingrese el Continente: ").strip().capitalize()
    
    nuevo_pais: Dict[str, Any] = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    
    catalogo.append(nuevo_pais)
    print(f"✅ Éxito: País '{nombre}' agregado al catálogo.")

def actualizar_datos_pais(catalogo: Catalogo) -> None:
    """
    Actualiza la Población y Superficie de un país existente (Requisito Actualizar).
    """
    nombre_buscar = input("Ingrese el nombre exacto del país a actualizar: ").strip().lower()
    
    pais_encontrado: Optional[Dict[str, Any]] = None
    for pais in catalogo:
        if pais['nombre'].lower() == nombre_buscar:
            pais_encontrado = pais
            break
            
    if pais_encontrado is None:
        print(f"❌ Error: País '{nombre_buscar.capitalize()}' no encontrado.")
        return
        
    print(f"Actualizando datos para: {pais_encontrado['nombre']}")

    try:
        nueva_poblacion = input(f"Nueva Población (actual: {pais_encontrado['poblacion']:,}, deje vacío para no cambiar): ")
        if nueva_poblacion:
            pais_encontrado['poblacion'] = int(nueva_poblacion)

        nueva_superficie = input(f"Nueva Superficie (actual: {pais_encontrado['superficie']:,}, deje vacío para no cambiar): ")
        if nueva_superficie:
            pais_encontrado['superficie'] = int(nueva_superficie)
            
        print(f"✅ Éxito: Datos de {pais_encontrado['nombre']} actualizados.")

    except ValueError:
        print("❌ Error de formato: Población y Superficie deben ser números enteros.")


# --- 2. Búsqueda y Filtro ---

def buscar_pais_por_nombre(catalogo: Catalogo) -> None:
    """
    Busca un país por nombre (coincidencia parcial o exacta) e imprime los resultados (Requisito Buscar).
    """
    if not catalogo:
        print("[AVISO] El catálogo está vacío.")
        return

    nombre_buscado = input("Ingrese el nombre (o parte del nombre) del país a buscar: ").strip().lower()
    
    # Uso de list comprehensions para filtrar de forma eficiente
    resultados = [
        pais 
        for pais in catalogo 
        if nombre_buscado in pais['nombre'].lower()
    ]
    
    imprimir_paises(resultados)

def menu_filtrado(catalogo: Catalogo) -> None:
    """Maneja el submenú de opciones de filtrado (Requisito Filtrar)."""
    print("\n--- OPCIONES DE FILTRADO ---")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    opcion = input("Seleccione el criterio de filtro (1-3): ")
    
    if opcion == '1':
        continente = input("Ingrese el Continente a filtrar: ").strip().capitalize()
        resultados = filtrar_por_continente(catalogo, continente)
        imprimir_paises(resultados)
    elif opcion == '2':
        filtrar_por_rango(catalogo, 'poblacion', 'Población')
    elif opcion == '3':
        filtrar_por_rango(catalogo, 'superficie', 'Superficie')
    else:
        print("Opción no válida.")


def filtrar_por_continente(catalogo: Catalogo, continente_a_filtrar: str) -> Catalogo:
    """Filtra países por un continente específico y retorna la lista resultante."""
    return [
        pais 
        for pais in catalogo 
        if pais['continente'].lower() == continente_a_filtrar.lower()
    ]

def filtrar_por_rango(catalogo: Catalogo, clave: str, nombre_clave: str) -> None:
    """
    Filtra países por un rango de valores numéricos (Población o Superficie).
    Incluye manejo de errores si los límites no son números.
    """
    try:
        min_val = int(input(f"Ingrese el valor mínimo para {nombre_clave}: "))
        max_val = int(input(f"Ingrese el valor máximo para {nombre_clave}: "))
        
        resultados = [
            pais 
            for pais in catalogo 
            if min_val <= pais[clave] <= max_val
        ]
        
        imprimir_paises(resultados)

    except ValueError:
        print("❌ Error de formato: Los valores de rango deben ser números enteros.")


# --- 3. Ordenamiento ---

def menu_ordenamiento(catalogo: Catalogo) -> None:
    """Maneja el submenú de opciones de ordenamiento (Requisito Ordenar)."""
    print("\n--- OPCIONES DE ORDENAMIENTO ---")
    print("1. Por Nombre")
    print("2. Por Población")
    print("3. Por Superficie")
    opcion = input("Seleccione el criterio de ordenamiento (1-3): ")
    
    # Define la clave para ordenar
    if opcion == '1':
        clave = 'nombre'
    elif opcion == '2':
        clave = 'poblacion'
    elif opcion == '3':
        clave = 'superficie'
    else:
        print("Opción no válida.")
        return

    # Pide si es ascendente o descendente
    orden = input("Ordenar ASCENDENTE (A) o DESCENDENTE (D)? ").strip().upper()
    reverse = (orden == 'D')

    # Crea una copia ordenada de la lista para no modificar el original
    # Usa lambda para ordenar por clave dinámica
    catalogo_ordenado = sorted(catalogo, key=lambda pais: pais[clave], reverse=reverse)
    imprimir_paises(catalogo_ordenado)

# --- 4. Estadísticas ---

def mostrar_estadisticas(catalogo: Catalogo) -> None:
    """
    Calcula y muestra estadísticas básicas sobre el catálogo (Requisito Estadísticas).
    """
    if not catalogo:
        print("[AVISO] El catálogo está vacío. No hay estadísticas para mostrar.")
        return

    print("\n" + "~"*40)
    print("     ESTADÍSTICAS BÁSICAS      ")
    print("~"*40)

    # 1. País con mayor y menor población (Uso de max/min con lambda)
    pais_mayor_pob = max(catalogo, key=lambda p: p['poblacion'])
    pais_menor_pob = min(catalogo, key=lambda p: p['poblacion'])

    print(f"País con MAYOR población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,})")
    print(f"País con MENOR población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,})")
    print("-" * 40)
    
    # 2. Promedio de población
    total_poblacion = sum(p['poblacion'] for p in catalogo)
    promedio_poblacion = total_poblacion / len(catalogo)
    print(f"Promedio de Población: {int(promedio_poblacion):,}")
    
    # 3. Promedio de superficie
    total_superficie = sum(p['superficie'] for p in catalogo)
    promedio_superficie = total_superficie / len(catalogo)
    print(f"Promedio de Superficie: {int(promedio_superficie):,} km²")
    print("-" * 40)

    # 4. Cantidad de países por continente (Uso de diccionario para conteo)
    conteo_continentes: Dict[str, int] = {} 
    for pais in catalogo:
        continente = pais['continente']
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1
        
    print("Cantidad de Países por Continente:")
    for cont, count in conteo_continentes.items():
        print(f"- {cont}: {count} países")
    print("~"*40)

    