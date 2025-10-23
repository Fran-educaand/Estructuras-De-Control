
## 6.11 Ejercicios avanzados
##**Ejercicio 23:** Escribe un programa que pida al usuario una lista de números y calcule su media, pero primero debe verificar que todos los números son positivos. 
# Si algún número es negativo, lanza una excepción personalizada.
class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
    pass



lista = input('Escribe numeros por coma: ')
listaInt = [int(n) for n in lista.split(",")]

for n in listaInt:
    if n < 0:
        raise MiExcepcionPersonalizada ("Numero negativo")
    else:pass  

media = sum(listaInt) / len(listaInt)


##- ❗**Ejercicio 24:** Crea una función que reciba una cadena de texto e imprima los caracteres en orden inverso (emplea `cadena[::-1]`). 
# Si la cadena contiene más de 10 caracteres (emplea la función `len`), eleva una excepción indicando que es demasiado larga.

lista = input('Escribe algo: ')
if len(lista)>10:
    raise MiExcepcionPersonalizada ("MENSAJE DEMASIADO LARGO")
else:print(lista[::-1])


## **Ejercicio 25:** Crea un programa que pida al usuario el nombre de un día de la semana y un número del 1 al 7. Si el número está dentro del rango, 
# imprimirá el día correspondiente de la semana usando match-case. Si el número está fuera del rango, imprimirá "Número inválido".

try: 
    num = input('Escribe un numero del 1 al 7: ')

    match num:
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miercoles") 
        case 4:
            print("Jueves")
        case 5:
            print("Viernes") 
        case 6:
            print("Sabado")
        case 7:
            print("Domingo")
        case _:
            raise ValueError ("No esta en tre el 1 y el 7 el numero introducido")
except:   print("error")



# ❗**Ejercicio 26:** Crea un programa que pida una lista de cadenas de texto. Si alguna de las cadenas tiene menos de 3 caracteres, 
# lanzará una excepción personalizada (por ejemplo: `class CadenasDemasiadoCortasError(Exception):` que no hará nada `pass`). Si la cadena tiene más de 3 caracteres, la imprimirá,
#  Recorrerá todas las cadenas, debe continuar incluso si se lanza una excepción para algunas cadenas.

try : 

    lista_cadena = input("Escribe una lista de cadenas: ").split(" ")

    for i in lista_cadena:
        if len(i) < 3:
           try:
             raise MiExcepcionPersonalizada("¡Algo salió mal!")
           except MiExcepcionPersonalizada as e:
                print(e)
        else:print(i)
      

except :  print ("Error")



##❗**Ejercicio 27:** Implementa una función recursiva que calcule el factorial de un número. 
# Si el número es negativo, lanza una excepción (como `class FactorialNegativoError(Exception):`) indicando que no se puede calcular el factorial de números negativos.
class FactorialNegativoError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

    pass
def funRecursiva(n):
    if(n < 0):
        return FactorialNegativoError("No puede ser negativo")
    else: pass




##- **Ejercicio 28:** Crea una función que reciba una lista de números y devuelva el mayor número que aparece en la lista. Si la lista está vacía, lanzará una excepción.


def mayor(lista_num):

    if len(lista_num)<1:
        raise  MiExcepcionPersonalizada("No hay nada")
    else:
        num = 0
        for i in lista_num:
            if (i > num):
                num = i
          
        print (num)   


## ❗**Ejercicio 29:** Crea una clase Producto que tenga un nombre y un precio.
#  Luego, implementa una clase Carrito que permita agregar productos al carrito, calcular el total, y eliminar productos. Si, al crear un producto, su precio es negativo, lanzará una excepción.
class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        if(precio <0):
            raise MiExcepcionPersonalizada("Precio es 0")
        else:
            self.precio = precio

    def getPrecio(self):
        return self.precio
    
class Carrito:
    def __init__(self):
        self.listaProducto =[]

    def añadirProducto(self,producto):
        self.listaProducto.append(producto)
    
    def calcPrecio(self):
        num = 0
        for producto in self.listaProducto:
            num += producto.getPrecio()
        return f"El precio total es : {num}"
    
    
    def quitarProducto(self,producto):
        self.listaProducto.remove(producto)
