##- **Ejercicio 2:** Crear una calculadora básica empleando una interfaz con botones para los números (0-9), las operaciones (+, -, *, /),
#  y un botón de igual (=) para calcular el resultado. Conforme se van presionando botones, 
# vamos escribiendo una expresión en un widget de tipo Entry (capturamos lo que había, lo borramos 
# y volvemos a escribir la expresión añadiendo lo nuevo). No obstante, si el botón presionado es `=` entonces habrá que evaluar la expresión 
# del Entry (`eval(entry.get())`... que podría arrojar excepciones), después borramos lo escrito y escribimos el resultado 
# (o un mensaje de error si se produjo). Opcionalmente, podríamos desplegar los botones en el Frame empleando una lista de tuplas (con todos los botones)
#  y recorriéndola con un bucle.
import tkinter as tk

ventana = tk.Tk()
ventana.title("Cambiar tamaño")
ventana.geometry("400x200")

cont = 0
for r in range(0, 4):
    for c in range(0, 4):
        cell = tk.Button(ventana, text=f'{cont}')
        cell.grid(padx=5, pady=5, row=r, column=c)
        cont = cont +1
      

ventana.mainloop()

