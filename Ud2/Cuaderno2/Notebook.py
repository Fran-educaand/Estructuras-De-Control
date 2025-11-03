### **Ejercicio 2.3. Aplicación de diseño de páginas con un Notebook**

##* Crea una aplicación con varias "páginas" utilizando el widget `Notebook`. 
##Cada página puede tener un botón que al ser presionado cambia el contenido de un `Label` que muestre información diferente en cada pestaña.
import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Notebook")
ventana.geometry("400x300")

notebook = ttk.Notebook(ventana)
notebook.pack(pady=20)

##Crear las páginas del Notebook (cada página es un Frame)
pagina1 = ttk.Frame(notebook)
pagina2 = ttk.Frame(notebook)

# Añadir las páginas al Notebook
notebook.add(pagina1, text="Pestaña 1")
notebook.add(pagina2, text="Pestaña 2")

# Añadir contenido a las páginas
label1 = ttk.Label(pagina1, text="Contenido de la Pestaña 1")
boton1 = ttk.Button(pagina1,text="Mostrar texto",command=lambda: label1.pack())
boton1.pack()

boton2 = ttk.Button(pagina2,text="Mostrar texto",command=lambda: label2.pack())
boton2.pack()
label2 = ttk.Label(pagina2, text="hola 2")


ventana.mainloop()