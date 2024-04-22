class Pelota:
    forma = "redondeada"
    #metodo constructor
    """
    def  __init__(self):
        self.color = "blanco"
        self.tamanio = 10
        self.material = "plastico"
        print("¡Se ha creado una pelota!")
    """
    def  __init__(self, color: str, tamanio: int, material: str): # se crean atributos con tipo de entrada de valores
        self.color = color # parametro color se guarda en atributo self.color de la clase
        self.tamanio = tamanio
        self.material = material
        print("¡Se ha creado una pelota!")

    @property
    def color_y_material(self):
        return f"Pelota {self.color} de {self.material}"
    
    @property
    def colores(self):
        return self.color
    
    @colores.setter
    def colores(self, color: str):
        self.color = color if color != ""  else "blanco"

    def getColor(self):
        return self.color

    def setColor(self, value):
        self.color = value

    #sobrecarga-> modificar el comportamiento del metodo
    def __str__(self):
        return f"forma: {self.forma}, color: {self.color}, material: {self.material} "