"""
funcion OPEN
file = open(ruta, argumento o modo de apertura)

"""
import os
try:
    log_file = open(os.path.abspath("dia11/logs/error.log"))
    print(log_file)
    #<_io.TextIOWrapper name='C:\\TalentoDigital\\2024\\MODULO_POO\\dia11\\logs\\error.log' mode='r' encoding='cp1252'>
except FileNotFoundError as e:
    print("archivo o directorio no encontrado")
    print(e)#[Errno 2] No such file or directory: 'C:\\TalentoDigital\\2024\\MODULO_POO\\logs\\error.log'

print(type(log_file))
#<class '_io.TextIOWrapper'>

#argumento r --> solo lectura
print("****************READ******************")
log_file2 = open(os.path.abspath("dia11/html/index.html"), "r")
print(log_file2.read()) #-->imprime el archivo html
log_file2.close()
print("****************READLINE******************")
log_file3 = open(os.path.abspath("dia11/html/index.html"), "r")
print(log_file3.readline()) # <!DOCTYPE html> ...trabajar con un for para trabajar linea por linea
log_file3.close()
print("***************READLINES*******************")
log_file4 = open(os.path.abspath("dia11/html/index.html"), "r")
print(log_file4.readlines()) # retorna una LISTA de cada una de las lineas del archivo HTML
log_file4.close()
print("**************WITH********************")
with open(os.path.abspath("dia11/html/index.html"), "r") as archivo:
    #print(archivo) #<_io.TextIOWrapper name='C:\\TalentoDigital\\2024\\MODULO_POO\\dia11\\html\\index.html' mode='r' encoding='cp1252'>
    for linea in archivo:
        #print(linea) #-->imprime el archivo html con saltos de linea respetando los espacios
        print(linea.strip()) #-->imprime el archivo html sin saltos de linea pero mantiene el espacio propio de escritura en el archivo

#ARGUMENTO w --> solo escritura
#la ruta donde se creara el archivo, DEBE EXISTIR DE ANTEMANO SI O SI
print("**************WRITE********************")
log_file5 = open(os.path.abspath("dia11/html/assets/css/style.css"),"w")
log_file5.write("/*ESTO ES OTRO COMENTARIO*/\n") 
log_file5.write("*{\n\tmargin: 0px\n}")#agrega a continuacion
log_file5.close()

print("**************WRITE con TRY y EXCEPT********************")
import time
try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open(f"dia11/logs/{round(time.time())}.log", "w") as log:
        log.write(f"ERROR: {e}")
        
#para hacer uso de r+ siempre debe existir el archivo
#with open(f"dia11/logs/{round(time.time())}.log", "r+") as log:


