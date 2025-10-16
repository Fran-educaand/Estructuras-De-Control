

##------------------------------------------------------------OPERADORES ARITMETICOS------------------------------------------------------------------##



#* **Ejercicio 1:** Realiza una operación de suma, resta, multiplicación, división y módulo con los números 12 y 5. Muestra el resultado de cada operación.

suma = 12 + 5
resta = 12 - 5
multiplicacion = 12 * 5
division = 12 / 5
modulo = 12 % 5
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}, Módulo: {modulo}")

# **Ejercicio 2:** Calcula la raíz cuadrada de 144 usando los operadores aritméticos y la función `**`.

raiz_cuadrada = 144 ** 0.5
print(f"La raíz cuadrada de 144 es: {raiz_cuadrada}")


#* **Ejercicio 3:** Usa la operación de división entera y el módulo para dividir 23 entre 5. ¿Cuál es el cociente y el resto?
cociente = 23 // 5
resto = 23 % 5
print(f"Cociente: {cociente}, Resto: {resto}")


##------------------------------------------------------------------ASIGNACION----------------------------------------------------------------------------##


#**Ejercicio 4:** Usa el operador `+=` para incrementar una variable en 5 y muestra el resultado.

x = 10
x += 5
print(f"El valor de x después de incrementar en 5 es: {x}")


#* **Ejercicio 5:** Usa los operadores de asignación `-=`, `*=`, `/=`, y `**=` con una variable `x` que inicia en 10. Muestra cómo cambia `x` después de cada operación.
x = 10
x -= 2
print(f"Después de x -= 2, x es: {x}")
x *= 3
print(f"Después de x *= 3, x es: {x}")
x /= 4
print(f"Después de x /= 4, x es: {x}")
x **= 2
print(f"Después de x **= 2, x es: {x}")


##------------------------------------------------------------------COMPARACION----------------------------------------------------------------------------##

#* **Ejercicio 6:** Compara dos números `a` y `b` (elige valores diferentes) usando los operadores `==`, `!=`, `>`, `<`, `>=`, `<=`. Muestra si cada comparación es `True` o `False`.

a = 8
b = 5
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")


#* **Ejercicio 7:** Compara una lista y una cadena (con los mismos caracteres ambas) para ver si son iguales utilizando el operador `==`. ¿Por qué el resultado es como es?

lista = [1, 2, 3]
cadena = "123"
print(f"Lista == Cadena: {lista == cadena}")  # Esto es False porque son tipos de datos diferentes.


#-----------------------------------------------------------------------LOGICOS----------------------------------------------------------------------------##

#* **Ejercicio 8:** Usa los operadores lógicos `and`, `or` y `not` para comprobar las condiciones en una variable booleana. Ejemplo: "Si una persona tiene 18 años o más, y si ha terminado la secundaria, puede inscribirse en el curso".

año = 20
secundaria_terminada = True
if año >= 18 and secundaria_terminada:
    print("Puede inscribirse en el curso.")
elif año < 18 or not secundaria_terminada:
    print("No puede inscribirse en el curso.")
else:
    print("...")


#-----------------------------------------------------------------------IDENTIDAD----------------------------------------------------------------------------##

#* **Ejercicio 9:** Crea dos listas con los mismos elementos y verifica si son la misma referencia de objeto usando `is` y `is not`. Explica el comportamiento.
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(f"lista1 is lista2: {lista1 is lista2}")  # Esto es False porque son objetos diferentes en memoria.
print(f"lista1 is not lista2: {lista1 is not lista2}")  # Esto es True porque son objetos diferentes en memoria.

#-------------------------------------------------------------------PERTENENCIA (IN , IN NOT)----------------------------------------------------------------------------##

#* **Ejercicio 10:** Crea una lista de números del 1 al 10 y verifica si el número 5 está dentro de esa lista usando el operador `in`.
#numeros = list(range(1, 11))
numeros = [1,2,3,4,5,6,7,8,9,10]
if 5 in numeros:
    print("El número 5 está en la lista.")  
elif 5 not in numeros:
    print("El número 5 no está en la lista.")

#* **Ejercicio 11:** Verifica si una cadena contiene una subcadena utilizando `in`. ¿Qué sucede si la subcadena no existe?
cadena = "Hola buenos dias"
subcadena = "buenos"
if subcadena in cadena:
    print(f"La subcadena '{subcadena}' está en la cadena.")
elif subcadena not in cadena:
    print(f"La subcadena '{subcadena}' no está en la cadena.")

#-----------------------------------------------------------------OPERADORES A NIVEL DE BITS----------------------------------------------------------------------------##

#* **Ejercicio 15:** Realiza la suma de 0.1 + 0.7 en Python y muestra el resultado. Explica por qué el resultado no es 0.8 exactamente.

resultado = 0.1 + 0.7
print(f"El resultado de 0.1 + 0.7 es: {resultado}")
# El resultado no es exactamente 0.8 debido a la representación interna de los números de punto flotante en la memoria del ordenador

