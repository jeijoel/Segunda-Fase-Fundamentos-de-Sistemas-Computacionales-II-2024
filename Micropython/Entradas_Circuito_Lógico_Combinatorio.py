import machine

entrada_H = machine.Pin(21, machine.Pin.OUT) # Entrada de habilitación
entrada_A = machine.Pin(20, machine.Pin.OUT)
entrada_B = machine.Pin(19, machine.Pin.OUT)
entrada_C = machine.Pin(18, machine.Pin.OUT)

def menos_3(A, B, C):
  """Función que simula un circuito lógico combinatorio que resta 3 a un número de 3 bits"""
  entrada_H.value(1)
  entrada_A.value(A)
  entrada_A.value(B)
  entrada_A.value(C)

def deshabilitar():
  """Función que deshabilita el circuito"""
  entrada_H.value(0)