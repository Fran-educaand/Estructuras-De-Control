import tkinter as tk
from tkinter import messagebox
import time

ventana = tk.Tk()
ventana.title("Botó y tres colores")
ventana.geometry("400x300")


label = tk.Label(ventana, font=('times', 30, 'bold'), bg='white')

label.pack(fill="both", expand=1)

def actualizarReloj():
    nuevaHora=time.strftime('%H:%M:%S')
    
    label.config(text=f"{nuevaHora}")
   
    label.after(200, actualizarReloj)
    
actualizarReloj()
ventana.mainloop()