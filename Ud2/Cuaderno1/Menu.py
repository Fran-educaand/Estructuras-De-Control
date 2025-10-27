##- **Ejercicio 5:** Crear un menú con cuatro entradas (Rojo, Verde, Azul y Amarillo) para cambiar el fondo de la ventana. 
##Cambia el fondo de la ventana cuando el usuario seleccione una opción.

import tkinter as tk

ventana = tk.Tk()
ventana.title("Botó y tres colores")
ventana.geometry("600x400")

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Crear un menú
menu_color = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Cambia color", menu=menu_color)

def cambiarColor(color):
    match color:
        case "Rojo": 
             ventana.config(bg="red")
        case "Verde":
             ventana.config(bg="green")
        case "Azul":
             ventana.config(bg="blue")
        case "Amarillo":
              ventana.config(bg="yellow")

menu_color.add_command(label="Rojo",command=lambda: cambiarColor("Rojo"))
menu_color.add_command(label="Verde",command=lambda: cambiarColor("Verde"))
menu_color.add_command(label="Azul",command=lambda: cambiarColor("Azul"))
menu_color.add_command(label="Amarillo",command=lambda: cambiarColor("Amarillo"))

ventana.mainloop()
                             