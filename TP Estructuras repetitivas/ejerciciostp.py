#Ejercicio1
for i in range(101):
    print(i)

#Ejercicio2
num = int(input("Ingrese un número entero: "))
n = abs(num)
if n == 0:
    digitos = 1    
else:
    digitos = 0
    while n > 0:
        n = n // 10
        digitos += 1
print(f"Tu número tiene {digitos} dígitos")

#Ejercicio3
num1 = int(input("Ingrese el primer número entero: ")) 
num2 = int(input("Ingrese el segundo número entero: "))
suma = 0
if num1 == num2:
    print("Los números son iguales")
else:
    if num1 > num2:
        mayor = num1
        menor = num2    
    else:
        mayor = num2
        menor = num1
    for menor in range(menor + 1, mayor ):
        suma += menor
    print(f"La suma de los números enteros entre esos dos numeros da como resultado {suma}")  

#Ejercicio4
numero = int(input("Ingrese un numero entero: "))
suma = 0
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro numero entero: "))
print(f"La suma de los números ingresados da como resultado {suma}")    

#Ejercicio5
import random
numerorandom = random.randint(0,9)
adiv = int(input("Adivina el número entre el 0 y el 9: "))
cont = 1
if adiv == numerorandom:
    print("Excelente, adivinaste el número en el primer intento")
else:
    while adiv != numerorandom:
        adiv = int(input("Incorrecto, volve a intentar con otro número: "))
        cont += 1
    print(f"Muy bien, adivinaste el número en {cont} intentos!") 
 
#Ejercicio6
for x in range(100, -1, -2):
    print(x)

#Ejercicio7
rango = int(input("Ingrese un número entero: "))
suma = 0
for rango in range(0, rango + 1):
    suma += rango
print(f"La suma de todos los números enteros entre 0 y {rango} es {suma}")    

#Ejercicio8
positivo = 0
negativo = 0
par = 0
impar = 0
for i in range(1, 101):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    if num >= 0:
        positivo += 1
    else:
        negativo += 1            
print(f"Ingresaste {par} números pares, {impar} impares, {positivo} positivos y {negativo} negativos")        

#Ejercicio9
suma = 0
for y in range(1,11):
    y = int(input("Ingrese un número entero: "))
    suma += y
print("El promedio de esos valores es: ", suma / 10)

#Ejercicio10
numero = int(input("Ingresá un número: "))
invertido = 0

while numero > 0:
    digito = numero % 10         
    invertido = invertido * 10 + digito
    numero = numero // 10        

print("El número invertido es:", invertido)

