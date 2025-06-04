from db import DataBase
from models.seguridad.UsuarioSesionModel import UsuarioSesionModel
class AuthService:
    @staticmethod
    def loginUsuario(usuario, p_strPassword):
        usuarioSesion = None
        conn = DataBase.get_connection()
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Seguridad.Usp_Login_Obtener ?"
                cursor.execute(query, (usuario,))
                resultado = cursor.fetchone()
                if resultado != None:
                    intUsuarioID, strPassword = resultado
                    if p_strPassword == strPassword:
                        query = "EXEC Seguridad.Usp_Usuario_Obtener ?"
                        cursor.execute(query, (intUsuarioID,))
                        resultado = cursor.fetchone()
                        usuarioSesion = UsuarioSesionModel(*resultado)

            finally:
                cursor.close()
        finally:
            conn.close()
        return usuarioSesion
    
