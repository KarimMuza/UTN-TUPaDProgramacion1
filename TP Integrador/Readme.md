Gestor de Información de Países (Programación 1)


Octavio Fredes
Karim Muzaber

---

Este proyecto aplica y define con precisión los siguientes conceptos de la materia:

 Estructuras de Datos
*Listas* :La estructura principal utilizada es una Lista de Diccionarios (CATALOGO). Esto permite almacenar una colección ordenada de registros de países y facilita la iteración, el filtrado y el ordenamiento eficiente de los datos.
*Diccionarios* : Cada país dentro del catálogo es un diccionario individual. El diccionario se utiliza para modelar el registro de cada país, permitiendo acceder a sus atributos de forma descriptiva a través de claves (nombre, poblacion, continente, etc).

 Arquitectura y Lógica 
*Funciones y Modularización*: El proyecto esta modularizado, dividido en dos archivos para una separación clara de responsabilidades:
    * *main.py*: Contiene la interfaz de usuario, la lógica de encendido y la carga de datos.
    * *manejo_datos.py:* Contiene la Lógica de Negocio (implementación de las funciones de CRUD, Búsqueda, Filtros, Ordenamiento y Estadísticas).
 *Ordenamientos*:Se utiliza la función nativa sorted() de Python junto con expresiones lambda para ordenar el catálogo dinámicamente por Nombre, Población o Superficie, según el criterio elegido por el usuario.
 *Estadísticas Básicas*: Se implementan cálculos de País con mayor/menor población, Promedios de población y superficie, y conteo por continente, utilizando funciones max(), min(), sum() y diccionarios para el conteo.

Robustez y Manejo de Errores 
*Manejo de Archivos (CSV)*:Se utiliza el módulo csv para la lectura. La función cargar_catalogo_desde_csv utiliza la sentencia try/except para garantizar una lectura robusta
*Validaciones y Excepciones*: Se controla si el archivo paises.csv no existe (FileNotFoundError). Además, se manejan errores de tipo (ValueError) si el usuario ingresa texto en campos numéricos (Población/Superficie), garantizando mensajes claros de éxito o error al usuario.

---

 Entregables y Estructura del Software

# Estructura de la Carpeta Digital
El proyecto se entrega en un repositorio público de GitHub y contiene los siguientes archivos, todos en la misma carpeta:
1.  *main.py*
2.  *manejo_datos.py*
3.  *paises.csv* 
4.  *README.md* 

Instrucciones de Uso y Ejecución
1.  Asegúrese de tener Python 3.x instalado.
2.  Coloque los archivos main.py, manejo_datos.py y paises.csv en la misma carpeta.
3.  Abra la terminal en esa carpeta y ejecute: main.py
4.  El programa iniciará el menú de opciones automáticamente.

Conclusion 

El desarrollo de este proyecto integrador nos proporcionó aprendizajes significativos en el uso de estructuras de datos, la arquitectura del software y el manejo de errores.

Modularidad Efectiva: Comprendimos que separar el código en módulos (main.py para la Interfaz y manejo_datos.py para la Lógica) es fundamental. Esta división facilitó la depuración y hace que el código sea altamente mantenible y escalable.
Eficiencia de Estructuras: El uso combinado de la Lista de Diccionarios junto con funciones avanzadas de Python permitió implementar funcionalidades complejas (como el ordenamiento dinámico y el cálculo de estadísticas) con un código muy limpio y eficiente.