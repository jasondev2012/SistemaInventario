import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from views.auth.login_view import LoginView
from views.seguridad.usuario.usuario_view import UsuarioView
from views.seguridad.rol.rol_view import RolView
from PIL import Image, ImageTk
import tkinter.font as tkfont

#TEMAS PARA EL TKBOOTSTRAP
# flatly
# cosmo
# journal
# darkly
# superhero
# solar
# morph
# vapor

def iniciar_app():
    
    app = ttk.Window(title="Sistema de Inventario", themename="superhero")
    ancho = 1366
    alto = 768
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    
    x = (screen_width // 2) - (ancho // 2)
    y = (screen_height // 2) - (alto // 2)
    app.geometry("1366x768")
    app.geometry(f"{ancho}x{alto}+{x}+{y}")
    app.resizable(False, False)  # evita redimensionamiento
    def mostrar_manteniemiento_usuario():
        for widget in app.content_frame.winfo_children():
            widget.destroy()
        app.content_frame.usuario_sesion = app.usuario_sesion
        UsuarioView(app.content_frame)

    def mostrar_manteniemiento_rol():
        for widget in app.content_frame.winfo_children():
            widget.destroy()
        app.content_frame.usuario_sesion = app.usuario_sesion
        RolView(app.content_frame)

    def mostrar_login():
        for widget in app.winfo_children():
            widget.destroy()
        LoginView(app, on_login_success)

    def on_login_success(usuarioSesion):
        app.usuario_sesion = usuarioSesion

        for widget in app.winfo_children():
            widget.destroy()

        cargar_menu()

        style = ttk.Style()
        style.configure("Custom4.TFrame", background="#BE791D")
        # Crear el contenedor principal de contenido
        app.content_frame = ttk.Frame(app, style="Custom4.TFrame", width=1366)
        app.content_frame.pack(fill="both", expand=True)

        # Contenido de bienvenida dentro del content_frame
        ttk.Label(
            app.content_frame,
            text=f'Bienvenido al sistema de inventario {app.usuario_sesion.strNombresCompletos}',
            font=("Helvetica", 16)

        ).pack(pady=60)

    def cargar_menu():
        Style = ttk.Style()
        Style.configure('TMenubutton', font=('Helvetica', 13))
        Style.configure('custom.TButton', background='tomato', focuscolor="tomato", bordercolor="tomato", foreground='white', font=('Helvetica', 13))
        cargar_iconos()
        fuente_grande = tkfont.Font(family="Helvetica", size=13, weight="normal")
        menubar_frame = ttk.Frame(app)
        menubar_frame.pack(side="top", fill="x")

        # Seguridad
        seguridad_menu_btn = ttk.Menubutton(menubar_frame, cursor="hand2", text="Seguridad", image=app.icon_seguridad, compound="left", bootstyle="secondary")
        seguridad_menu = ttk.Menu(seguridad_menu_btn, tearoff=0, font=fuente_grande)
        seguridad_menu.add_command(label="Usuarios", command=mostrar_manteniemiento_usuario)
        seguridad_menu.add_command(label="Roles", command=mostrar_manteniemiento_rol)    
        seguridad_menu_btn["menu"] = seguridad_menu
        seguridad_menu_btn.pack(side="left", padx=0)
        
        # Servicios
        gestion_menu_btn = ttk.Menubutton(menubar_frame, cursor="hand2", text="Servicios", image=app.icon_servicios, compound="left", bootstyle="secondary")
        gestion_menu = ttk.Menu(gestion_menu_btn, tearoff=0, font=fuente_grande)
        gestion_menu.add_command(label="Ventas")
        gestion_menu.add_command(label="Compras")
        gestion_menu.add_command(label="Mermas")
        gestion_menu.add_command(label="Kardex")
        gestion_menu_btn["menu"] = gestion_menu
        gestion_menu_btn.pack(side="left", padx=0)

        # Gestión
        gestion_menu_btn = ttk.Menubutton(menubar_frame, cursor="hand2", text="Gestión", image=app.icon_mantenimiento, compound="left", bootstyle="secondary")
        gestion_menu = ttk.Menu(gestion_menu_btn, tearoff=0, font=fuente_grande)
        gestion_menu.add_command(label="Productos")
        gestion_menu.add_command(label="Categorías")
        gestion_menu_btn["menu"] = gestion_menu
        gestion_menu_btn.pack(side="left", padx=0)

        # Catálogos
        catalogos_menu_btn = ttk.Menubutton(menubar_frame, cursor="hand2", text="Catálogos", image=app.icon_catalogo, compound="left", bootstyle="secondary")
        catalogos_menu = ttk.Menu(catalogos_menu_btn, tearoff=0, font=fuente_grande)
        catalogos_menu.add_command(label="Unidades de Medida")
        catalogos_menu.add_command(label="Documentos Identidad")
        catalogos_menu.add_command(label="Tipos de Movimientos")
        catalogos_menu_btn["menu"] = catalogos_menu
        catalogos_menu_btn.pack(side="left", padx=0)

        # Cerrar sesión (como botón simple)
        cerrar_btn = ttk.Button(menubar_frame, cursor="hand2", text="Cerrar Sesión", image=app.icon_logout, compound="left", bootstyle="danger", command=mostrar_login)
        cerrar_btn.pack(side="right", padx=5)

    def cargar_iconos():
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        ruta_seguridad = os.path.join(BASE_DIR, "assets", "icons", "seguridad.png")
        ruta_mantenimiento = os.path.join(BASE_DIR, "assets", "icons", "mantenimiento.png")
        ruta_catalogo = os.path.join(BASE_DIR, "assets", "icons", "catalogo.png")
        ruta_logout = os.path.join(BASE_DIR, "assets", "icons", "logout.png")
        ruta_servicios = os.path.join(BASE_DIR, "assets", "icons", "servicios.png")
        app.icon_seguridad = ImageTk.PhotoImage(Image.open(ruta_seguridad).resize((25, 25)))
        app.icon_mantenimiento = ImageTk.PhotoImage(Image.open(ruta_mantenimiento).resize((25, 25)))
        app.icon_catalogo = ImageTk.PhotoImage(Image.open(ruta_catalogo).resize((25, 25)))
        app.icon_logout = ImageTk.PhotoImage(Image.open(ruta_logout).resize((25, 25)))
        app.icon_servicios = ImageTk.PhotoImage(Image.open(ruta_servicios).resize((25, 25)))

    LoginView(app, on_login_success)
    app.mainloop()

if __name__ == "__main__":
    iniciar_app()
