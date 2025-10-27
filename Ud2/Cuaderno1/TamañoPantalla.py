##- **Ejercicio 4:** Crea una interfaz con tres botones que al ser presionados cambien el tamaño de la ventana. Ofrece tres opciones: pequeño, mediano 
##y grande, usando un `match-case` para cambiar el tamaño de la ventana según la selección.
import tkinter as tk


ventana = tk.Tk()
ventana.title("Cambiar tamaño")
ventana.geometry("800x500")


def cambiarTamaño(event):
    match event.widget.cget('text'):
        case "Haz la pantalla grande": 
            ventana.geometry("1600x1000")
        case "Haz la pantalla mediana":
            ventana.geometry("800x500")
        case "Haz la pantalla chica":
            ventana.geometry("400x250")

botonG = tk.Button(ventana, text="Haz la pantalla grande")
botonG.pack()

botonM = tk.Button(ventana, text="Haz la pantalla mediana")
botonM.pack()

botonP = tk.Button(ventana, text="Haz la pantalla chica")
botonP.pack()

'''botonG = tk.Button(ventana, text="Haz la pantalla grande",command=lambda: ventana.geometry("1600x1000"))
botonG.pack()

botonM = tk.Button(ventana, text="Haz la pantalla mediana",command=lambda: ventana.geometry("800x500"))
botonM.pack()

botonP = tk.Button(ventana, text="Haz la pantalla chica",command=lambda: ventana.geometry("400x250"))
botonP.pack()'''

ventana.bind("<ButtonPress>",cambiarTamaño)

ventana.mainloop()

