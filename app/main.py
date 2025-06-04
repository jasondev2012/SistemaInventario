import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from modules.auth.login_view import LoginView
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
    app.state("zoomed")
    
    def mostrar_login():
        for widget in app.winfo_children():
            widget.destroy()
        LoginView(app, on_login_success)

    def on_login_success():
        # Limpiar la ventana
        for widget in app.winfo_children():
            widget.destroy()

        # Crear barra de menú
        menubar = ttk.Menu(app)

        # Menú "Archivo"
        archivo_menu = ttk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Nueva Entrada")
        archivo_menu.add_command(label="Guardar")
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Cerrar Sesión", command=mostrar_login)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

        # Menú "Inventario"
        inventario_menu = ttk.Menu(menubar, tearoff=0)
        inventario_menu.add_command(label="Ver Productos")
        inventario_menu.add_command(label="Categorías")
        menubar.add_cascade(label="Inventario", menu=inventario_menu)

        # Menú "Ayuda"
        ayuda_menu = ttk.Menu(menubar, tearoff=0)
        ayuda_menu.add_command(label="Acerca de")
        menubar.add_cascade(label="Ayuda", menu=ayuda_menu)

        # Configurar el menú en la ventana
        app.config(menu=menubar)

        # Contenido principal
        ttk.Label(app, text="Bienvenido al sistema de inventario", font=("Helvetica", 16)).pack(pady=60)

    LoginView(app, on_login_success)
    app.mainloop()

if __name__ == "__main__":
    iniciar_app()
