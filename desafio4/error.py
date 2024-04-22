    
class DimensionError(Exception):
    def __init__(self, mensaje, dimension = None, maximo = None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        
        if self.mensaje is not None and self.dimension is None and self.maximo is None:
            return super().__str__()
        elif self.dimension is not None and self.maximo is not None:
            return f"{self.mensaje} (Dimension ingresada: {self.dimension}, Máximo permitido: {self.maximo})"
        elif self.dimension is not None:
            return f"{self.mensaje} (Dimension: {self.dimension})"
        elif self.maximo is not None:
            return f"{self.mensaje} (Máximo: {self.maximo})"

