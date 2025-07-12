from models.catalogo.tipo_movimiento_lista_combo_model import TipoMovimientoListaComboModel
from models.catalogo.tipo_movimiento_lista_model import TipoMovimientoListaModel
from models.catalogo.tipo_movimiento_registro_model import TipoMovimientoRegistroModel
from db import DataBase
from models.reponse_model import ResponseModel

class TipoMovimientoService:
    @staticmethod
    def listar_combo():
        conn = DataBase.get_connection()
        listado = []
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Catalogo.Usp_TipoMovimiento_ListarCombo"
                cursor.execute(query)
                resultado = cursor.fetchall()
                if resultado is not None:
                    listado = [TipoMovimientoListaComboModel(*fila) for fila in resultado]
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
                query = "EXEC Catalogo.Usp_TipoMovimiento_Listar"
                cursor.execute(query)
                resultado = cursor.fetchall()
                if resultado is not None:
                    listado = [TipoMovimientoListaModel(*fila) for fila in resultado]
            finally:
                cursor.close()
        finally:
            conn.close()
        return listado
    @staticmethod
    def obtener(intTipoMovimientoID):
        conn = DataBase.get_connection()
        usuario = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Catalogo.Usp_TipoMovimiento_Obtener ?"
                cursor.execute(query, (intTipoMovimientoID,))
                resultado = cursor.fetchone()
                if resultado is not None:
                    usuario = TipoMovimientoRegistroModel(*resultado)
            finally:
                cursor.close()
        finally:
            conn.close()
        return usuario
    @staticmethod
    def dar_de_baja(intTipoMovimientoID):
        conn = DataBase.get_connection()
        respuesta = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Catalogo.Usp_TipoMovimiento_Eliminar ?"
                cursor.execute(query, (intTipoMovimientoID,))
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
        intTipoMovimientoID,
        strNombre,
        bitActivo
    ):
        conn = DataBase.get_connection()
        respuesta = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Catalogo.Usp_TipoMovimiento_Registrar ?,?,?"
                cursor.execute(query, (
                    int(intTipoMovimientoID),
                    strNombre,
                    bool(bitActivo)
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
