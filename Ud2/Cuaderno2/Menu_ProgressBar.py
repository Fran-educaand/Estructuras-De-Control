### **Ejercicio 2.2. Menú desplegable para la selección de opciones con un ProgressBar**

##* Crea una interfaz donde el usuario selecciona una opción de un `Menubutton` (como "Iniciar", "Pausar", "Detener") 
##y luego un `Progressbar` que indique el progreso de una tarea simulada.
import tkinter as tk
from tkinter import ttk
import time

def actualizar_progreso():
    
    if progress["value"] < 100:
        progress['value'] += 1  # Actualiza el progreso
        ventana.update_idletasks()  # Refresca la interfaz
        ventana.after(100,actualizar_progreso()) 

def pausar_progreso():

    print("Se detenio el progreso")

def iniciar_progreso():
     progress["value"]= 0
     progress["maximum"] = 100
     actualizar_progreso()

def detener_progreso():
    progress["value"]=0


ventana = tk.Tk()
ventana.title("Menu Progressbar")
ventana.geometry("400x300")

# Crear el MenuButton
menu_button = tk.Menubutton(ventana, text="Selecciona una opción", direction="below")
menu_button.pack(pady=20)

# Crear el menú asociado al MenuButton
menu = tk.Menu(menu_button, tearoff=False)

# Crear la ProgressBar
progress = ttk.Progressbar(ventana, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

# Agregar opciones al menú
menu.add_command(label="Iniciar",command=lambda: iniciar_progreso())
menu.add_command(label="Pausar",command= pausar_progreso())
menu.add_command(label="Detener",command= detener_progreso())


# Asociar el menú al MenuButton
menu_button["menu"] = menu
ventana.mainloop()

