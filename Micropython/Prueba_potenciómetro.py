from machine import ADC, Pin
import time

# Configuración del potenciómetro en el pin ADC (26, 27 o 28)
pot_pin = ADC(Pin(27))  # Cambia el 26 si estás usando 27 o 28

# Función para mapear el valor del potenciómetro al rango deseado
def mapear_valor(valor, in_min, in_max, out_min, out_max):
    return int((valor - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    pot_value = pot_pin.read_u16()  # Lee el valor del potenciómetro (0 a 65535)

    # Mapea el valor del potenciómetro al rango de 0 a 100 (como control de volumen)
    volumen = mapear_valor(pot_value, 0, 65535, 0, 100)

    print("Valor del potenciómetro:", pot_value)
    print("Volumen:", volumen)

    # Aquí puedes usar el valor 'volumen' para controlar el nivel de sonido en el proyecto
    # Ejemplo: ajustar_volumen(volumen)

    time.sleep(0.1)  # Pausa para evitar lecturas demasiado rápidas43