from models.catalogo.unidad_medida_lista_combo_model import UnidadMedidaListaComboModel
from models.catalogo.unidad_medida_lista_model import UnidadMedidaListaModel
from models.catalogo.unidad_medida_registro_model import UnidadMedidaRegistroModel
from db import DataBase
from models.reponse_model import ResponseModel

class UnidadMedidaService:
    @staticmethod
    def listar_combo():
        conn = DataBase.get_connection()
        listado = []
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Catalogo.Usp_UnidadMedida_ListarCombo"
                cursor.execute(query)
                resultado = cursor.fetchall()
                if resultado is not None:
                    listado = [UnidadMedidaListaComboModel(*fila) for fila in resultado]
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
                query = "EXEC Catalogo.Usp_UnidadMedida_Listar"
                cursor.execute(query)
                resultado = cursor.fetchall()
                if resultado is not None:
                    listado = [UnidadMedidaListaModel(*fila) for fila in resultado]
            finally:
                cursor.close()
        finally:
            conn.close()
        return listado
    @staticmethod
    def obtener(intUnidadMedidaID):
        conn = DataBase.get_connection()
        usuario = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Catalogo.Usp_UnidadMedida_Obtener ?"
                cursor.execute(query, (intUnidadMedidaID,))
                resultado = cursor.fetchone()
                if resultado is not None:
                    usuario = UnidadMedidaRegistroModel(*resultado)
            finally:
                cursor.close()
        finally:
            conn.close()
        return usuario
    @staticmethod
    def dar_de_baja(intUnidadMedidaID):
        conn = DataBase.get_connection()
        respuesta = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Catalogo.Usp_UnidadMedida_Eliminar ?"
                cursor.execute(query, (intUnidadMedidaID,))
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
        intUnidadMedidaID,
        strNombre,
        strAbreviatura,
        bitActivo
    ):
        conn = DataBase.get_connection()
        respuesta = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Catalogo.Usp_UnidadMedida_Registrar ?,?,?,?"
                cursor.execute(query, (
                    int(intUnidadMedidaID),
                    strNombre,
                    strAbreviatura,
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
