#Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

#Ejercicio2

nota = int(input("Ingrese su nota:"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio3
num = int(input("Ingrese un número par: "))
if (num % 2) == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño")
elif (edad >= 12) and edad < 18:
    print("Adolescente")
elif (edad >= 18) and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto")    

#Ejercicio5
contraseña = input("Ingrese una contraseña: ")
if (len(contraseña) >= 8 ) and (len(contraseña) <= 14 ):
    print("Ha ingresado una constraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
     
#Ejercicio6
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)
from statistics import mode, median, mean
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
if (media > mediana) and (mediana > moda):
    print("Sesgo positivo o a la derecha")
elif (media < mediana) and (mediana < moda):
    print("Sesgo negativo o a la iquierda")
elif (media == mediana == moda):
    print("Sin sesgo")    
else:
    print("No definido")

#Ejercicio7
string = input("Escriba una frase o palabra: ")
comprobacion = [string.endswith(("a","e","i","o","u","A","E","I","O","U"))]
if comprobacion:
    print(string,"!")
else:
    print(string)

#Ejercicio8
nombre = input("Ingrese su nombre: ")
opcion = int(input("""1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
Ingrese 1, 2, o 3, según la opción que desee: """))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2: 
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title()) 

#Ejercicio9
magnitud = int(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif (magnitud >= 3) and (magnitud < 4):
    print("Leve (ligeramente perceptible).")
elif (magnitud >= 4) and (magnitud < 5):
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif (magnitud >= 5) and (magnitud < 6):
    print("Fuerte (puede causar daños en estructuras débiles).")
elif (magnitud >= 6) and (magnitud < 7):
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")

#Ejercicio10

hemisferio = input("Ingrese el hemisferio (N para norte, S para sur): ")
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if (hemisferio == "N") or (hemisferio == "n") :
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"

elif (hemisferio == "S") or (hemisferio == "s"):
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print(f"La estación es: {estacion}")

