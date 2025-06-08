import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar, filedialog, messagebox
from PIL import Image, ImageTk
from services.seguridad.usuario_service import UsuarioService
from models.seguridad.usuario_registro_model import UsuarioRegistroModel

class UsuarioRegistroView(ttk.Frame):
    def __init__(self, master, intUsuarioID, on_register_success):
        super().__init__(master)
        self.usuario_sesion = master.usuario_sesion
        self.on_register_success = on_register_success
        
        self.pack(fill="both", expand=True)

        # Variables de control
        self.rol_var = ttk.StringVar()
        self.nombres_var = StringVar()
        self.apellido_paterno_var = StringVar()
        self.apellido_materno_var = StringVar()
        self.tipo_documento_var = ttk.StringVar()
        self.numero_documento_var = StringVar()
        self.usuario_var = StringVar()
        self.password_var = StringVar()
        self.activo_var = ttk.BooleanVar(value=True)

        # Diccionarios de opciones
        self.rol_opciones = {
            "Administrador": 1,
            "Vendedor": 2,
            "Proveedor": 3
        }
        self.tipo_documento_opciones = {
            "DNI": 1,
            "Carnet de Extranjería": 2,
            "Pasaporte": 3
        }
        usuario = None
        if intUsuarioID > 0:
            usuario = UsuarioService.obtener(intUsuarioID)
        if usuario is not None:
            print("aaaaa")
            self.rol_var.set(next((k for k, v in self.rol_opciones.items() if v == usuario.intRolID), None))
            self.nombres_var.set(usuario.strNombres)
            self.apellido_paterno_var.set(usuario.strApellidoPaterno)
            self.apellido_materno_var.set(usuario.strApellidoMaterno)
            self.tipo_documento_var.set(next((k for k, v in self.tipo_documento_opciones.items() if v == usuario.intDocumentoIdentidadID), None))
            self.numero_documento_var.set(usuario.strNumeroDocumento)
            self.usuario_var.set(usuario.strUsuario)
            self.password_var.set(usuario.strPassword)
            self.activo_var.set(usuario.bitActivo)


        # Frame derecho con formulario
        right_frame = ttk.Frame(self, padding=(5, 20))
        right_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        right_frame.columnconfigure(0, weight=1)
        right_frame.columnconfigure(1, weight=1)

        # Imagen y botón de carga
        self.foto_label = ttk.Label(right_frame)
        self.foto_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        ttk.Button(
            right_frame,
            text="Cargar Foto",
            command=self.cargar_foto,
            bootstyle="primary-outline"
        ).grid(row=1, column=0, columnspan=2, padx=5, pady=3)

        # Rol
        ttk.Label(right_frame, text='Rol:', font=("Helvetica", 11)).grid(row=2, column=0, sticky="nsew")
        ttk.Combobox(
            right_frame,
            textvariable=self.rol_var,
            values=list(self.rol_opciones.keys()),
            font=("Helvetica", 11),
            state="readonly",
            bootstyle="primary",
            width=32
        ).grid(row=3, column=0, pady=3, padx=1, sticky="w")

        # Nombres
        ttk.Label(right_frame, text='Nombres:', font=("Helvetica", 11)).grid(row=2, column=1, sticky="nsew")
        ttk.Entry(right_frame, textvariable=self.nombres_var, width=45).grid(row=3, column=1, pady=3, padx=1, sticky="w")

        # Apellidos
        ttk.Label(right_frame, text='Apellido Paterno', font=("Helvetica", 11)).grid(row=4, column=0, sticky="nsew")
        ttk.Entry(right_frame, textvariable=self.apellido_paterno_var, width=45).grid(row=5, column=0, pady=3, padx=1, sticky="w")

        ttk.Label(right_frame, text='Apellido Materno', font=("Helvetica", 11)).grid(row=4, column=1, sticky="nsew")
        ttk.Entry(right_frame, textvariable=self.apellido_materno_var, width=45).grid(row=5, column=1, pady=3, padx=1, sticky="w")

        # Documento
        ttk.Label(right_frame, text='Tipo Documento', font=("Helvetica", 11)).grid(row=6, column=0, sticky="nsew")
        ttk.Combobox(
            right_frame,
            textvariable=self.tipo_documento_var,
            values=list(self.tipo_documento_opciones.keys()),
            font=("Helvetica", 11),
            state="readonly",
            bootstyle="primary",
            width=32
        ).grid(row=7, column=0, pady=3, padx=1, sticky="w")

        ttk.Label(right_frame, text='Número Documento', font=("Helvetica", 11)).grid(row=6, column=1, sticky="nsew")
        ttk.Entry(right_frame, textvariable=self.numero_documento_var, width=45).grid(row=7, column=1, pady=3, padx=1, sticky="w")

        # Usuario y contraseña
        ttk.Label(right_frame, text='Usuario', font=("Helvetica", 11)).grid(row=8, column=0, sticky="nsew")
        ttk.Entry(right_frame, textvariable=self.usuario_var, width=45).grid(row=9, column=0, pady=3, padx=1, sticky="w")

        ttk.Label(right_frame, text='Contraseña', font=("Helvetica", 11)).grid(row=8, column=1, sticky="nsew")
        ttk.Entry(right_frame, show='*', textvariable=self.password_var, width=45).grid(row=9, column=1, pady=3, padx=1, sticky="w")

        # Checkbox de activo
        ttk.Checkbutton(
            right_frame,
            text="¿Está activo?",
            variable=self.activo_var,
            bootstyle="success"
        ).grid(row=10, column=0, sticky="w", pady=10)

        # Botón de guardar
        ttk.Button(
            right_frame,
            text="Guardar Cambios",
            bootstyle="success",
            command=lambda: self.guardar_cambios(intUsuarioID)
        ).grid(row=11, column=0, columnspan=2, padx=5, pady=20)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
    def guardar_cambios(self, intUsuarioID):
        intRolID = next((v for k, v in self.rol_opciones.items() if k == self.rol_var.get()), None)
        intDocumentoIdentidadID = next((v for k, v in self.tipo_documento_opciones.items() if k == self.tipo_documento_var.get()), None)
        response = UsuarioService.registrar(
                        int(intUsuarioID),
                        int(intRolID) if intRolID is not None else 0,
                        self.usuario_var.get(),
                        self.password_var.get(),
                        self.nombres_var.get(),
                        self.apellido_paterno_var.get(),
                        self.apellido_materno_var.get(),
                        int(intDocumentoIdentidadID) if intDocumentoIdentidadID is not None else 0,
                        self.numero_documento_var.get(),
                        bool(self.activo_var.get()),
                        int(self.usuario_sesion.intUsuarioID)
                    )
        if response.bitError:
            messagebox.showwarning("Validación", response.strMensaje)
        else:
            messagebox.showinfo("Hecho!", response.strMensaje)
            self.on_register_success()
            
    def cargar_foto(self):
        ruta = filedialog.askopenfilename(
            filetypes=[("Imagenes", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if ruta:
            imagen = Image.open(ruta)
            imagen = imagen.resize((100, 100))  # ajusta el tamaño deseado
            self.foto_imgtk = ImageTk.PhotoImage(imagen)

            if self.foto_label:
                self.foto_label.configure(image=self.foto_imgtk)
