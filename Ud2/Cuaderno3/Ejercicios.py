from tkinter import *
from collections import deque
from tkinter import messagebox



class Window:
    def __init__(self, master):
        self.master = master

        self.Main = Frame(self.master)

        self.stack = deque(maxlen=10)
        self.stackcursor = 0

        self.L1 = Label(self.Main, text="This is my NotePad")
        self.L1.pack(padx=5, pady=5)

        self.T1 = Text(self.Main, width=80, height=20)
        self.T1.pack(padx=5, pady=5)

        self.menu = Menu(self.Main)
        self.menu.add_command(label="Print", command=self.print_stack)
        self.menu.add_command(label="Undo", command=self.undo)
        self.menu.add_command(label="Redo", command=self.redo)
        self.menu.add_command(label="Blanco", command=lambda: self.change_color("white"))
        self.menu.add_command(label="Gris", command=lambda: self.change_color("gray"))
        self.menu.add_command(label="Azul", command=lambda: self.change_color("blue"))
        self.master.config(menu=self.menu)

        self.B1 = Button(self.Main, text="Print", width=8, command=self.display)
        self.B1.pack(padx=5, pady=5, side="left")

        self.B2 = Button(self.Main, text="Clear", width=8, command=self.clear)
        self.B2.pack(padx=5, pady=5, side="left")

        self.B3 = Button(self.Main, text="Undo", width=8, command=self.undo)
        self.B3.pack(padx=5, pady=5, side="left")

        self.B4 = Button(self.Main, text="Redo", width=8, command=self.redo)
        self.B4.pack(padx=5, pady=5, side="left")

        self.Main.pack(padx=5, pady=5)

    def display(self):
        print(self.T1.get("1.0", "end"))

    def clear(self):
        mensaje = messagebox.askyesno(title='¿Estas seguro?',message="Quieres borrar?")
        if mensaje:
         self.T1.delete("1.0", "end")
        else: pass

    def stackify(self):
        text_content = self.T1.get("1.0", "end - 1c")
        estricted_words = ["Python", "error"]

        if any(word in text_content for word in estricted_words):
            print("⚠️ El texto contiene palabras restringidas y no se guardará en el historial.")
        else:
            self.stack.append(text_content)
            Window.cambiarTamaño(self)
        if self.stackcursor < 9:
            self.stackcursor += 1
    def cambiarTamaño(self):
        text_content = self.T1.get("1.0", "end - 1c")
        longitud = len(text_content)
        if longitud <50:
            self.T1.configure(width=40 , height=10)
        elif longitud >50 and longitud <200:
            self.T1.configure(width=80 , height=20)
        else: self.T1.configure(width=160 , height=400)


    def undo(self):
        if self.stackcursor != 0:
            self.clear()
            if self.stackcursor > 0: self.stackcursor -= 1
            self.T1.insert("0.0", self.stack[self.stackcursor])

    def redo(self):
        if len(self.stack) > self.stackcursor + 1:
            self.clear()
            if self.stackcursor < 9: self.stackcursor += 1
            self.T1.insert("0.0", self.stack[self.stackcursor])
    
    def change_color(self, color):
     self.T1.config(bg=color)

    def print_stack(self):
        i = 0
        for stack in self.stack:
            print(str(i) + " " + stack)
            i += 1


root = Tk()
window = Window(root)
root.bind("<Key>", lambda event: window.stackify())
root.mainloop()