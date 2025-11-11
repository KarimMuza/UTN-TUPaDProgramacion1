import csv
from typing import List, Dict, Any, Optional
from manejo_datos import (
    agregar_pais, 
    actualizar_datos_pais, 
    buscar_pais_por_nombre, 
    menu_filtrado, 
    menu_ordenamiento, 
    mostrar_estadisticas
)

# Alias para el tipo de dato principal (para consistencia de tipado)
Catalogo = List[Dict[str, Any]]

# --- CONFIGURACIÓN ---
NOMBRE_ARCHIVO_CSV = 'paises.csv'

def cargar_catalogo_desde_csv(nombre_archivo: str) -> Optional[Catalogo]:
    """
    Carga los datos de países desde un archivo CSV.
    Implementa manejo de errores robusto (Requisito CSV).
    """
    catalogo: Catalogo = []
    try: 
        with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Intenta la conversión de tipos
                    pais: Dict[str, Any] = {
                        'nombre': row['nombre'].strip(),
                        'poblacion': int(row['poblacion']),
                        'superficie': int(row['superficie']),
                        'continente': row['continente'].strip()
                    }
                    catalogo.append(pais)
                except ValueError:
                    # Manejo de error si Población o Superficie no son números
                    print(f" Error de formato en el CSV (Población/Superficie no es un número en la fila): {row}")
            return catalogo
    except FileNotFoundError:
        # Manejo de error si el archivo no existe
        print(f" ERROR CRÍTICO: No se encontró el archivo '{nombre_archivo}'. Asegúrese de que esté en la misma carpeta.")
        return None

def mostrar_menu() -> None:
    """Muestra el menú de opciones en consola."""
    print("\n" + "="*40)
    print("      GESTOR DE PAÍSES - UTN      ")
    print("="*40)
    print("1. Agregar un país")
    print("2. Actualizar datos (Población/Superficie)")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Guardar y Salir")
    print("="*40)

def menu_principal(catalogo: Catalogo) -> None:
    """Maneja el flujo principal del programa."""
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción (1-7): ")

        if opcion == '1':
            agregar_pais(catalogo)
        elif opcion == '2':
            actualizar_datos_pais(catalogo)
        elif opcion == '3':
            buscar_pais_por_nombre(catalogo)
        elif opcion == '4':
            menu_filtrado(catalogo)
        elif opcion == '5':
            menu_ordenamiento(catalogo)
        elif opcion == '6':
            mostrar_estadisticas(catalogo)
        elif opcion == '7':
            # Aquí iría la lógica para guardar el 'catalogo' actualizado a un nuevo CSV si fuera necesario
            print(" Guardando y saliendo... ¡Programa finalizado con éxito!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# --- INICIO DEL PROGRAMA (La línea de encendido) ---
if __name__ == "__main__":
    print("Cargando catálogo de países...")
    CATALOGO = cargar_catalogo_desde_csv(NOMBRE_ARCHIVO_CSV)
    
    # Si la carga fue exitosa, ejecuta el menú. Si no, termina.
    if CATALOGO is not None:
        menu_principal(CATALOGO)
    else:
        print("El programa ha terminado debido a un error de carga de datos.")
