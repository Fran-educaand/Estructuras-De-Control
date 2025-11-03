### **Ejercicio 2.5. Formulario de registro con `Entry`, `Combobox` y `Checkbutton`**

##* Crea un formulario de registro que permita al usuario ingresar su nombre, elegir un país de un `ComboBox`, 
##y marcar una casilla de aceptación con un `Checkbutton`. Un botón debe verificar si todos los campos están completos y mostrar un mensaje de éxito o error.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Formulario ")
ventana.geometry("400x300")

def verifica(event):
    

etiquetaNombre = tk.Label(ventana, text="Introduce tu nombre:")
etiquetaNombre.pack()
entradaNombre = tk.Entry(ventana)
entradaNombre.pack()

opciones = ["España", "Etiopía", "Madagascar", "Perú"]
combo = ttk.Combobox(ventana, values=opciones)
combo.pack(pady=20)

var1=tk.IntVar()
check = ttk.Checkbutton(ventana,text='Aceptas cookies',variable=var1)
check.pack()

boton = ttk.Button(text='Verificar campos',command=)
ventana.mainloop()

