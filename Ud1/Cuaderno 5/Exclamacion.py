#* ❗**Ejercicio 32:** Convierte una lista de números en una cadena utilizando `join()`. Luego, convierte la cadena de nuevo en una lista de enteros.

lista = [2,2,2,2,2]
cadena = "".join([str(n)for n in lista])

print (cadena)

lista = [int (num) for num in cadena]

print (lista)




#* ❗**Ejercicio 33:** Convierte un diccionario en una lista de claves y luego en una lista de valores. Puedes utilizar los métodos .keys() y .values(). Ambos métodos devuelven vistas del diccionario, que son iterables, y puedes convertirlos fácilmente en listas utilizando la función list().






#* ❗**Ejercicio 34:** Crea un programa que pida al usuario unos números separados por comas. Luego, convierte esa lista en una lista de enteros, calcula la suma y el promedio, y
#verifica si el promedio está en la lista. Puedes obtener una lista a partir de los números separados por coma con la función `split(',')` 
#aplicada sobre la cadena de caracteres. Después puedes convertir cada elemento de la lista en un entero, bien recorriendo la lista elemento a elemento,
#bien usando una función `map(int, lista)`. Puedes sumar los elementos de la lista con la función `sum(lista)`. Cuida de calcular el promedio solo si la longitud de la lista es mayor que cero.

cadena = input("Escribe números separados por coma: ")
lista = [int(num)for num in cadena.split(",")]
print(lista)
suma = sum(lista)
longitud = len(lista)
if longitud > 0:
    promedio = sum(lista) / len(lista)
    print (promedio)
else:
    print ("No se puede calcular el promedio")

#* ❗**Ejercicio 35:** Usa una lista de cadenas que representen números flotantes, conviértelas a flotantes y muestra los resultados con 3 decimales.   

cadena2 = ["3.432323","5.632323","8.83232"]
cadenaNueva = [round(float(num),3) for num in cadena2]
print (cadenaNueva)
#cadenaNueva = [float(num2)for num2 in cadena2]
#print(cadenaNueva)

#for num in cadena2:
 #   cadenaNueva.append(round(float(num),3))
#print(cadenaNueva)
    