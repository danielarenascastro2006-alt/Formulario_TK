import tkinter as Ventana

class Formulario:
    def __init__(self):
        self.color="rojo"
        self.entry_nombre= " "
        self.label_resultado=" "
        self.formulario=" "
        
    def iniciar_ventana(self):
        self.formulario=Ventana.Tk()
        self.formulario.title("Registro de Usuario")
        self.formulario.geometry("900x600")
        self.formulario.resizable(False, False)
        self.formulario.configure(bg="navy")
        self.formulario.configure(cursor="hand2")
        return self.formulario
    
    
    def iniciar_preguntas(self):
        label_nombre = Ventana.Label(self.formulario, text="Digite el nombre del cliente")
        label_nombre.configure(padx=10, pady=10, borderwidth=2, fg="grey")
        label_nombre.pack()
        
        self.entry_nombre = Ventana.Entry(self.formulario)
        self.entry_nombre.configure(bg="grey")
        
        buton_guardar =Ventana.Button(self.formulario, text="Enviar", command=self.hacer_click)
        buton_guardar.configure(bg="grey")
        buton_guardar.pack()        
    
    def hacer_click(self):
        print("Cliccccckkk .....")