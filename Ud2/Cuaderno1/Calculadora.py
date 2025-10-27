##- **Ejercicio 2:** Crear una calculadora básica empleando una interfaz con botones para los números (0-9), las operaciones (+, -, *, /),
#  y un botón de igual (=) para calcular el resultado. Conforme se van presionando botones, 
# vamos escribiendo una expresión en un widget de tipo Entry (capturamos lo que había, lo borramos 
# y volvemos a escribir la expresión añadiendo lo nuevo). No obstante, si el botón presionado es `=` entonces habrá que evaluar la expresión 
# del Entry (`eval(entry.get())`... que podría arrojar excepciones), después borramos lo escrito y escribimos el resultado 
# (o un mensaje de error si se produjo). Opcionalmente, podríamos desplegar los botones en el Frame empleando una lista de tuplas (con todos los botones)
#  y recorriéndola con un bucle.
import tkinter as tk

ventana = tk.Tk()
ventana.title("Botó y tres colores")
ventana.geometry("600x400")

boton0 = tk.Button(ventana, text="0", command=cambiarColor)
boton1 = tk.Button(ventana, text="1", command=cambiarColor)
boton2= tk.Button(ventana, text="2", command=cambiarColor)
boton3 = tk.Button(ventana, text="3", command=cambiarColor)
boton4 = tk.Button(ventana, text="4", command=cambiarColor)
boton5 = tk.Button(ventana, text="5", command=cambiarColor)
boton6 = tk.Button(ventana, text="6", command=cambiarColor)
boton7 = tk.Button(ventana, text="7", command=cambiarColor)
boton8 = tk.Button(ventana, text="8", command=cambiarColor)
boton9 = tk.Button(ventana, text="9", command=cambiarColor)
botonMas = tk.Button(ventana, text="+", command=cambiarColor)
botonMenos = tk.Button(ventana, text="-", command=cambiarColor)
boton1.pack() 
boton2.pack() 
boton3.pack() 
ventana.mainloop()


