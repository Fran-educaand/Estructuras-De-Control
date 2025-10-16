#- Ejercicio 5.1: Crea un programa que pida al usuario su nombre y su edad, los guarde en variables y luego imprima un mensaje que diga "Hola, [nombre]. Tienes [edad] años". Escribe un comentario de una sola línea que describa el propósito de tu código.

nombre = input("¿Cuál es tu nombre?: ")

edad = input("¿Cuántos años tienes?: ")

print("Hola, " + nombre + ". Tienes " + edad + " años.")

#Mi código le pide al usuario su nombre y su edad, y tras esto se imprime un mensaje con la información


#- Ejercicio 5.2: Crea tres variables: una con un valor booleano, otra con un número y otra con una cadena de texto. Usa print() para mostrar los tres valores en una sola línea, separados por un guion. Escribe un comentario de varias líneas en el que expliques qué hace el código.

booleano = True
numero = 10
cadena = "buenas"
print(booleano, numero, cadena, sep=" - ")
#Este código crea tres variables de cada tipo (booleano, número y cadena de texto ) y después muestra por pantalla los valores de las variables separados por un guion.

#- Ejercicio 5.3: Realiza una operación matemática con variables que hayas asignado anteriormente y usa print() para mostrar el resultado de la operación. Comenta temporalmente una línea de código que imprima un valor para evitar que se ejecute.
resultado = numero + 5
print(resultado)    
# print(cadena)  # Esta línea está comentada para evitar que se ejecute.
#El código realiza una operación matemática sumando 5 al valor de la variable "numero" y lo muestra por pantalla