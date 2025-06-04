import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from modules.auth.auth_service import AuthService
from PIL import Image, ImageTk

class LoginView(ttk.Frame):
    def __init__(self, master, on_login_success):
        super().__init__(master)
        self.master = master
        self.on_login_success = on_login_success
        self.pack(fill="both", expand=True)

        # === Frame Izquierdo (Login) ===
        frame_login = ttk.Frame(self)
        frame_login.grid(row=0, column=0, sticky=W+E+N+S)
        frame_login.columnconfigure(0, weight=1,)
        frame_login.rowconfigure(0, weight=1)

        # === Frame DERECHO (IMAGEN) ===
        frame_imagen = ttk.Frame(self)
        frame_imagen.grid(row=0, column=1, sticky="nsew")
        frame_imagen.columnconfigure(0, weight=1)
        frame_imagen.rowconfigure(0, weight=1)

        self.frame_login = frame_login
        self.frame_imagen = frame_imagen
        
        self.cargar_configuraciones()

        self.crear_panel_izquierdo()
        self.crear_panel_derecho()
        
    def cargar_configuraciones(self):
        # Frame principal dividido en dos columnas
        self.columnconfigure(0, weight=3)  # 30%
        self.columnconfigure(1, weight=7)  # 70%
        self.rowconfigure(0, weight=1)     # ocupa toda la altura

    def crear_panel_izquierdo(self):

        # Sub-frame centrado dentro del frame izquierdo
        formulario = ttk.Frame(self.frame_login)
        ancho_pantalla = self.master.winfo_screenwidth()
        formulario.grid(row=0, column=0)

        ttk.Label(formulario, text="Usuario:", font=("Segoe UI", 12)).pack(pady=(10, 5), anchor="w")
        self.entry_usuario = ttk.Entry(formulario, width=50)
        self.entry_usuario.pack(pady=5)

        ttk.Label(formulario, text="Contraseña:", font=("Segoe UI", 12)).pack(pady=(15, 5), anchor="w")
        self.entry_contrasena = ttk.Entry(formulario, show="*", width=50)
        self.entry_contrasena.pack(pady=5)

        ttk.Button(formulario, text="Iniciar Sesión", bootstyle=PRIMARY, command=self.iniciar_sesion)\
            .pack(pady=30)
        
    def crear_panel_derecho(self):
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.master.winfo_screenwidth()
        alto_pantalla = self.master.winfo_screenheight()
        # === Frame Derecho (Imagen) ===
        frame_imagen = ttk.Frame(self.frame_imagen)
        frame_imagen.grid(row=0, column=1, sticky="nsew")

        try:
            imagen = Image.open("app/assets/login_image.png")  # Ruta a tu imagen
            imagen = imagen.resize((int(ancho_pantalla * 0.7), alto_pantalla))
            imagen_tk = ImageTk.PhotoImage(imagen)
            ttk.Label(frame_imagen, image=imagen_tk).pack()
            # Necesario mantener una referencia a la imagen
            self.imagen_tk = imagen_tk
        except Exception as e:
            ttk.Label(frame_imagen, text="Imagen no disponible", font=("Segoe UI", 12)).pack(pady=50)

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        if usuario == '' or contrasena == '':
            messagebox.showwarning("Validación", "Debe ingresar un usuario y contraseña")
        else:
            usuarioSesion = AuthService.loginUsuario(usuario, contrasena)
            if usuarioSesion != None:
                self.on_login_success(usuarioSesion)
            else:
                messagebox.showerror("Error", "Credenciales inválidas")
