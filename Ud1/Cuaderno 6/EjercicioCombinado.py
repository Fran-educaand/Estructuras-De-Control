## 6.10 Ejercicios combinados

##- **Ejercicio 13:** Escribe un programa que pida una lista de números separados por comas y luego determine cuál es el mayor número par de la lista. Si no hay ningún número par, 
# debe indicar que no existe ninguno.
try:
    lista = input('Escribe numeros por coma: ')

    listaInt = [int(n) for n in lista.split(",")]
    num = 0
    for n in listaInt:
     if  n%2 ==0 and n > num:
         num = n
    print (num)
except: print("Error")


##- **Ejercicio 14:** Pide al usuario que introduzca una lista de números y, utilizando un bucle for y condicionales, imprima los números negativos y positivos por separado.

try:
    lista = input('Escribe numeros por coma: ')

    listaInt = [int(n) for n in lista.split(",")]
    listaPos = []
    listaNeg =[]

    for n in listaInt:
     if n >0:
           listaPos.append(n)
     else: listaNeg.append(n)
    print (listaPos)
    print(" ")
    print (listaNeg)
    print(" ")
except: print("Error")
##- **Ejercicio 15:** Imprime los números impares del 1 al 200 utilizando un bucle for con un rango que tenga paso de 3.
try:
    for num in range (0,199,3):
        if num %2 != 0:
         print (num)
        else:pass

    print(" ")
except: print("Error")

##- **Ejercicio 16:** Escribe un programa que imprima todos los múltiplos de 3 del 1 al 100, pero solo hasta el primer múltiplo mayor que 50.
try: 
     mul = 0
     for num in range (0,99):
          if num <= 50 :
            if num % 3 == 0:
                print(num)
            else:pass
          else:break
except:
    print("error")


##- **Ejercicio 17:** Crea una función que reciba el nombre de un mes (como "enero", "febrero", etc.) y devuelva la estación del año correspondiente usando match-case.



try: 
    def estacion ( mes):

        match mes:
            case "Enero","Febrero","Marzo":
                return"Invierno"
            case "Abril","Mayo","Junio":
                return"Primavera"
            case "Julio","Agosto","Septiembre":
                return"Verano"
            case "Octube","Noviembre","Diciembre":
                return"Invierno"
except:
    print("error")

##- **Ejercicio 18:** Escribe un programa que reciba una cadena de texto representando un día de la semana y te diga si es fin de semana o día laborable utilizando match-case.

    

try: 
    dia = input("Escribe un dia: ")

    def estacion (dia):

        match dia:
            case "Lunes","Martes","Miercoles","Jueves","Viernes":
                return"Dia Laboral"
            case "Sabado","Domingo":
                return"Fin de semana"
except:
    print("error")

##- **Ejercicio 19:** Escribe un programa que busque un número en una lista utilizando un bucle for. Si lo encuentra, imprime "Número encontrado", y si no, imprime "Número no encontrado"
# , utilizando else en el bucle.

try: 
    listamia = [1,2,3,4,5,6,7,8]

    nencontrado = 8

    for n in listamia:
        if n == nencontrado:
            print ("numero encontrado")
            break
        else: print:('buscando')
except:
    print("error")

##- **Ejercicio 20:** Implementa un programa que recorra una lista de nombres y determine si algún nombre tiene más de 5 caracteres. Si se encuentra uno, el bucle debe finalizar con break,
#  y si no se encuentra ninguno, imprime "Ningún nombre largo" al final.

caracteres = ["Fran","Angel","Antonio"]

for a in caracteres:
    if len(a) >5:
        print("Encontrado")
        break
    else:"Ningun nombre largo por ahora "

##- **Ejercicio 21:** Crea una función que reciba un número como argumento y si el número es negativo, lance una excepción de tipo ValueError con un mensaje como "Error: número negativo".

lista = int(input('Escribe numero: '))
if num < 0:
 raise ValueError("numero negativo")

##❗**Ejercicio 22:** Modifica la solución anterior para que el usuario pueda intentar introducir un nuevo número si se lanza una excepción. Tendrá un número de intentos infinito.

intentos = 3
while intentos > 0:
    lista = int(input('Escribe numero: '))
    if num < 0:
        intentos = intentos -1
        raise ValueError("numero negativo")
    else: 
        intentos = intentos -1
        print(f"Tequedan: {intentos}")