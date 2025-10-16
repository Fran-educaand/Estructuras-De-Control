#- Ejercicio 7: Solicita el nombre del usuario y muéstralo en pantalla.

nombre = input("¿Cuál es tu nombre?: ")
print(nombre)

#- Ejercicio 8: Solicita al usuario dos números, realiza operaciones matemáticas con ellos y muestra el resultado.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

print(f"Suma: {suma}, Resta: {resta}, Multiplicacion: {multiplicacion}")




#- Ejercicio 9: Solicita al usuario que introduzca varios números separados por comas, luego convierte esa entrada en una lista de números y muestra la suma de esos números (emplea la función 'sum').

entrada = input("Introduce varios números separados por comas: ")
print(entrada)
numeros = [int(num) for num in entrada.split(",")]
suma_numeros = sum(numeros)   
print(f"La suma de los números es: {suma_numeros}") 




#- Ejercicio 10: Solicita al usuario una frase y convierte esa frase en una lista de palabras. Luego, muestra la longitud de la lista y la palabra más larga. Emplea la función 'max(palabras, key=len)'.
frase = input("Introduce una frase: ")
palabras = frase.split()
print(palabras)
longitud_lista = len(palabras)
palabra_mas_larga = max(palabras, key=len)
print(f"La longitud de la lista es: {longitud_lista}")
print(f"La palabra más larga es: {palabra_mas_larga}")