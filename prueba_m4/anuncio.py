from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

#definicion clase abstracta Anuncio
class Anuncio(ABC):
    #atributos de clase
    FORMATO = ""
    SUB_TIPOS = ()# tupla
    #atributos de instancia de clase
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.__alto = alto
        self.__ancho = ancho
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
        
    #getter ancho
    @property
    def ancho(self):
        return self.__ancho
    
    #setter ancho
    @ancho.setter #validacion bajo una condicional 
    def ancho(self, ancho: int):
        if ancho <= 0:
            self.__ancho = 1
        else:
            return self.__ancho
        
    #getter alto
    @property
    def alto(self):
        return self.__alto
    
    #setter alto
    @alto.setter #validacion bajo una condicional 
    def alto(self, alto: int):
        if alto <= 0:
            self.__alto = 1
        else:
            return self.__alto
    
    #getter url_archivo
    @property
    def url_archivo(self):
        return self.__url_archivo
    
    #setter url_archivo
    @url_archivo.setter
    def url_archivo(self, url_archivo: int):
        self.__url_archivo = url_archivo
        
    #getter url_clic
    @property
    def url_clic(self):
        return self.__url_clic
    
    #setter url_clic
    @url_clic.setter
    def url_clic(self, url_clic: int):
        self.__url_clic = url_clic   

    #getter sub_tipo
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    #setter sub_tipo
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo: str):
        if sub_tipo in self.SUB_TIPOS:
            self.__sub_tipo = sub_tipo
        else:
            raise SubTipoInvalidoError(f"El subtipo '{sub_tipo}' no es válido para este anuncio.")
    
    #deficion de metodo estatico
    @staticmethod
    def mostrar_formatos():  
        print(f"FORMATO {Anuncio.FORMATO}:")#imprime formatos disponibles
        for subtipo in Anuncio.SUB_TIPOS:
            print(f"- {subtipo}")#imprime subtipos disponibles
            
    #definicion de metodos abstractos
    @abstractmethod
    def comprimir_anuncio():
        pass
    
    @abstractmethod
    def redimensionar_anuncio():
        pass
    
###############subclass video##################
class Video(Anuncio):
    #atributos de clase
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    
    #valor 1 predeterminado para ancho-alto
    def __init__(self, ancho:1, alto:1, duracion:int):
        self.__ancho = ancho
        self.__alto = alto
        self.__duracion = duracion
    #getter    
    @property
    def duracion(self):
        return self.__duracion
    #setter 
    @duracion.setter
    #validacion bajo una condicional 
    def duracion(self, duracion: int): 
        if duracion <= 0:
            self.__duracion = 5
        else:
            return self.__duracion
        
    #sobreescritura de metodos abstractos
    def comprimir_anuncio(self):
        return "COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN"
    
    def redimensionar_anuncio(self):
        return "RECORTE DE VIDEO NO IMPLEMENTADO AÚN"
    
###################subclass display######################
class Display(Anuncio):
    #atributos de clase
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")
    
    #sobreescritura de metodos abstractos
    def comprimir_anuncio(self):
        return "COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN"
    
    def redimensionar_anuncio(self):
        return "REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN"
    
################subclass social###########################
class Social(Anuncio):
    #atributos de clase
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    
    #sobreescritura de metodos abstractos
    def comprimir_anuncio(self):
        return "COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN"
    
    def redimensionar_anuncio(self):
        return "REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN"




