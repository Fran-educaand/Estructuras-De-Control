
### **Ejercicio 2.4. Barra deslizante (Scale) para el ajuste del tamaño de la fuente**

##* Crea una interfaz donde el usuario puede ajustar el tamaño de la fuente de un `Label` mediante un `Scale` (barra deslizante). 
##Añade un botón que permita restablecer el tamaño de la fuente a su valor predeterminado.

import tkinter as tk

def cambiarTamaño(valor):
   
   fuente = ("Arial",valor)
   label.config(font=fuente)



root = tk.Tk()
root.title("Ejemplo de Scale")

# Crear un Scale con un rango de 0 a 100 y orientado horizontalmente
scale = tk.Scale(root, from_=0, to=100, orient="vertical",command=cambiarTamaño)
scale.pack(pady=20)

label = tk.Label(root,text="Buenos dias",font=0 )
label.pack()

boton=tk.Button(root,text="Restablecer",command=lambda: label.config(font=0))
boton.pack()

root.mainloop()