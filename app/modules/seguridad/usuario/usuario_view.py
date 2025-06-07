import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from tkinter import messagebox, StringVar, filedialog
from modules.auth.auth_service import AuthService
from PIL import Image, ImageTk

class UsuarioView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.foto_imgtk = None
        self.pack(fill="both", expand=True)  # Asegúrate de empacar el frame principal

        style = ttk.Style()
        style.configure("Custom.TFrame", background="#3838F0")
        style.configure("Custom1.TFrame", background="#32BB54")
        style.configure("Custom2.TFrame", background="#BE791D")

        # TOP FRAME
        top_frame = ttk.Frame(self)
        top_frame.grid(row=0, columnspan=2, padx=10, sticky="nsew")

        ttk.Label(
            top_frame,
            text='Mantenimiento de Usuarios',
            font=("Helvetica", 16)
        ).pack(pady=20)

        # Define columnas
        columns = [
            {"text": "ID", "stretch": False},
            {"text": "Nombre"},
            {"text": "Rol"},
            {"text": "Activo", "anchor": "center"},
        ]

        # Datos de ejemplo
        usuarios = [
            [1, "Jason Joseph Gutierrez Cuadros", "Admin", True],
            [2, "Ana", "Usuario", True],
            [3, "Luis", "Invitado", False]
        ]

        # LEFT FRAME
        left_frame = ttk.Frame(self, style="Custom1.TFrame")
        left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        # Crear tabla
        self.table = Tableview(
            left_frame,
            coldata=columns,
            rowdata=usuarios,
            paginated=True,
            searchable=True,
            bootstyle="info",
            pagesize=50,
            autoalign=False,
            yscrollbar=True,
            autofit=True
        ).pack(fill=BOTH, expand=True)
        
        notebook = ttk.Notebook(self, bootstyle="primary")
        notebook.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        # notebook.pack(fill="both", expand=True, padx=10, pady=10)

        notebook.columnconfigure(1, weight=1)
        right_frame = ttk.Frame(notebook, padding=(5, 20))
        right_frame.columnconfigure(0, weight=1)
        right_frame.columnconfigure(1, weight=1)

        
        self.tipo_usuario_var = StringVar()
        self.nombres_var = StringVar()
        self.apellido_paterno_var = StringVar()
        self.apellido_materno_var = StringVar()
        self.tipo_documento_var = StringVar()
        self.numero_documento_var = StringVar()
        self.usuario_var = StringVar()
        self.password_var = StringVar()
        self.activo_var = ttk.BooleanVar(value=True) 
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
        notebook.add(right_frame, text="Datos del Usuario")

        self.foto_label = ttk.Label(right_frame)
        self.foto_label.grid(rowspan=3, columnspan=2, padx=10, pady=10)

        ttk.Button(
            right_frame,
            text="Cargar Foto",
            command=self.cargar_foto,
            bootstyle="primary-outline"
        ).grid(row=4, columnspan=2, padx=5, pady=3)

        ttk.Label(
            right_frame,
            text='Rol: ',
            font=("Helvetica", 11),
        ).grid(row=5, column=0, sticky="nsew")
        ttk.Combobox(
            right_frame,
            textvariable=self.tipo_usuario_var,
            values=list(self.rol_opciones.keys()),
            font=("Helvetica", 11),
            state="readonly",
            bootstyle="primary"
        ).grid(row=6, column=0, pady=3, padx=1, sticky="ew")

        ttk.Label(
            right_frame,
            text='Nombres: ',
            font=("Helvetica", 11),
        ).grid(row=5, column=1, sticky="nsew")
        ttk.Entry(right_frame, textvariable=self.nombres_var).grid(row=6, column=1, pady=3, padx=1, sticky="ew")

        ttk.Label(
            right_frame,
            text='Apellido Paterno',
            font=("Helvetica", 11)
        ).grid(row=7, column=0, sticky="nsew")
        ttk.Entry(right_frame, textvariable=self.apellido_paterno_var).grid(row=8, column=0, pady=3, padx=1, sticky="ew")

        ttk.Label(
            right_frame,
            text='Apellido Materno',
            font=("Helvetica", 11),
        ).grid(row=7, column=1, sticky="nsew")
        ttk.Entry(right_frame, textvariable=self.apellido_materno_var).grid(row=8, column=1, pady=3, padx=1, sticky="ew")

        ttk.Label(
            right_frame,
            text='Tipo Documento',
            font=("Helvetica", 11)
        ).grid(row=9, column=0, sticky="nsew")
        ttk.Combobox(
            right_frame,
            textvariable=self.tipo_documento_var,
            values=list(self.tipo_documento_opciones.keys()),
            font=("Helvetica", 11),
            state="readonly",
            bootstyle="primary"
        ).grid(row=10, column=0, pady=3, padx=1, sticky="ew")

        ttk.Label(
            right_frame,
            text='Número Documento',
            font=("Helvetica", 11),
        ).grid(row=9, column=1, sticky="nsew")
        ttk.Entry(right_frame, textvariable=self.numero_documento_var).grid(row=10, column=1, pady=3, padx=1, sticky="ew")

        ttk.Label(
            right_frame,
            text='Usuario',
            font=("Helvetica", 11),
        ).grid(row=11, column=0, sticky="nsew")
        ttk.Entry(right_frame, textvariable=self.usuario_var).grid(row=12, column=0, pady=3, padx=1, sticky="ew")

        ttk.Label(
            right_frame,
            text='Contraseña',
            font=("Helvetica", 11),
        ).grid(row=11, column=1, sticky="nsew")
        ttk.Entry(right_frame, show='*', textvariable=self.password_var).grid(row=12, column=1, pady=3, padx=1, sticky="ew")

        ttk.Checkbutton(
            right_frame,
            text="¿Está activo?",
            variable=self.activo_var,
            bootstyle="success" 
        ).grid(row=13, column=0, sticky="w", pady=5)

        ttk.Button(
            right_frame,
            text="Guardar Cambios",
            bootstyle="success"
        ).grid(row=14, columnspan=2, padx=5, pady=20)
        # Configurar filas y columnas para expandirse
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=11)
        self.columnconfigure(0, weight=7)
        self.columnconfigure(1, weight=5)

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