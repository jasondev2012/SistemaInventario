from models.gestion.producto_lista_combo_model import ProductoListaComboModel
from db import DataBase

class ProductoService:
    @staticmethod
    def listar_combo():
        conn = DataBase.get_connection()
        listado = []
        try:
            cursor = conn.cursor()
            try:
                query = "EXEC Gestion.Usp_Producto_ListarCombo"
                cursor.execute(query)
                resultado = cursor.fetchall()
                if resultado is not None:
                    listado = [ProductoListaComboModel(*fila) for fila in resultado]
            finally:
                cursor.close()
        finally:
            conn.close()
        return listado
    
