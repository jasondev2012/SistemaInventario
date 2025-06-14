from db import DataBase
from models.seguridad.usuario_sesion_model import UsuarioSesionModel
class AuthService:
    @staticmethod
    def loginUsuario(strUsuario, strPassword):
        usuarioSesion = None
        conn = DataBase.get_connection()
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Seguridad.Usp_Login_Obtener ?, ?"
                cursor.execute(query, (strUsuario, strPassword,))
                
                if cursor.description is not None:
                    resultado = cursor.fetchone()
                    if resultado is not None:
                        usuarioSesion = UsuarioSesionModel(*resultado)
            finally:
                cursor.close()
        finally:
            conn.close()
        return usuarioSesion
