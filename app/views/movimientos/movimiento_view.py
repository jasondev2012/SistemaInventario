import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from tkinter import StringVar, messagebox
from ttkbootstrap.constants import *
from controllers.seguridad.rol_service import RolService
from views.seguridad.rol.rol_registro_view import RolRegistroView

class MovimientoView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.usuario_sesion = master.usuario_sesion
        self.pack(fill="both", expand=True)

        style = ttk.Style()
        # style.configure("Custom.TFrame", background="#3838F0")
        style.configure("Custom1.TFrame", background="#32BB54")
        # style.configure("Custom2.TFrame", background="#BE791D")

        # TOP FRAME
        top_frame = ttk.Frame(self)
        top_frame.grid(row=0, columnspan=6, padx=10, sticky="nsew")

        ttk.Label(
            top_frame,
            text='Movimientos',
            font=("Helvetica", 16)
        ).pack(pady=5)

        # Define columnas

        # Datos de ejemplo
        # self.roles = RolService.listar()

        # MID FRAME
        self.nombre_var = StringVar()
        mid_frame = ttk.Frame(self)
        mid_frame.grid(row=1, column=0, padx=10, sticky="nsew")
        
        # Nombres
        ttk.Label(mid_frame, text='Tipo de Operación:', font=("Helvetica", 11)).grid(row=0, column=0, padx=4, sticky="nsew")
        tipo_operacion_entry = ttk.Combobox(mid_frame, state="readonly", values=[
            "01 - Venta",
            "02 - Compra",
            "03 - Compra interna",
            "11 - Transferencia entre almacenes",
            "12 - MErmas",
            "16 - Saldo Inicial",
            "99 - Otros"
            ])
        tipo_operacion_entry.grid(row=1, column=0, pady=3, padx=4, sticky="w")

        ttk.Label(mid_frame, text="Fecha (DD-MM-YYYY):").grid(row=0, column=1, padx=4)
        ttk.DateEntry(mid_frame, dateformat="%d-%m-%Y", firstweekday=0).grid(row=1, column=1, pady=3, padx=4, sticky="w")

        ttk.Label(mid_frame, text="Tipo de Documento:").grid(row=0, column=2, sticky="nsew")
        tipo_documento_entry = ttk.Combobox(mid_frame, state="readonly", values=[
            "00 - Otros",
            "01 - Factura",
            "03 - Boleta de venta",
            "07 - Nota de crédito",
            "08 - Nota de débito"
            ])
        tipo_documento_entry.grid(row=1, column=2, pady=2, padx=4, sticky="w")
        
        ttk.Label(mid_frame, text="Número de Serie:").grid(row=0, column=3, sticky="nsew")
        serie_entry = ttk.Entry(mid_frame)
        serie_entry.grid(row=1, column=3, pady=3, padx=4, sticky="nsew")

        ttk.Label(mid_frame, text="Número de Comprobante:").grid(row=0, column=4, sticky="nsew")
        comprobante_entry = ttk.Entry(mid_frame)
        comprobante_entry.grid(row=1, column=4, pady=3, padx=4, sticky="nsew")

        ttk.Label(mid_frame, text="Cantidad:").grid(row=0, column=5, sticky="nsew")
        cantidad_entry = ttk.Entry(mid_frame)
        cantidad_entry.grid(row=1, column=5, pady=3, padx=4, sticky="nsew")

        ttk.Label(mid_frame, text="Costo Unitario:").grid(row=0, column=6, sticky="nsew")
        costo_unitario_entry = ttk.Entry(mid_frame)
        costo_unitario_entry.grid(row=1, column=6, pady=3, padx=4, sticky="nsew")
        ttk.Button(
            mid_frame,
            text="Guardar",
            bootstyle="success"
        ).grid(row=1, column=7, columnspan=2, padx=5, pady=3)
        # Configurar filas y columnas para expandirse
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=11)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=1)
        self.columnconfigure(7, weight=1)

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