class UsuarioRegistroModel:
    def __init__(self, 
                 intUsuarioID,
                 intRolID,
                 strUsuario,
                 strPassword,
                 strNombres,
                 strApellidoPaterno,
                 strApellidoMaterno,
                 intDocumentoIdentidadID,
                 strNumeroDocumento,
                 bitActivo):
        self.intUsuarioID = intUsuarioID
        self.intRolID = intRolID
        self.strUsuario = strUsuario
        self.strPassword = strPassword
        self.strNombres = strNombres
        self.strApellidoPaterno = strApellidoPaterno
        self.strApellidoMaterno = strApellidoMaterno
        self.intDocumentoIdentidadID = intDocumentoIdentidadID
        self.strNumeroDocumento = strNumeroDocumento
        self.bitActivo = bitActivo

