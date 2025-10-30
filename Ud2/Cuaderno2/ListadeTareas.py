### **Ejercicio 2.1. Lista de tareas con Checkbuttons**

##* Crea una aplicación de lista de tareas. 
#El usuario podrá añadir tareas a una `Listbox` y marcar cada tarea como completada utilizando un `Checkbutton`.
#Añadir un botón para eliminar tareas completadas.

import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Lista de tareas")
ventana.geometry("400x300")

listbox = tk.Listbox(ventana, selectmode=tk.MULTIPLE, height=6, width=30)
listbox.pack(pady=20)

etiquetaTarea = tk.Label(ventana, text="Introduce tu tarea:")
etiquetaTarea.pack()
entradaTarea = tk.Entry(ventana)
entradaTarea.pack()

def borrarTarea():
    for i,variable in enumerate (checkVariables):
        if variable.get():
            checkButtons[i].destroy()
            listbox.delete(i)
            del checkButtons[i]
            del checkVariables[i]
            
        else:pass

checkVariables = []
checkButtons = []
boton = tk.Button(ventana , text="Borra Aqui",command=borrarTarea)
boton.pack()


def añadirTarea():
   
    if len(entradaTarea.get()) == 0:
        return  messagebox.showerror(message='No hay tarea',title='Error')
    else:
        var1 = tk.IntVar()
        cb1 = tk.Checkbutton(ventana, text=f'{entradaTarea.get()}', variable=var1)
        checkButtons.append(cb1)
        checkVariables.append(var1)
        cb1.pack()
        listbox.insert(tk.END,f"{cb1.cget('text')}")


botonM = tk.Button(ventana, text="Añadir tarea",command=añadirTarea)
botonM.pack()


ventana.mainloop()