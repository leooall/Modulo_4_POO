""" 
Tu amigo nuevamente ha solicitado tu ayuda, esta vez, para agregar tres pequeñas mejoras
en el programa ya entregado.
Mejora 1
Necesita que, en el caso de crear un mapper de Pokemon, se solicite además de la URL base
el límite de registros a obtener al consultar por el listado completo, y almacenar este valor en
un atributo de instancia.
Mejora 2
Además, te comunica que su otro amigo (el que hizo la API), solicita que se aplique
encapsulamiento de los atributos, tanto del que ya existía que contenía la URL base, como del
nuevo solicitado que almacena el límite de registros (solo para pokemones).
Mejora 3
Finalmente, te solicita colocar un pequeño mensaje que aparezca en la terminal cada vez que
se solicite el listado de personajes, indicando el listado que se está obteniendo.
"""

"""1 En la clase MonMapper, modificar el constructor de forma tal que la url base se asigne
a un atributo de instancia privado. Agregar también el getter y setter de este atributo."""
class MonMapper():
    def __init__(self, base_url: str) -> None:
        self.__base_url = base_url
    
@property
def base_url(self) -> str:
    return self.__base_url

@base_url.setter
def base_url(self, base_url) -> None:
    self.__base_url = base_url
    
"""2. Sobrescribir el constructor en la clase PokemonMapper, de forma tal que dentro de éste
se haga el llamado al constructor de la clase base, y luego se asigne el límite al atributo
de instancia privado (se dejó con valor por defecto 20, que es el mismo que tiene la
api)"""
class PokemonMapper(MonMapper):
    def __init__(self, base_url: str, limit: int = 20) -> None:
        super().__init__(base_url)
        self.__limit = limit
"""3. en la misma clase, definir la propiedad con getter y setter del atributo de instancia limit."""        
@property
def limit(self):
    return self.__limit

@limit.setter
def limit(self, limit: int = 20):
    self.__limit = limit
        
"""4. Luego, modificar el llamado al listado de todos los pokemones, de forma tal que
incluya el límite de la instancia."""
import requests
def obtener_mon_por_nombre(self, nombre: str) -> dict:
    respuesta = requests.get(
        f"{self.base_url}/{nombre}?limit={self.__limit}"
    )        