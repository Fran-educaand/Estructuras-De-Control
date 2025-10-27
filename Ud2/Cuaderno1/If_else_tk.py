## 1.9 Ejercicios if-elif-else:
##- **Ejercicio 1:** Crear una ventana que tenga un botón. Al presionar el botón, se cambia el color de fondo de la ventana. 
# Utiliza tres colores diferentes: red, blue y green. Cuando se presiona el botón, cambia el color de fondo entre estos colores de forma cíclica.
# Puedes obtener el color de fondo de la ventana con `ventana.cget("bg")` y establecerlo con `ventana.config(br="mi_color")`.
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Botó y tres colores")
ventana.geometry("400x300")


def cambiarColor ():

   

    if  ventana.cget("bg") == "green":
        ventana.config(bg="red")
        boton.config(text="Ahora soy rojo")
    elif ventana.cget("bg") == "red":
         ventana.config(bg="blue")
         boton.config(text="Ahora soy azul")
    else:
         ventana.config(bg="green")
         boton.config(text="Ahora soy verde")


boton = tk.Button(ventana, text="Haz clic aquí", command=cambiarColor)
ventana.mainloop()




##- **Ejercicio 2:** Crear una calculadora básica empleando una interfaz con botones para los números (0-9), las operaciones (+, -, *, /),
#  y un botón de igual (=) para calcular el resultado. Conforme se van presionando botones, 
# vamos escribiendo una expresión en un widget de tipo Entry (capturamos lo que había, lo borramos 
# y volvemos a escribir la expresión añadiendo lo nuevo). No obstante, si el botón presionado es `=` entonces habrá que evaluar la expresión 
# del Entry (`eval(entry.get())`... que podría arrojar excepciones), después borramos lo escrito y escribimos el resultado 
# (o un mensaje de error si se produjo). Opcionalmente, podríamos desplegar los botones en el Frame empleando una lista de tuplas (con todos los botones)
#  y recorriéndola con un bucle.



 

##- **Ejercicio 3:** Crear un formulario que valide la entrada de datos del usuario. Si la entrada es incorrecta, muestra un mensaje de error.
#  Crea un formulario con campos para el nombre y el correo electrónico. Validemos que el nombre no esté vacío y que el correo electrónico contenga un @.
#  Si la entrada no es válida, muestra un mensaje de error. Puedes emplear `messagebox.showerror("Tu mensaje de error")`. No olvides importar el
#  componente: `from tkinter import messagebox`.
