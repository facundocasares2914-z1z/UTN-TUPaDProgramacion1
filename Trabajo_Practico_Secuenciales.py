# ## 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("hola mundo")

# ## 2)  Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# ##el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# ##por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# ##realizar la impresión por pantalla. 

nombre = input("Escriba su nombre: ")
print (f"hola {nombre}! ")

## 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
## imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
## “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
## años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# ## la impresión por pantalla.

nombre = input ("Escriba su nombre: ")
apellido = input ("Escriba su apellido: ")
edad = input ("Ingrese su edad: ")
lugar = input ("Ingrese su Lugar de residencia: ")
print (f"Soy {nombre} {apellido}, y tengo {edad} años y vivo en {lugar}.")


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingrese el radio del circulo: "))

area = 3.14159 * radio ** 2
perímetro = 2 * 3.14159 * radio
print (f"El area del circulo es {area} y su perímetro es {perímetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = float(input("Escriba una cantidad de segundos: "))

hora = segundos // 36000

print (f"la cantidad de horas es {hora}")

# 6)Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = int(input("Ingrese un numero: "))

print ("la tabla de multiplar es:")
print (numero * 1)
print (numero * 2)
print (numero * 3)
print (numero * 4)
print (numero * 5)
print (numero * 6)
print (numero * 7)
print (numero * 8)
print (numero * 9)
print (numero * 10)

# 7)Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese un distinto a 0 : "))
num2 = int(input("Ingrese otro numero distinto a 0: "))

suma = num1 + num2
divi = num1 / num2
multi = num1 * num2
resta = num1 - num2
print (f"la resta es {resta}")
print (f"la suma es {suma}")
print(f"la multiplicacion es {multi}")
print(f"la division es {divi}")

#8)Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo: 𝐼𝑀𝐶 = peso en kg / (altura en m  ** 2)


altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / (altura **2 )

print(f"Su indice de masa corporal es de: {imc}")

# 9)Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia

celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = 9/5 * celsius + 32
print(f"Su equivalente en grados Fahrenheit es: {fahrenheit}")

# 10)  Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese el ultimo numero: "))
total = num1 + num2 + num3
promedio = total / 3

print(f"el promedio de las notas es: {promedio:.2f}")
