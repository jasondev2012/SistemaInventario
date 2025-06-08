class UsuarioSesionModel:
    def __init__(self, intUsuarioID, strNombresCompletos, strRol):
        self.intUsuarioID = intUsuarioID
        self.strNombresCompletos = strNombresCompletos
        self.strRol = strRol    

    def __str__(self):
        return f"ID: {self.intUsuarioID}, Nombre Completos: {self.strNombresCompletos}, Rol: {self.strRol}"