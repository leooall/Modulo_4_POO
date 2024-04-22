from pelota import Pelota
from medicamentos import Medicamento

#INSTANCIA de clase
pelota_de_andy = Pelota() #Instancia de la clase Pelota()
print(pelota_de_andy.forma)

print(Pelota.crear_rebote) #invocacion a metodo ESTATICO

#INSTANCIA class Medicamento
paracetamol = Medicamento()
print(paracetamol.IVA)#se imprime el atributo IVA
print(paracetamol.descuento)#se imprime el atributo descto

aspirina = Medicamento()
print(aspirina.IVA)#se imprime el atributo IVA
print(aspirina.descuento)#se imprime el atributo descto
