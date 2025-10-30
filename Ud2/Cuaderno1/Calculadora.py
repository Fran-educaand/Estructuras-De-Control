##- **Ejercicio 2:** Crear una calculadora básica empleando una interfaz con botones para los números (0-9), las operaciones (+, -, *, /),
#  y un botón de igual (=) para calcular el resultado. Conforme se van presionando botones, 
# vamos escribiendo una expresión en un widget de tipo Entry (capturamos lo que había, lo borramos 
# y volvemos a escribir la expresión añadiendo lo nuevo). No obstante, si el botón presionado es `=` entonces habrá que evaluar la expresión 
# del Entry (`eval(entry.get())`... que podría arrojar excepciones), después borramos lo escrito y escribimos el resultado 
# (o un mensaje de error si se produjo). Opcionalmente, podríamos desplegar los botones en el Frame empleando una lista de tuplas (con todos los botones)
#  y recorriéndola con un bucle.
import tkinter as tk

frame = tk.Tk()
frame.title("Cambiar tamaño")
frame.geometry("400x200")



entrada =  tk.Entry(frame)
entrada.config ( state = "readonly")
entrada.pack(pady=15)

frame = tk.Frame(frame)
frame.pack()

cont = 0
for fila in range(0, 4):
    for columna in range(0, 4):
        if fila == 0 and columna <3:
            cell = tk.Button(frame, text=f'{cont}')
            cell.grid(padx=5, pady=5, row=fila, column=columna)
            cont = cont +1
        elif fila == 0 and columna == 3:
             cell = tk.Button(frame, text=f'+')
             cell.grid(padx=5, pady=5, row=fila, column=columna)
             cont = cont +1
        elif fila == 1 and columna < 3:
            cell = tk.Button(frame, text=f'{cont}')
            cell.grid(padx=5, pady=5, row=fila, column=columna)
            cont = cont +1
        elif fila == 1 and columna == 3:
            cell = tk.Button(frame, text=f'-')
            cell.grid(padx=5, pady=5, row=fila, column=columna)
        elif fila == 2 and columna < 3:
            cell = tk.Button(frame, text=f'{cont}')
            cell.grid(padx=5, pady=5, row=fila, column=columna)
            cont = cont +1
        elif fila == 2 and columna == 3:
            cell = tk.Button(frame, text=f'x')
            cell.grid(padx=5, pady=5, row=fila, column=columna)
        elif fila == 3 and columna == 2:
            cell = tk.Button(frame, text=f'/')
            cell.grid(padx=5, pady=5, row=fila, column=columna)
            
        elif fila == 3 and columna == 3:
            cell = tk.Button(frame, text=f'=')
            cell.grid(padx=5, pady=5, row=fila, column=columna)
            
            
            

frame.mainloop()

