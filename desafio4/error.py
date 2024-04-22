    
class DimensionError(Exception):
    def __init__(self, mensaje, dimension = None, maximo = None):
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is not None and self.maximo is not None:
            return f"{self.args[0]} (Dimension ingresada: {self.dimension}, Máximo permitido: {self.maximo})"
        elif self.dimension is not None:
            return f"{self.args[0]} (Dimension: {self.dimension})"
        elif self.maximo is not None:
            return f"{self.args[0]} (Máximo: {self.maximo})"
        else:
            return super().__str__()
        
    
