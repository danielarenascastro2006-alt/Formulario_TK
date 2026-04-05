import tkinter as Ventana

class Formulario:
    def __init__(self):
        self.color="green"
        self.entry_nombre= " "
        self.label_resultado=" "
        self.formulario=" "
        
    def iniciar_ventana(self):
        self.formulario=Ventana.Tk()
        self.formulario.title("Registro de Usuario")
        self.formulario.geometry("900x600")
        self.formulario.resizable(False, False)
        self.formulario.configure(bg="navy", padx=20, pady=20,)
        self.formulario.configure(cursor="hand2")
        return self.formulario
    
    
    def iniciar_preguntas(self):
        label_nombre = Ventana.Label(self.formulario, text="Digite el nombre del cliente")
        label_nombre.configure(padx=10, pady=10, borderwidth=2, fg="grey")
        label_nombre.pack(padx=20, pady=5)
        
        self.entry_nombre = Ventana.Entry(self.formulario)
        self.entry_nombre.configure(bg="grey")
        self.entry_nombre.pack(padx=20, pady=5)
        
        label_apellido = Ventana.Label(self.formulario, text="Digite el apellido del cliente")
        label_apellido.configure(padx=10, pady=10, borderwidth=2, fg="grey")
        label_apellido.pack(padx=20, pady=5)
        
        self.entry_apellido = Ventana.Entry(self.formulario)
        self.entry_apellido.configure(bg="grey")
        self.entry_apellido.pack(padx=20, pady=5)
        
        label_email = Ventana.Label(self.formulario, text="Digite el email del cliente")
        label_email.configure(padx=10, pady=10, borderwidth=2, fg="grey")
        label_email.pack(padx=20, pady=5)
        
        self.entry_email = Ventana.Entry(self.formulario)
        self.entry_email.configure(bg="grey")
        self.entry_email.pack(padx=20, pady=5)
        
        label_documento = Ventana.Label(self.formulario, text="Digite el documento del cliente")
        label_documento.configure(padx=10, pady=10, borderwidth=2, fg="grey")
        label_documento.pack(padx=20, pady=5)
        
        self.entry_documento = Ventana.Entry(self.formulario)
        self.entry_documento.configure(bg="grey")
        self.entry_documento.pack(padx=20, pady=5)
        
        label_telefono = Ventana.Label(self.formulario, text="Digite el telefono del cliente")
        label_telefono.configure(padx=10, pady=10, borderwidth=2, fg="grey")
        label_telefono.pack(padx=20, pady=5)
        
        self.entry_telefono = Ventana.Entry(self.formulario)
        self.entry_telefono.configure(bg="grey")
        self.entry_telefono.pack(padx=20, pady=5)
        
        
        buton_guardar =Ventana.Button(self.formulario, text="Enviar", command=self.tomar_datos)
        buton_guardar.configure(bg="grey")
        buton_guardar.pack(padx=20, pady=5)       
        
    def tomar_datos(self):
        aux_dato = self.entry_nombre.get()
        aux_dato2 =self.entry_apellido.get()
        aux_dato3 =self.entry_email.get()
        aux_dato4 =self.entry_documento.get()
        aux_dato5 =self.entry_telefono.get()
        self.imprimir_datos(aux_dato, aux_dato2, aux_dato3, aux_dato4, aux_dato5)
    
    def imprimir_datos(self, aux_dato, aux_dato2,aux_dato3, aux_dato4, aux_dato5):
        label_resultado = Ventana.Label(self.formulario, text="Nombre= "+aux_dato +" Apellido= "+ aux_dato2 +" Email= "+aux_dato3 +" Documento= "+ aux_dato4 +" Telefono= " + aux_dato5)
        label_resultado.configure(bg= self.color)
        label_resultado.pack()
        
