# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.



for x in range (0,101):
    print(x)



# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero=(int(input("Ingrese un numero entero: ")))

digitos = len(str(numero))

print (f"El numero contiene {digitos} digitos")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero entero: "))

suma = 0
num += 1
for x in range(num,num2):
    contador = x
    suma += contador

print (f"la suma total de todos los numeros es {suma} ")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

x = 1
acumulador = 0
while x != 0:
    x=int(input("Ingrese un numero entero: "))
    acumulador += x
print(acumulador)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

intento = 0
while True:
    num=(int(input("Ingrese un numero entre el 0 y 9: ")))
    import random
    numero_random=random.randrange(0,9)
    if num != numero_random:
        print(f"el numero random fue {numero_random}")
        intento += 1
    else:
        print("¡¡¡CORRECTO GANASTE!!!")
        break
print(f"intentos necesarios para ganar {intento}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for x in range (100,-1,-2):
    print(x)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero entero: "))

sumatoria = 0
for x in range (0,num+1):
    sumatoria += x

print(f"la sumatoria comprendida es {sumatoria}")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
positivos = 0
negativos = 0
pares = 0
impares = 0
for x in range (1,101,1):
    num=int(input("ingrese numeros enteros: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1
print(f"cantidad de numeros pares: {pares}")
print(f"cantidad de numeros impares: {impares}")
print(f"cantidad de numeros positivos: {positivos}")
print(f"cantidad de numeros negativos: {negativos}")


    # 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
    # media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

sumatoria = 0
for x in range (0,100):
    num = int(input("Ingrese numeros enteros: "))
    sumatoria += num
    print(x)
promedio = sumatoria / 4

print(f"El promedio es {promedio}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.


n = int(input("Ingresar un numero: "))

inv = 0

while n > 0:
    digito = n % 10
    inv = inv * 10  + digito
    n //= 10
print(f"el numero invertido es {inv}")