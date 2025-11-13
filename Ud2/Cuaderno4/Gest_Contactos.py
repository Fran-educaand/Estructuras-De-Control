import tkinter as tk
from tkinter import messagebox


class Contacto:
   
   def __init__(self,nombre,telefono,email):
      self.nombre=nombre
      self.telefono=telefono
      self.email = email
    
   def __str__(self):
      return f"{self.nombre}, {self.telefono}, {self.email}"
      



ventana = tk.Tk()
ventana.title("Botó y tres colores")
ventana.geometry("400x300")

listbox = tk.Listbox(ventana, selectmode=tk.MULTIPLE, height=6, width=30)
listbox.pack(pady=20)

frame = tk.Frame(ventana)
frame.pack()

etiquetaNombre = tk.Label(frame, text="Introduce tu nombre:")
etiquetaNombre.pack()
entradaNombre = tk.Entry(frame)
entradaNombre.pack()
etiquetaTelefono = tk.Label(frame, text="Introduce tu telefono:")
etiquetaTelefono.pack()
entradaTelefono = tk.Entry(frame)
entradaTelefono.pack()
etiquetaCo = tk.Label(frame, text="Introduce tu nombre email:")
etiquetaCo.pack()
entradaCo = tk.Entry(frame)
entradaCo.pack()

array_contacto= []

def añadirContacto():
    nombre = entradaNombre.get()
    telefono = entradaTelefono.get()
    correo = entradaCo.get()
   
    if len(nombre)==0:
      return  messagebox.showerror(message='Nombre vacio',title='Error')
    
    if len(telefono)!=9:
      return  messagebox.showerror(message='Telefono inservible',title='Error')
    
   
    if '@' in correo:
        newContacto = Contacto(nombre,telefono,correo)
        array_contacto.append(newContacto)
        etiquetaVerificado = tk.Label(ventana, text="Contacto añadido")
        etiquetaVerificado.pack()
        return array_contacto
          
    else: messagebox.showerror(message='Falta un @ en el email',title='Error')

def actualizarContactos():

   if añadirContacto():
        listbox.delete(0, tk.END)
        for contacto in array_contacto:
            listbox.insert(tk.END, str(contacto))

def borrarContacto():
    seleccion = listbox.curselection()
    for i in reversed(seleccion):
        listbox.delete(i)
        del array_contacto[i]

botonActualizar = tk.Button(ventana, text="Agregar Contactos", command=actualizarContactos)
botonActualizar.pack()
botonBorrar = tk.Button(ventana, text="Borrar Contactos ", command=borrarContacto)
botonBorrar.pack()
ventana.mainloop()



      

