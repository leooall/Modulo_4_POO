from error import DimensionErrorException
class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
            if not (1 <= ancho <= Foto.MAX):    
                raise DimensionErrorException(f'error: El ancho no puede ser mayor a {Foto.MAX}')  
                self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if not (1 <= alto <= Foto.MAX):    
                raise DimensionErrorException(f'error: El alto no puede ser mayor a {Foto.MAX}', alto, Foto.MAX)  
                self.__alto = alto
            
foto_1 = Foto(2000,2000, "https://...") 
print(foto_1.ancho)  #2000

try:
    foto_1.ancho = 2600  #  setter del ancho  Esto lanzará una excepción
except DimensionErrorException as e:
    print(e)  # error: El ancho no puede ser mayor a 2500