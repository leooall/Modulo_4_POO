from datetime import datetime

try:
    now = datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open("dia11/logs/error.log", "a+") as log:
        log.seek(0)#posicionate al principio
        print(log.read())
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        log.seek(3)#posicion
        print(log.read(40))#cantidad de bytes a imprimir