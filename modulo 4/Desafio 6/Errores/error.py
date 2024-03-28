class DimensionError(Exception):
    def __init__(self, mensaje="",dimension=None,maximo=None) -> None:
        super().__init__(mensaje)
        self.mensaje=mensaje
        self.dimension=dimension
        self.maximo=maximo
        
    def __str__(self) -> str:
        if self.dimension is not None and self.maximo is not None:
            return f"**Atención:{self.mensaje} debe ser entre 1 y {self.maximo}. Valor ingresado{self.dimensiones}**"
        else:
            return super().__str__

        