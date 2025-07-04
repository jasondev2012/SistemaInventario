import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from tkinter import messagebox
from ttkbootstrap.constants import *
from controllers.seguridad.rol_service import RolService
from views.seguridad.rol.rol_registro_view import RolRegistroView

class RolView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.usuario_sesion = master.usuario_sesion
        self.pack(fill="both", expand=True)

        style = ttk.Style()
        style.configure("Custom.TFrame", background="#3838F0")
        style.configure("Custom1.TFrame", background="#32BB54")
        style.configure("Custom2.TFrame", background="#BE791D")

        # TOP FRAME
        top_frame = ttk.Frame(self)
        top_frame.grid(row=0, columnspan=2, padx=10, sticky="nsew")

        ttk.Label(
            top_frame,
            text='Mantenimiento de Roles',
            font=("Helvetica", 16)
        ).pack(pady=20)

        # Define columnas

        # Datos de ejemplo
        self.roles = RolService.listar()

        # LEFT FRAME
        left_frame = ttk.Frame(self, style="Custom1.TFrame")
        left_frame.grid(row=1, rowspan=4, column=0, padx=10, pady=10, sticky="nsew")
        
        self.cols = self.obtener_columnas()
        # Crear tabla
        self.table = Tableview(
            left_frame,
            coldata=self.cols,
            rowdata=[
                [r.intRolID, r.strNombre, r.strEstado]
                for r in self.roles
            ],
            paginated=True,
            searchable=True,
            bootstyle="info",
            pagesize=50,
            autoalign=False,
            yscrollbar=True,
            autofit=True
        )
        self.table.pack(fill=BOTH, expand=True)
        self.table.view.bind("<<TreeviewSelect>>", self.on_row_selected)


        right_frame = ttk.Frame(self, padding=(5, 50))
        right_frame.columnconfigure(0, weight=1)
        right_frame.grid(row=1, rowspan=4, column=1, sticky="nw")
        # right_frame.columnconfigure(1, weight=1)
        ttk.Button(
            right_frame,
            text="Nuevo",
            bootstyle="success",
            width=20,
            command=lambda: self.abrir_registro_rol(0)
        ).grid(row=0, column=0, pady=2)
        ttk.Button(
            right_frame,
            text="Editar",
            bootstyle="info",
            width=20,
            command=lambda: self.abrir_registro_rol(self.intRolID)
        ).grid(row=1, column=0, pady=2)
        ttk.Button(
            right_frame,
            text="Eliminar",
            bootstyle="danger",
            width=20,
            command=lambda: self.dar_de_baja(self.intRolID)
        ).grid(row=2, column=0, pady=2)
        
        # Configurar filas y columnas para expandirse
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=11)
        self.columnconfigure(0, weight=6)
        self.columnconfigure(1, weight=5)

    def on_row_selected(self, event):
        selected = self.table.view.focus()
        values = self.table.view.item(selected, "values")
        if values:
            self.intRolID = int(values[0])

    def dar_de_baja(self, intRolID):
        respuesta = messagebox.askyesno("Confirmación", "¿Está seguro que desea dar de baja al rol?")
        if respuesta:
            respuesta = RolService.dar_de_baja(intRolID, self.usuario_sesion.intUsuarioID) 
            if respuesta.bitError:
                messagebox.showwarning("Validación!", respuesta.strMensaje)
            else:
                self.on_register_success()    

    def abrir_registro_rol(self, intRolID):

        # Crear el diálogo
        self.dialog = ttk.Toplevel(self)
        self.dialog.usuario_sesion = self.usuario_sesion
        self.dialog.title("Editar Rol" if intRolID > 0 else "Nuevo Rol")
        self.dialog.transient(self.winfo_toplevel())  # asociar con ventana principal
        self.dialog.grab_set()  # hace que sea modal

        # Establecer tamaño fijo (por ejemplo: 600x400)
        ancho = 600
        alto = 250

        # Calcular posición centrada
        screen_width = self.dialog.winfo_screenwidth()
        screen_height = self.dialog.winfo_screenheight()

        x = (screen_width // 2) - (ancho // 2)
        y = (screen_height // 2) - (alto // 2)

        self.dialog.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.dialog.resizable(False, False)  # evita redimensionamiento

        # Cargar la vista de registro dentro del diálogo
        RolRegistroView(self.dialog, intRolID, self.on_register_success).pack(fill="both", expand=True)
    def obtener_columnas(self):
        return [
            {"text": "ID", "stretch": False},
            {"text": "Nombre"},
            {"text": "Estado", "anchor": "center"},
        ]
    def on_register_success(self):
        self.roles = RolService.listar()
        
        if hasattr(self, 'table'):
            nueva_data = [
                [r.intRolID, r.strNombre, r.strEstado]
                for r in self.roles
            ]
            self.table.build_table_data(self.cols, nueva_data)
            self.table.load_table_data(True)
        if hasattr(self, 'dialog'):
            self.dialog.destroy()