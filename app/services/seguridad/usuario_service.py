from db import DataBase
from models.seguridad.usuario_lista_model import UsuarioListaModel
from models.seguridad.usuario_registro_model import UsuarioRegistroModel
from models.reponse_model import ResponseModel

class UsuarioService:
    @staticmethod
    def listar():
        conn = DataBase.get_connection()
        listado = []
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Seguridad.Usp_Usuario_Listar"
                cursor.execute(query)
                resultado = cursor.fetchall()
                if resultado is not None:
                    listado = [UsuarioListaModel(*fila) for fila in resultado]
            finally:
                cursor.close()
        finally:
            conn.close()
        return listado
    @staticmethod
    def obtener(intUsuarioID):
        conn = DataBase.get_connection()
        usuario = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Seguridad.Usp_Usuario_Obtener ?"
                cursor.execute(query, (intUsuarioID,))
                resultado = cursor.fetchone()
                if resultado is not None:
                    usuario = UsuarioRegistroModel(*resultado)
            finally:
                cursor.close()
        finally:
            conn.close()
        return usuario
    @staticmethod
    def registrar(
        intUsuarioID,
        intRolID,
        strUsuario,
        strPassword,
        strNombres,
        strApellidoPaterno,
        strApellidoMaterno,
        intDocumentoIdentidadID,
        strNumeroDocumento,
        bitActivo,
        intUsuarioSesion
    ):
        conn = DataBase.get_connection()
        usuario = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Seguridad.Usp_Usuario_Registrar ?,?,?,?,?,?,?,?,?,?,?"
                cursor.execute(query, (
                    int(intUsuarioID),
                    int(intRolID),
                    strUsuario,
                    strPassword,
                    strNombres,
                    strApellidoPaterno,
                    strApellidoMaterno,
                    int(intDocumentoIdentidadID),
                    strNumeroDocumento,
                    bool(bitActivo),
                    int(intUsuarioSesion)
                ))
                resultado = cursor.fetchone()
                conn.commit()
                if resultado is not None:
                    usuario = ResponseModel(*resultado)
            finally:
                cursor.close()
        finally:
            conn.close()
        return usuario
