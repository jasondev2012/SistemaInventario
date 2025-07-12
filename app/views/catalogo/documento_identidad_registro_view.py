import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar, messagebox
from controllers.catalogo.documento_identidad_service import DocumentoIdentidadService

class DocumentoIdentidadRegistroView(ttk.Frame):
    def __init__(self, master, intDocumentoIdentidadID, on_register_success):
        super().__init__(master)
        self.usuario_sesion = master.usuario_sesion
        self.on_register_success = on_register_success
        
        self.pack(fill="both", expand=True)

        # Variables de control
        self.nombre_var = StringVar()
        self.activo_var = ttk.BooleanVar(value=True)

        documentoIdentidad = None
        if intDocumentoIdentidadID > 0:
            documentoIdentidad = DocumentoIdentidadService.obtener(intDocumentoIdentidadID)
        if documentoIdentidad is not None:
            self.nombre_var.set(documentoIdentidad.strNombre)
            self.activo_var.set(documentoIdentidad.bitActivo)


        # Frame derecho con formulario
        right_frame = ttk.Frame(self, padding=(5, 20))
        right_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        right_frame.columnconfigure(0, weight=1)


        # Nombres
        ttk.Label(right_frame, text='Nombre:', font=("Helvetica", 11)).grid(row=0, column=0, sticky="nsew")
        ttk.Entry(right_frame, textvariable=self.nombre_var, width=65).grid(row=1, column=0, pady=3, padx=1, sticky="w")

        # Checkbox de activo
        ttk.Checkbutton(
            right_frame,
            text="¿Está activo?",
            variable=self.activo_var,
            bootstyle="success"
        ).grid(row=2, column=0, sticky="w", pady=10)

        # Botón de guardar
        ttk.Button(
            right_frame,
            text="Guardar Cambios",
            bootstyle="success",
            command=lambda: self.guardar_cambios(intDocumentoIdentidadID)
        ).grid(row=3, column=0, columnspan=2, padx=5, pady=20)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
    def guardar_cambios(self, intDocumentoIdentidadID):
        response = DocumentoIdentidadService.registrar(
                        int(intDocumentoIdentidadID),
                        self.nombre_var.get(),
                        bool(self.activo_var.get())
                    )
        if response.bitError:
            messagebox.showwarning("Validación", response.strMensaje)
        else:
            messagebox.showinfo("Hecho!", response.strMensaje)
            self.on_register_success()
