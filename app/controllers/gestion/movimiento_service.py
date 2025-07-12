from models.gestion.movimiento_lista_model import MovimientoListaModel
from models.gestion.movimiento_registro_model import MovimientoRegistroModel
from db import DataBase
from models.reponse_model import ResponseModel

class MovimientoService:
    @staticmethod
    def listar():
        conn = DataBase.get_connection()
        listado = []
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Gestion.Usp_Movimiento_Listar"
                cursor.execute(query)
                resultado = cursor.fetchall()
                if resultado is not None:
                    listado = [MovimientoListaModel(*fila) for fila in resultado]
            finally:
                cursor.close()
        finally:
            conn.close()
        return listado
    @staticmethod
    def obtener(intMovimientoID):
        conn = DataBase.get_connection()
        usuario = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Gestion.Usp_Movimiento_Obtener ?"
                cursor.execute(query, (intMovimientoID,))
                resultado = cursor.fetchone()
                if resultado is not None:
                    usuario = MovimientoRegistroModel(*resultado)
            finally:
                cursor.close()
        finally:
            conn.close()
        return usuario
    @staticmethod
    def dar_de_baja(intMovimientoID,intUsuarioSesion):
        conn = DataBase.get_connection()
        respuesta = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Gestion.Usp_Movimiento_Eliminar ?, ?"
                cursor.execute(query, (intMovimientoID,intUsuarioSesion,))
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
        intMovimientoID,
        intTipoMovimientoID,
        intProductoID,
        decCantidad,
        bitActivo,
        intUsuarioSesion
    ):
        conn = DataBase.get_connection()
        respuesta = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Gestion.Usp_Movimiento_Registrar ?,?,?,?,?,?"
                cursor.execute(query, (
                    int(intMovimientoID),
                    int(intTipoMovimientoID),
                    int(intProductoID),
                    float(decCantidad),
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
