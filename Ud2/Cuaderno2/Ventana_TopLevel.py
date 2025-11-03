### **Ejercicio 2.8. Ventana emergente con Toplevel para la confirmación de una acción**

##*  Crea una ventana emergente usando el widget `Toplevel` que aparezca cuando el usuario haga clic en un botón.
##Dentro de esa ventana, utiliza un `Label` 
##y un `Checkbutton` para pedir al usuario una confirmación (por ejemplo, "¿Estás seguro de que quieres continuar?").


import tkinter as tk

def abrir_ventana():
    # Crear una nueva ventana Toplevel
    ventana_secundaria = tk.Toplevel(root)
    ventana_secundaria.title("Ventana Secundaria")

    # Agregar un mensaje a la nueva ventana
    tk.Label(ventana_secundaria, text="¡Esta es una ventana secundaria!").pack()

    # Puedes añadir más widgets a la ventana secundaria si lo necesitas
    tk.Checkbutton(ventana_secundaria, text="Cerrar", command=ventana_secundaria.destroy).pack()

root = tk.Tk()
root.title("Ventana Principal")

# Botón para abrir la ventana secundaria
boton = tk.Button(root, text="Abrir ventana secundaria", command=abrir_ventana)
boton.pack()

root.mainloop()