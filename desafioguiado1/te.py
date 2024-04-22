# definicion de la class
class Te():
    expiracion  = 365 # tiempo de expiracion en días
    sabores = ["Té Negro", "Té Verde", "Infusion de Hierbas"] #Lista de los sabores 
    formatos = [300, 500] # Lista de los formatos disponibles por gramos 
    
    #metodos estaticos de la class
    @staticmethod
    def tiempo_recomendacion(): # metodo que retorna el tiempo de preparacion y su recomendacion segun cada té
        te_negro = "El té negro tiene un tiempo de preparación de 3 minutos y se recomienda consumir al desayuno"
        te_verde = "El té verde tiene un tiempo de preparación de 5 minutos y se recomienda consumir al medio día"
        agua_de_hierbas = "La infusion de hierbas tiene un tiempo de preparación de 6 minutos y se recomienda consumir al atardecer"
        return te_negro, te_verde, agua_de_hierbas
    
    #metodo que retorna el precio en int segun formato de té
    @staticmethod
    def precio_segun_formato():
        formato_300gr = 3000
        formato_500gr = 5000
        return int(formato_300gr), int(formato_500gr)
        
        

