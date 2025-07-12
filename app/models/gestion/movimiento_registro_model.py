class MovimientoRegistroModel:
    def __init__(self, 
                 intMovimientoID,
                 intTipoMovimientoID,
                 intProductoID,
                 decCantidad,
                 bitActivo):
        self.intMovimientoID = intMovimientoID
        self.intTipoMovimientoID = intTipoMovimientoID
        self.intProductoID = intProductoID
        self.decCantidad = decCantidad
        self.bitActivo = bitActivo

