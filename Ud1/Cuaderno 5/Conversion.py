

#------------------------------------------------------------Conversiones Implicitas-----------------------------------------------------#

#Ejercicio 28:** Realiza una operación entre un número entero y un número decimal. Muestra el resultado y explica cómo Python maneja la conversión implícita.
entero = 5
flotante = 3.2
resultado = entero + flotante
# Python convierte automáticamente el entero a flotante para realizar la operación, resultando en un número

#--------------------------------------------------------------Conversiones Explicitas-----------------------------------------------------#

#* **Ejercicio 29:** Convierte un número flotante en un número entero utilizando `int()`. ¿Qué sucede con los decimales?

print(int(flotante))
#Python elimina los decimales

#* **Ejercicio 30:** Convierte una cadena que contiene un número a un número entero o flotante utilizando `int()` o `float()`. ¿Qué sucede si la cadena no es un número válido?
cadena_numero = "4.7"
print(float(cadena_numero))
#Si la cadena no es un número válido, Python lanzará un ValueError


#* **Ejercicio 31:** Realiza una conversión explícita entre tipos `int` o `float` y `str` y muestra los resultados.
num = 10
cadena = str(num)
print(cadena)

#--------------------------------------------------------------Conversiones entre estructuras de datos-----------------------------------------------------#

#* ❗**Ejercicio 32:** Convierte una lista de números en una cadena utilizando `join()`. Luego, convierte la cadena de nuevo en una lista de enteros.

#* ❗**Ejercicio 33:** Convierte un diccionario en una lista de claves y luego en una lista de valores. Puedes utilizar los métodos .keys() y .values(). Ambos métodos devuelven vistas del diccionario, que son iterables, y puedes convertirlos fácilmente en listas utilizando la función list().
