import machine

entradaAB = machine.Pin(18, machine.Pin.OUT)
entradaClock = machine.Pin(19, machine.Pin.OUT)


def apagar():

    global entradaAB, entradaClock

    for i in range(7):
        entradaAB.value(0)
        entradaClock.value(1)
        entradaClock.value(0)


def encender(posicion):

    global entradaAB, entradaClock


    entradaAB.value(1)
    entradaClock.value(1)
    entradaClock.value(0)


    if 0 < posicion and posicion < 6:
        
        if posicion == 5:
            entradaAB.value(1)
            entradaClock.value(1)
            entradaClock.value(0)
        
        for i in range(posicion-1):
            entradaAB.value(0)
            entradaClock.value(1)
            entradaClock.value(0)
    
    else:

        print("Posicion no valida")





    
    
