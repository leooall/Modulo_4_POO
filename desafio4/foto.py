from error import DimensionError
class Foto():
    MAX = 2500
    
    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho 
        self.__alto = alto 
        self.ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        try:
            if ancho < 1 or ancho > Foto.MAX:
                raise DimensionError("El valor del ancho no es válido", dimension=ancho, maximo=Foto.MAX)
        except DimensionError as e:
            print("Error:: Ancho no permitido", e)
        self.__ancho = ancho
        
    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        self.__alto = alto
        try:
            if alto < 1 or alto > Foto.MAX:
                raise DimensionError("El valor del alto no es válido", dimension=alto, maximo=Foto.MAX)
        except DimensionError as e:
            print("Error:: Alto no permitido", e)
        


if __name__ == "__main__":
    foto = Foto(2500, 2500, "ruta")
    
    #intento de modificacion fuera de parametros permitidos
    foto.ancho = 3000