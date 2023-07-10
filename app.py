import os
import datetime 
#para definir el nombre de aplicacion para bloquear 
nombre_aplicacion = "Duoing"
#definir los dias de la semana a bloquear
lunes =  []
#funcion para bloquear la aplicacion
def bloquear_aplicacion():
    os.system(f"adb shell am force-stop {nombre_aplicacion}")
    print("aplicacion bloqueada upps ;)")
# funcion para desbloquear la aplicacion
def desbloquear_aplicacion():
    os.system(f"abd shell monkey -p {nombre_aplicacion -c android.intent.category.LAUNCHER 1}")
    print("Aplicación desbloqueada.} ")
#funcion principal
def main ()
    wile True:
    #obtener el dia actual y la fecha actual
    now = datetime.datetime.now()
    lunes = now.strftime("%A")
    #verificar si es un dia en el que se puede bloquear la aplicacion 
    if lunes in dias_bloqueo:
        bloquear_aplicacion()
    else:
        desbloquear_aplicacion()
    #esperar un minuto antes de volver a vreficar el estado
    time.sleep(60)
if __name__ == "__main__":
    main()    