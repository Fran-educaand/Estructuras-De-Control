import tkinter as tk
class TimerApp:

    def __init__(self):
        self.tiempoInicial = 10
        self.running = False
        self.tiempoRestante = self.tiempoInicial
        self.label = tk.Label(text=f"Tiempo: {self.tiempoRestante}", font=('Arial',24))
        self.label.pack(padx=20,pady=20)
        self.boton = tk.Button(text="Inicar/Pausar",command=self.toggle_timer)
        self.boton.pack()
    
    def toggle_timer(self):
        if self.running== True:   
              self.running = False   
        else : 
               self.running = True
               self.countdown()
        
    def countdown(self):
        
        if self.tiempoRestante >= 0 and self.running == True:
            self.label.config(text=f"Tiempo: {self.tiempoRestante}")
            self.tiempoRestante = self.tiempoRestante - 1
            self.label.after(1000,self.countdown)
        else: pass

        if self.tiempoRestante == 0:
             print("Tiempo Agotado")
      


ventana = tk.Tk()
ventana.title("TimerApp")
ventana.geometry("400x300")
t = TimerApp()
ventana.mainloop()