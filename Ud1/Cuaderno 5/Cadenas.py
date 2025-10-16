
#--------------------------------------------------------------Concatenacion--------------------------------------------------------------#

#* **Ejercicio 16:** Crea dos cadenas, `cadena1` y `cadena2`, y concaténalas para formar una nueva cadena.

cadena1 = "Hola, "
cadena2 = "¿Cómo estás?"
cadena_concatenada = cadena1 + cadena2


#* **Ejercicio 17:** Concatenar varias cadenas usando un bucle for y el operador `+`. Prueba también la función `join()`.

cadena3 = "Python esta guay"
cadena4 = "y es divertido"

cadena5 = cadena3.join([" ",cadena4])
print(cadena5)

for palabra in range(1):
    cadena3 += " " + cadena4
    
print(cadena3)

#--------------------------------------------------------------Repeticion---------------------------------------------------------------#

#* **Ejercicio 18:** Usa el operador de repetición `*` para repetir una cadena un número determinado de veces.
cadena = "Hola "
cadena_repetida = cadena * 3
print(cadena_repetida)

#--------------------------------------------------------------Comparacion--------------------------------------------------------------#

#* **Ejercicio 19:** Compara dos cadenas para ver si son iguales (usa el operador `==`) y luego compara si una cadena es mayor o menor alfabéticamente.
cadena6 = "manzana"
cadena7 = "naranja"
print(f"cadena_a == cadena_b: {cadena6 == cadena7}")
print(f"cadena_a < cadena_b: {cadena6 < cadena7}")


#--------------------------------------------------------------Longitud------------------------------------------------------------------#

#* **Ejercicio 20:** Usa la función `len()` para obtener la longitud de una cadena.
cadena8 = "Hola, ¿cómo estás?"
longitud = len(cadena8)
print(f"La longitud de la cadena es: {longitud}")



#* **Ejercicio 21:** Crea una función que calcule la longitud de una cadena sin usar `len()`.
def longitud_cadena(cadena):
    contador = 0
    for _ in cadena:
        contador += 1
    print(f"La longitud de la cadena sin len es: {contador}")
    return contador
longitud_cadena(cadena8)


#-------------------------------------------------------Indexacion y Acceso a Caracteres-----------------------------------------------------#
#* **Ejercicio 22:** Accede al primer, último y un elemento intermedio de una cadena utilizando índices.
cadena9 = "Python"
print(f"Primer caracter: {cadena9[0]}")
print(f"Ultimo caracter: {cadena9[-1]}")
print(f"Caracter intermedio: {cadena9[len(cadena9)//2]}")  # Caracter en la posición media

#* **Ejercicio 23:** Intenta acceder a un índice fuera del rango y maneja el error con un `try`-`except`. La excepción a manejar sería `IndexError`.
try:
    print(cadena9[10])  # Intento de acceso a un índice fuera del rango
except IndexError as e:
    print(f"Error: {e}. Índice fuera del rango.")

#--------------------------------------------------------------Slicing-------------------------------------------------------------------#

#* **Ejercicio 24:** Utiliza slicing para obtener una subcadena de una cadena original. Intenta obtener los primeros 3 y últimos 3 caracteres de una cadena.
cadena10 = "Aprendiendo Python"
print(f"Primeros 3 caracteres: {cadena10[:3]}")
print(f"Últimos 3 caracteres: {cadena10[-3:]}")

#* **Ejercicio 25:** Realiza un slicing inverso de una cadena (es decir, invertir la cadena).
cadena_invertida = cadena10[::-1]
print(f"Cadena invertida: {cadena_invertida}")

#### 15. **Iteración sobre cadenas**

#* **Ejercicio 26:** Usa un bucle `for` para imprimir cada carácter de una cadena por separado.

for num in range (len(cadena10)):
    print (cadena10[num])


#* **Ejercicio 27:** Escribe una función que cuente cuántas veces aparece un carácter específico en una cadena.

def contar_caracter(cadena, caracter):
    contador = 0
    for num in range (len(cadena)):
        if cadena[num] == caracter:
            contador +=1
        else:
            pass
    return print (contador)

contar_caracter(cadena10,"e")
