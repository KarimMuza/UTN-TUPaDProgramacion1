#Ejercicio N1
print("Hola mundo!")

#Ejercicio N2
name = input("¿Cómo es tu nombre?" )
print(f"Hola {name}!")

#Ejercicio N3
nombre = input("¿Cuál es tu nombre?" )
apellido = input("¿?Cuál es tu apellido?" )
edad = int(input("¿Cuántos años tenes?" ))
residencia = input("¿Cúal es tu lugar de residencia? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")   

#Ejercicio N4
radio = float(input("¿Cuál es el radio del circulo? "))
pi = 3.14
area = pi * radio**2
perimetro = 2 * pi * radio
print(f"área = {area}")
print(f"perimetro = {perimetro}")

#Ejercicio N5
segundos = int(input("Ingrese la cantidad de segundos "))
horas = (segundos // 60) // 60
print(f"Esa cantidad de segundos equivale a {horas} hora/s ")

#Ejercicio N6
num = int(input("Ingrese un numero"))
for i in range (1, 10): 
    print(f"{num} x {i} = {num * i}")
    
#Ejercicio N7
num1 = int(input("Ingrese un número entero distinto de 0 "))
num2 = int(input("Ingrese otro número entero distinto de 0 "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} - {num2} = {num1 - num2}")

#Ejercicio N8
altura = float(input("¿Cuál es tu altura en metros?"))   
peso = float(input("¿Cuál es tu peso en kg?")) 
imc = peso / (altura**2)
print(f"Tu índice de masa corporal es {imc}")

#Ejercicio N9
celsius = float(input("Ingrese una temperatura en grados celsius "))
fahrenheit = (9/5) * celsius + 32
print(f"El equivalente en grados fahrenheit es: {fahrenheit}")