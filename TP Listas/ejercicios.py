#Ejercicio1
notas = [8,9,10,3,5,7,2,4,7,8]
suma = 0
mayor = notas[0]
menor = notas[0]
print(notas)
for i in notas:
    suma += i
    if i > mayor:
        mayor = i
    if i < menor:
        menor = i
promedio = suma / len(notas)
print(f"La nota mas alta fue {mayor}, la nota mas baja fue {menor}, y el promedio de todas las notas fue {promedio}")

#Ejercicio2
productos = []
for i in range(5):
    prod = input(f"Ingresa el producto {i + 1}: ")
    productos.append(prod)
print("Lista ordenada alfabeticamente: ")
print(sorted(productos))

eliminar = input("Indique el producto que desee eliminar: ")

if eliminar in productos:
    productos.remove(eliminar)
    print("Lista actualizada: ", productos)
else:
    print("El producto no existe en la lista")
    
#Ejercicio3
import random
numeros = [random.randint(1,100) for n in range(15)]
pares = []
impares = []
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print("Los números pares son: ", pares)
print("Los números impares son: ", impares)

#Ejercicio4
datos = [1,3,5,3,7,1,9,5,3]
print("Lista original: ", datos)
sin_repetir = []
for i in datos:
    if i not in sin_repetir:
        sin_repetir.append(i)
print("Lista sin repetidos: ",sin_repetir)

#Ejercicio5
estudiantes = ["Karim", "Octavio", "Martin", "Juan", "Pedro", "Carolina", "Maximiliano", "Luis"]
print(f"Estudiantes: {estudiantes}")
accion = input("Decidi si queres ''agregar'' un nuevo estudiante o ''eliminar'' uno existente").strip().lower()
if accion == "agregar":
    nuevo = input("Ingresa el nombre del estudiante que queres agregar: ").strip().capitalize()
    estudiantes.append(nuevo)
elif accion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ").strip().capitalize()
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
    else:
        print(f"{eliminar} no esta en la lista de estudiantes")
else:
    print("La opcion no es valida")
print(f"Lista final de estudiantes: {estudiantes}")

#Ejercicio6
numeros = [1,2,3,4,5,6,7]
invertir = [numeros[-1]] + [numeros[:-1]]
print(f"Lista original: {numeros}")
print(f"Lista invertida {invertir}")

#Ejercicio7
temperaturas = [
    [12, 20],  
    [10, 18],  
    [8, 22],   
    [14, 25],  
    [11, 19],  
    [9, 21],   
    [13, 24]   
]

minimas = [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]

prom_min = sum(minimas) / len(minimas)
prom_max = sum(maximas) / len(maximas)

print("Promedio de mínimas:", prom_min)
print("Promedio de máximas:", prom_max)

amplitud = [dia[1] - dia[0] for dia in temperaturas]

mayor_amp = max(amplitud)
dia_mayor_amp = amplitud.index(mayor_amp) + 1 

print(f"La mayor amplitud térmica fue de {mayor_amp}° en el día {dia_mayor_amp}.")

#Ejercicio8
notas = [
    [7, 8, 9],
    [6, 5, 7],
    [10, 9, 8],
    [4, 6, 5],
    [9, 8, 10]
]
print("Matriz de notas (5 estudiantes x 3 materias):")
for fila in notas:
    print(fila)

print("\n--- Promedio de cada estudiante ---")
for i in range(len(notas)):
    promedio_est = sum(notas[i]) / len(notas[i])
    print(f"Estudiante {i+1}: {promedio_est}")

print("\n--- Promedio de cada materia ---")
num_materias = len(notas[0])
for j in range(num_materias):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    promedio_mat = suma / len(notas)
    print(f"Materia {j+1}: {promedio_mat}")
    
    
#Ejercicio9

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

for fila in tablero:
    print(fila)

turno = "X"
for jugada in range(9):  
    print("Turno de", turno)
    fila = int(input("Ingrese la fila (0-2): "))
    col = int(input("Ingrese la columna (0-2): "))

    if tablero[fila][col] == "-":
        tablero[fila][col] = turno
    else:
        print("Casilla ocupada, perdiste tu turno")

    
    for fila_tablero in tablero:
        print(fila_tablero)

   
    if turno == "X":
        turno = "O"
    else:
        turno = "X"

#Ejercicio10

ventas = [
    [10, 12, 8, 15, 9, 11, 14],
    [5, 7, 6, 8, 10, 9, 12],
    [20, 18, 22, 25, 19, 24, 21],
    [7, 6, 9, 5, 8, 7, 10]
]

print("Total vendido por cada producto:")
for i in range(len(ventas)):
    total_prod = sum(ventas[i])
    print(f"Producto {i+1}: {total_prod}")

totales_dia = []
for j in range(7):
    suma = 0
    for i in range(4):
        suma += ventas[i][j]
    totales_dia.append(suma)

mayor_dia = max(totales_dia)
indice_dia = totales_dia.index(mayor_dia)
print("\nDía con mayores ventas totales:", indice_dia+1, "con", mayor_dia, "ventas")

totales_productos = [sum(fila) for fila in ventas]
mayor_producto = max(totales_productos)
indice_producto = totales_productos.index(mayor_producto)
print("Producto más vendido en la semana: Producto", indice_producto+1, "con", mayor_producto, "ventas")
