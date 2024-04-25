#se importa el modulo error ademas de datetime para la entrada de argumentos formato YY-MM-DD
from error import LargoExcedidoError 
from datetime import date
from anuncio import Anuncio, Video, Display, Social

#definicion de la class Campania, con parámetros str, de tipo date y una lista
class Campania():
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, info_anuncios: list) -> None:
        #verificación longitud del nombre de la campaña
        if len(nombre) > 250:
            #si la longitud del nombre es mayor que 250 caracteres, se lanza una excepción
            raise LargoExcedidoError("El nombre de la campaña excede los 250 caracteres.")
        #encapsulamiento de los atributos de instancia
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = []
        
        #llamada al metodo privado __crear_anuncios, pasando como argumento el atributo de instancia "info_anuncios""
        self.__crear_anuncios(info_anuncios)
        
    #método privado que crea instancias de la clase Anuncio a partir de la lista info_anuncios y agrega a la lista de anuncios de la campaña (self.__anuncios).
    def __crear_anuncios(self, info_anuncios: list):
        for info_anuncio in info_anuncios:
            anuncio = Anuncio(**info_anuncio)  # Utilizamos el operador ** para pasar los diccionarios como argumentos
            self.__anuncios.append(anuncio)
            

    #metodo sobrecargado
    def __str__(self): #verifica el valor del atributo FORMATO de cada instancia de Anuncio y suma las instancias que coinciden con cada tipo
        cantidad_video = sum(1 for anuncio in self.__anuncios if anuncio.FORMATO == "Video")
        cantidad_display = sum(1 for anuncio in self.__anuncios if anuncio.FORMATO == "Display")
        cantidad_social = sum(1 for anuncio in self.__anuncios if anuncio.FORMATO == "Social")
        #retorna texto con el nombre de la campaña de la instancia actual, y la cantidad de anuncios por cada tipo
        return f"Nombre de la campaña: {self.__nombre}\nAnuncios: {cantidad_video} Video, {cantidad_display} Display, {cantidad_social} Social"
    
    #getter fecha_inicio
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    #setter fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: date):
        self.__fecha_inicio = fecha_inicio
    #getter fecha_termino
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    #setter fecha_termino
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino: date):
        self.__fecha_termino = fecha_termino
        
    #se solicita solamente crear el método getter para el atributo anuncios, SIN crear su setter.
    @property
    def anuncios(self):
        return self.__anuncios    