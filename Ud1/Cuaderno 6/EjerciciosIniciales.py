## 6.9 Ejercicios iniciales
##- **Ejercicio 1:** Lee un número entero desde la entrada estándar y determina si es positivo, negativo o cero.

n1 = input("Escribe un numero: ")
if int(n1) > 0:
    print("Positivo")
elif int(n2)<0:
    print("Negativo")
elif int(n2) == 0:
    print ( "es cero")



##- **Ejercicio 2:** Escribe un programa que pida un número y determine si es divisible entre 3, 5, o ambos.

n2 = int(input("Escribe un numero: "))

if n2 % 3 == 0:
    print("Es divisible entre tres ")
elif n2 % 5 == 0:
    print("Es divisible entre 5 ")
elif n2 % 5 == 0 and n2 % 3 == 0:
    print ("Es divisble por ambos ")
else:
    print('No es divisible')



##- **Ejercicio 3:** Verifica si un número es par o impar usando un condicional ternario.


mensaje = "Es par" if n2 % 2 == 0 else "Es impar"
print(mensaje)  



##- **Ejercicio 4:** Determina si una persona es mayor de edad (18 años o más) con un condicional ternario.

edad = 20  # Ejemplo de edad
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)  # Salida: Mayor de edad



##- **Ejercicio 5:** Imprime los números del 1 al 10 utilizando un bucle for con un rango.

for i in range (11):
    print(i)
  
print(" ")
##- **Ejercicio 6:** Imprime todos los números del 1 al 50 que sean divisibles por 4 utilizando un bucle for con un rango.
for i in range (51):
   if i % 4 == 0:
        print(i)
   else: pass
       

##- **Ejercicio 7:** Escribe un programa que pida al usuario un número positivo y luego calcule la suma de todos los números del 1 hasta ese número utilizando un bucle while.

n3 = int(input("Escribe un numero: "))



##- **Ejercicio 8:** Implementa un programa que pida una contraseña y se repita (con un bucle while) hasta que el usuario introduzca la contraseña correcta.
micontraseña="h"
contraseña = " "
while(micontraseña!=contraseña):
    contraseña = input("Introduce una contraseña: ")
print("Introducida con exito")

##- **Ejercicio 9:** Crea un bucle for que imprima números del 1 al 10, pero que detenga el bucle al llegar al número 6 utilizando break.

for i in range (11):
    if i != 6:
        print(i)
    else: break
print (' ')

##- **Ejercicio 11:** Escribe un programa que imprima los números del 1 al 10, pero que omita el número 5 utilizando continue.

for i in range (11):
    if i != 5:
        print(i)
    else: continue


##- **Ejercicio 12:** Crea una función que reciba un número y eleve una excepción si el número es negativo, utilizando raise.

def negaivo (num):
    if num < 0:
        raise "No puede ser negativo"
    else: print ('positivo')
    return num