from usuario import Usuario
from datetime import datetime
import json

lista_usuarios = []

with open ("dia12/revisiondesafio/usuarios.txt") as usuarios:
    #print(usuarios.readline())
    #print(usuarios.readline())
    linea = usuarios.readline()
    while linea:
        try:
            dicc_usuario = json.loads(linea)# tranformando texto a formato json y contenerlo en una variable
            usuario = Usuario(dicc_usuario["nombre"],dicc_usuario["apellido"],dicc_usuario["email"],dicc_usuario["genero"])
            lista_usuarios.append(usuario)
            linea = usuarios.readline()
        except Exception as e:
            with open ("dia12/revisiondesafio/logs/error.log", "a+") as log:
                fecha_hora = datetime.now()
                log.write(f"[{fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
            log.close()
        finally:
            linea = usuarios.readline()
    usuarios.close()
    
print(lista_usuarios)
                
            

    
    
    
    
    
    
    
    