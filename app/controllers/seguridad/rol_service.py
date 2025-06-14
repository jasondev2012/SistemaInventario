from db import DataBase
from models.seguridad.rol_lista_combo_model import RolListaComboModel
from models.seguridad.rol_lista_model import RolListaModel
from models.seguridad.rol_registro_model import RolRegistroModel
from models.reponse_model import ResponseModel

class RolService:
    @staticmethod
    def listar_combo():
        conn = DataBase.get_connection()
        listado = []
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Seguridad.Usp_Rol_ListarCombo"
                cursor.execute(query)
                resultado = cursor.fetchall()
                if resultado is not None:
                    listado = [RolListaComboModel(*fila) for fila in resultado]
            finally:
                cursor.close()
        finally:
            conn.close()
        return listado
    @staticmethod
    def listar():
        conn = DataBase.get_connection()
        listado = []
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Seguridad.Usp_Rol_Listar"
                cursor.execute(query)
                resultado = cursor.fetchall()
                if resultado is not None:
                    listado = [RolListaModel(*fila) for fila in resultado]
            finally:
                cursor.close()
        finally:
            conn.close()
        return listado
    @staticmethod
    def obtener(intRolID):
        conn = DataBase.get_connection()
        usuario = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Seguridad.Usp_Rol_Obtener ?"
                cursor.execute(query, (intRolID,))
                resultado = cursor.fetchone()
                if resultado is not None:
                    usuario = RolRegistroModel(*resultado)
            finally:
                cursor.close()
        finally:
            conn.close()
        return usuario
    @staticmethod
    def dar_de_baja(intRolID,intUsuarioSesion):
        conn = DataBase.get_connection()
        respuesta = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Seguridad.Usp_Rol_Eliminar ?, ?"
                cursor.execute(query, (intRolID, intUsuarioSesion,))
                resultado = cursor.fetchone()
                conn.commit()
                if resultado is not None:
                    respuesta = ResponseModel(*resultado)
            finally:
                cursor.close()
        finally:
            conn.close()
        return respuesta
    @staticmethod
    def registrar(
        intRolID,
        strNombre,
        bitActivo,
        intUsuarioSesion
    ):
        conn = DataBase.get_connection()
        respuesta = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Seguridad.Usp_Rol_Registrar ?,?,?,?"
                cursor.execute(query, (
                    int(intRolID),
                    strNombre,
                    bool(bitActivo),
                    int(intUsuarioSesion)
                ))
                resultado = cursor.fetchone()
                conn.commit()
                if resultado is not None:
                    respuesta = ResponseModel(*resultado)
            finally:
                cursor.close()
        finally:
            conn.close()
        return respuesta
