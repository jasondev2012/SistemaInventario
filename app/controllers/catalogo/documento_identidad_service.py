from models.catalogo.documento_identidad_lista_combo_model import DocumentoIdentidadListaComboModel
from models.catalogo.documento_identidad_lista_model import DocumentoIdentidadListaModel
from models.catalogo.documento_identidad_registro_model import DocumentoIdentidadRegistroModel
from db import DataBase
from models.reponse_model import ResponseModel

class DocumentoIdentidadService:
    @staticmethod
    def listar_combo():
        conn = DataBase.get_connection()
        listado = []
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Catalogo.Usp_DocumentoIdentidad_ListarCombo"
                cursor.execute(query)
                resultado = cursor.fetchall()
                if resultado is not None:
                    listado = [DocumentoIdentidadListaComboModel(*fila) for fila in resultado]
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
                query = "EXEC Catalogo.Usp_DocumentoIdentidad_Listar"
                cursor.execute(query)
                resultado = cursor.fetchall()
                if resultado is not None:
                    listado = [DocumentoIdentidadListaModel(*fila) for fila in resultado]
            finally:
                cursor.close()
        finally:
            conn.close()
        return listado
    @staticmethod
    def obtener(intDocumentoIdentidadID):
        conn = DataBase.get_connection()
        usuario = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Catalogo.Usp_DocumentoIdentidad_Obtener ?"
                cursor.execute(query, (intDocumentoIdentidadID,))
                resultado = cursor.fetchone()
                if resultado is not None:
                    usuario = DocumentoIdentidadRegistroModel(*resultado)
            finally:
                cursor.close()
        finally:
            conn.close()
        return usuario
    @staticmethod
    def dar_de_baja(intDocumentoIdentidadID):
        conn = DataBase.get_connection()
        respuesta = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Catalogo.Usp_DocumentoIdentidad_Eliminar ?"
                cursor.execute(query, (intDocumentoIdentidadID,))
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
        intDocumentoIdentidadID,
        strNombre,
        bitActivo
    ):
        conn = DataBase.get_connection()
        respuesta = None
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Catalogo.Usp_DocumentoIdentidad_Registrar ?,?,?"
                cursor.execute(query, (
                    int(intDocumentoIdentidadID),
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
