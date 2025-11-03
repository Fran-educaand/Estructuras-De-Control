### **Ejercicio 2.7. Juego de adivinanza de números con `Spinbox` y `Button`**

##* Crea un juego de adivinanza en el que el usuario debe adivinar un número entre 1 y 100. Utiliza un `Spinbox` para permitir al usuario seleccionar un número, 
##un `Button` para hacer la adivinanza y un `Label` para mostrar si la adivinanza fue correcta o no.

import tkinter as tk
import random

def verifica():
    if int(spinbox.get())== ran:
        label.configure(text="Acertaste")
    else:label.configure(text="Sigue buscando")


root = tk.Tk()

# Crear el SpinBox con un rango de 0 a 10
spinbox = tk.Spinbox(root, from_=1, to=100)
spinbox.pack()

label = tk.Label(root,text="¿Que número será?")
label.pack()
ran = random.randint(1,100)
print(ran)

boton=tk.Button(root,text="!LO TENGO¡",command=lambda:verifica())
boton.pack()


root.mainloop()