#* ❗**Ejercicio 34:** Crea un programa que pida al usuario unos números separados por comas. Luego, convierte esa lista en una lista de enteros, calcula la suma y el promedio, y
#verifica si el promedio está en la lista. Puedes obtener una lista a partir de los números separados por coma con la función `split(',')` 
#aplicada sobre la cadena de caracteres. Después puedes convertir cada elemento de la lista en un entero, bien recorriendo la lista elemento a elemento,
#bien usando una función `map(int, lista)`. Puedes sumar los elementos de la lista con la función `sum(lista)`. Cuida de calcular el promedio solo si la longitud de la lista es mayor que cero.

lista = []

while True:

    cadena = input("Escribe números separados por coma: ")
    for a in range (len(cadena)):
        if cadena[a]==" " or cadena[-1] == ",":
            print("No incluyas ni espacios ni comas al final ")
           
        else:
            lista = [int(num)for num in cadena.split(",")]       
    break
print(lista)
suma = sum(lista)
longitud = len(lista)
if longitud > 0:
    promedio = sum(lista) / len(lista)
    print (promedio)
else:
    print ("No se puede calcular el promedio")
