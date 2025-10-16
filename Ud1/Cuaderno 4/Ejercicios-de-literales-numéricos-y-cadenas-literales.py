#- Ejercicio 1: Escribe tres expresiones numéricas: una que utilice enteros, otra con números decimales, y otra con una mezcla de ambos. Muestra los resultados de estas expresiones.
entero = 5 + 3

decimal = 4.5 * 2.0

mixto = 7 -3.1

print(entero, decimal, mixto, sep=" - ")


#- Ejercicio 2: Crea cadenas utilizando comillas simples, dobles y triples. Muestra cómo funcionan y cuándo es conveniente usarlas. Pregunta: ¿Qué pasa si usas comillas dobles dentro de comillas dobles o comillas simples dentro de comillas simples?

simple = 'Hola'

doble = "Mundo"

triple = '''Cadena triple'''

print(simple, doble, triple, sep=" - ")

#No funcionan las comillas par que aparezcan sería usando lo siguiente : \" o \'


#- Ejercicio 3: Muestra cómo insertar caracteres especiales, como el salto de línea (\n), tabulación (\t), y comillas dentro de cadenas. Pregunta: ¿Qué efecto tiene cada uno de los caracteres especiales?

cadena= "Primera línea\nSegunda línea\n\tCon tabulación\n\"Comillas dentro de la cadena\""
print(cadena)

# \n crea un salto de línea, \t añade una tabulación, y \" permite incluir comillas dentro de la cadena .


#- Ejercicio 4: Demuestra cómo insertar valores en cadenas utilizando f-strings, .format(), y el operador %. Pregunta: ¿Cuál de estos métodos te parece más sencillo de usar? ¿Por qué?
hola = "Hola"
f= print(f"Usando {entero} asi")

format= print("Usando {} asi".format(decimal))

porcentaje= print ("Usando %s asi" % hola)



#- Ejercicio 5: Emplea la alineación de texto en cadenas para alinear valores a la izquierda, derecha o centrados. Utiliza .format() o f-strings. Pregunta: ¿Cómo puedes cambiar la alineación de las columnas usando los métodos vistos?

alineacion_izquierda = f"{'Izquierda':<15}"

alineacion_derecha = f"{'Derecha':>15}"

alineacion_centrada = f"{'Centrada':^15}"

print(alineacion_izquierda)
print(alineacion_derecha)
print(alineacion_centrada)

#- Ejercicio 6: Realiza ejemplos de formatos de texto con números decimales, enteros, y porcentajes. Usa f-strings o .format(). Pregunta: ¿Cómo puedes redondear el precio a un número específico de decimales? ¿Cómo puedes mostrar un número como porcentaje?

precio = 49.98765
print(f"Precio con 2 decimales: {precio:.2f}")
print("Precio con 2 decimales: {:.2f}".format(precio))
porcentaje = 0.2567
print(f"Porcentaje: {porcentaje:.2%}")
print("Porcentaje: {:.2%}".format(porcentaje))
