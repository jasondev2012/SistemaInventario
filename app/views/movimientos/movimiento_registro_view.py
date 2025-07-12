import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar, messagebox
from controllers.catalogo.tipo_movimiento_service import TipoMovimientoService
from controllers.gestion.producto_service import ProductoService
from controllers.gestion.movimiento_service import MovimientoService

class MovimientoRegistroView(ttk.Frame):
    def __init__(self, master, intMovimientoID, on_register_success):
        super().__init__(master)
        self.usuario_sesion = master.usuario_sesion
        self.on_register_success = on_register_success
        
        self.pack(fill="both", expand=True)

        # Variables de control
        self.tipo_movimiento_var = StringVar()
        self.producto_var = StringVar()
        self.cantidad_var = StringVar()
        self.activo_var = ttk.BooleanVar(value=True)

        movimiento = None
        if intMovimientoID > 0:
            movimiento = MovimientoService.obtener(intMovimientoID)
        if movimiento is not None:
            self.nombre_var.set(movimiento.strNombre)
            self.abreviatura_var.set(movimiento.strAbreviatura)
            self.activo_var.set(movimiento.bitActivo)

        productos = ProductoService.listar_combo()
        tipos_movimientos = TipoMovimientoService.listar_combo()
        self.producto_opciones = {producto.strNombre: producto.intProductoID for producto in productos}
        self.tipo_movimiento = {tm.strNombre: tm.intTipoMovimientoID for tm in tipos_movimientos}

        # Frame derecho con formulario
        right_frame = ttk.Frame(self, padding=(5, 20))
        right_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        right_frame.columnconfigure(0, weight=1)


        # Nombres
        ttk.Label(right_frame, text='Tipo Movimiento', font=("Helvetica", 11)).grid(row=0, column=0, sticky="nsew")
        ttk.Combobox(
            right_frame,
            textvariable=self.tipo_movimiento_var,
            values=list(self.tipo_movimiento.keys()),
            font=("Helvetica", 11),
            state="readonly",
            bootstyle="primary",
            width=32
        ).grid(row=1, column=0, pady=3, padx=1, sticky="w")
        
        
        ttk.Label(right_frame, text='Producto', font=("Helvetica", 11)).grid(row=2, column=0, sticky="nsew")
        ttk.Combobox(
            right_frame,
            textvariable=self.producto_var,
            values=list(self.producto_opciones.keys()),
            font=("Helvetica", 11),
            state="readonly",
            bootstyle="primary",
            width=32
        ).grid(row=3, column=0, pady=3, padx=1, sticky="w")

        ttk.Label(right_frame, text='Cantidad', font=("Helvetica", 11)).grid(row=4, column=0, sticky="nsew")
        ttk.Entry(right_frame, textvariable=self.cantidad_var, width=45).grid(row=5, column=0, pady=3, padx=1, sticky="w")

        # Checkbox de activo
        ttk.Checkbutton(
            right_frame,
            text="¿Está activo?",
            variable=self.activo_var,
            bootstyle="success"
        ).grid(row=6, column=0, sticky="w", pady=10)

        # Botón de guardar
        ttk.Button(
            right_frame,
            text="Guardar Cambios",
            bootstyle="success",
            command=lambda: self.guardar_cambios(intMovimientoID)
        ).grid(row=7, column=0, columnspan=2, padx=5, pady=20)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
    def guardar_cambios(self, intMovimientoID):
        intTipoMovimientoID = next((v for k, v in self.tipo_movimiento.items() if k == self.tipo_movimiento_var.get()), None)
        intProductoID = next((v for k, v in self.producto_opciones.items() if k == self.producto_var.get()), None)
        
        response = MovimientoService.registrar(
                        int(intMovimientoID),
                        int(intTipoMovimientoID) if intTipoMovimientoID is not None else 0,
                        int(intProductoID) if intProductoID is not None else 0,
                        float(self.cantidad_var.get()),
                        bool(self.activo_var.get(),
                        int(self.usuario_sesion.intUsuarioID))
                    )
        if response.bitError:
            messagebox.showwarning("Validación", response.strMensaje)
        else:
            messagebox.showinfo("Hecho!", response.strMensaje)
            self.on_register_success()
