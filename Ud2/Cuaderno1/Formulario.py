

##- **Ejercicio 3:** Crear un formulario que valide la entrada de datos del usuario. Si la entrada es incorrecta, muestra un mensaje de error.
##Crea un formulario con campos para el nombre y el correo electrónico. 
##Validemos que el nombre no esté vacío y que el correo electrónico contenga un @. Si la entrada no es válida, muestra un mensaje de error.
##Puedes emplear `messagebox.showerror("Tu mensaje de error")`. No olvides importar el componente: `from tkinter import messagebox`.
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Botó y tres colores")
ventana.geometry("400x300")

etiquetaNombre = tk.Label(ventana, text="Introduce tu nombre:")
etiquetaNombre.pack()
entradaNombre = tk.Entry(ventana)
entradaNombre.pack()
etiquetaCo = tk.Label(ventana, text="Introduce tu nombre email:")
etiquetaCo.pack()
entradaCo = tk.Entry(ventana)
entradaCo.pack()

def validar():
    nombre = entradaNombre.get()
    correo = entradaCo.get()
   
    if len(nombre)==0:
      return  messagebox.showerror(message='Nombre vacio',title='Error')
    
    for i in correo:
          if i == '@':
             etiquetaVerificado = tk.Label(ventana, text="Todo bien")
             etiquetaVerificado.pack()
             return "todo bien"
          
    return  messagebox.showerror(message='Falta un @ en el email',title='Error')
       

boton = tk.Button(ventana, text="Haz clic aquí", command=validar)
boton.pack()
ventana.mainloop()

