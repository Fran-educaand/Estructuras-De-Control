#- Ejercicio 11: Formatear la salida de una tabla. Solicita al usuario varias entradas para crear una tabla de datos. Por ejemplo, nombre, edad y ciudad, y luego alinea las columnas.

tabla = (f"{'Nombre':<15} {'Edad':<5} {'Ciudad':<15}\n")
tabla += (f"{'Ana':<15} {'28':<5} {'Madrid':<15}\n")

print(tabla)






#- Ejercicio 12: Cálculo de una media. Solicita al usuario una lista de números separados por comas, luego calcula y muestra la media de esos números. Emplea las funciones 'sum' y 'len' para calcular la media.
entrada = input("Introduce varios números separados por comas: ")
numeros = [int(num) for num in entrada.split(",")]
media = sum(numeros) / len(numeros)
print(f"La media de los números es: {media}")
