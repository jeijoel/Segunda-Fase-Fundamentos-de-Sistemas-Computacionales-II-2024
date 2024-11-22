import pygame #importa el módulo python
import time #importa el módulo time

#configuración de pygame
pygame.init() #Inizializa el módulo pygame
pygame.mixer.init() #Inizializa el módulo mixer de pygame


ventana_interfaz = pygame.display.set_mode((1152, 648)) #crea la ventana y le otorga dimensiones
reloj = pygame.time.Clock() # Crea un reloj
reloj.tick() # Inicia el reloj
ejecucion_ventana_interfaz = True #variable para el manejo de la ejecucción de la pantalla

# Define los colores
blanco = (255, 255, 255)
azul = (0, 0, 255)
celeste = (173, 216, 230)
negro = (0, 0, 0)

# Determina el modo seleccionado
color_a_mostrar_boton_un_jugador = azul
color_a_mostrar_boton_dos_jugadores = celeste

# Fuente para el texto utilizado en la interfaz para algunos textos y botones
fuente_letra = pygame.font.Font(None, 36)

# Fuente para el texto utilizado en la interfaz para textos
fuente_letra_t = pygame.font.Font(None, 24)


# Estado de la pantalla (presentación para la pantalla de presentación, inicio para la pantalla de inicio, etc..)
pantalla_actual = "presentación"

tiempo_inactividad = time.time()  # Tiempo de la última actividad

pygame.mixer.music.load("Sonidos/ambience_pinball.mp3")
pygame.mixer.music.play(-1)

# Función para mostrar la pantalla de presentación
def mostrar_pantalla_de_presentacion():


  ventana_interfaz.fill((200, 200, 200))  # Fondo gris


  #Escribe un texto en la pantalla de presentación
  texto_p_presentacion = fuente_letra.render("¡Pinball!", True, negro)
  ventana_interfaz.blit(texto_p_presentacion, (520, 250))

  pygame.display.flip() # Actualiza toda la pantalla

  # Verifica si se desea volver a la pantalla de inicio
  click_raton = pygame.mouse.get_pressed()
  if click_raton[0]:  # Al hacer clic en cualquier parte, regresa a la pantalla de inicio
    print("Dirigiéndose al inicio")

    # Agrega música de fondo a la pantalla de inicio
    pygame.mixer.music.load("Sonidos/music_menu.mp3")
    pygame.mixer.music.play(-1)
    return "inicio"
  else:
    return "presentación"

# Función para mostrar la pantalla de inicio
def mostrar_pantalla_de_inicio():
  global pantalla_actual, tiempo_inactividad
  ventana_interfaz.fill("purple")


  #Escribe un texto en la pantalla de inicio
  texto_p_inicio = fuente_letra.render("¡Pinball!", True, negro)
  ventana_interfaz.blit(texto_p_inicio, (520, 150))
  
  # Define un rectangulo para el boton para acceder a la pantalla Acerca de
  boton_p_acerca_de_rect = pygame.Rect(476, 250, 200, 80)

  # Define un rectangulo para el boton para acceder a la pantalla configuración
  boton_p_configuracion_rect = pygame.Rect(476, 350, 200, 80)

  # Define un rectangulo para el boton para acceder a la pantalla preliminales
  boton_p_preliminales_rect = pygame.Rect(476, 450, 200, 80)

  # Dibuja el botón para acceder a la pantalla Acerca de
  pygame.draw.rect(ventana_interfaz, celeste, boton_p_acerca_de_rect)

  # Dibuja el botón para acceder a la pantalla Acerca de
  pygame.draw.rect(ventana_interfaz, celeste, boton_p_configuracion_rect)

  # Dibuja el botón para acceder a la pantalla Acerca de
  pygame.draw.rect(ventana_interfaz, celeste, boton_p_preliminales_rect)

  # Dibujar el texto del botón
  texto_b_acerca_de = fuente_letra.render("Acerca de", True, negro)
  escribe_texto_b_acerca_de = texto_b_acerca_de.get_rect(center=boton_p_acerca_de_rect.center)
  ventana_interfaz.blit(texto_b_acerca_de, escribe_texto_b_acerca_de)
  
  # Dibujar el texto del botón
  texto_b_configuracion = fuente_letra.render("Configuración", True, negro)
  escribe_texto_b_configuracion = texto_b_configuracion.get_rect(center=boton_p_configuracion_rect.center)
  ventana_interfaz.blit(texto_b_configuracion, escribe_texto_b_configuracion)

  # Dibujar el texto del botón
  texto_b_preliminales = fuente_letra.render("Preliminales", True, negro)
  escribe_texto_b_preliminales = texto_b_preliminales.get_rect(center=boton_p_preliminales_rect.center)
  ventana_interfaz.blit(texto_b_preliminales, escribe_texto_b_preliminales)

  pygame.display.flip() # Actualiza toda la pantalla

  # Obtiene la posición del ratón
  posicion_cursor = pygame.mouse.get_pos()

  # Evento al hacer click iquierdo
  click_raton = pygame.mouse.get_pressed()

  if click_raton[0]:
    if pantalla_actual == "inicio":
      tiempo_inactividad = time.time()  # Reinicia el temporizador al hacer clic
  if pantalla_actual == "inicio":
    tiempo_transcurrido = time.time() - tiempo_inactividad
    if tiempo_transcurrido > 15:  # Si hay inactividad durante más de 15 segundos
      print("Regresando a la pantalla de presentación")
      pygame.mixer.music.load("Sonidos/ambience_pinball.mp3")
      pygame.mixer.music.play(-1)
      tiempo_transcurrido = 0  # Reinicia el temporizador
      tiempo_inactividad = 0  # Reinicia el tiempo de inactividad
      return "presentación"

  # Verifica si el ratón está sobre el botón para acceder a la pantalla Acerca de
  if boton_p_acerca_de_rect.collidepoint(posicion_cursor) and click_raton[0]:
    # Verificar si se hizo clic con el botón izquierdo del ratón en el botón para acceder a la pantalla Acerca de
    print("Cambiando a la pantalla Acerca de")

    # Detiene la música de fondo de la pantalla de inicio
    pygame.mixer.music.stop()
    return "acerca de"
  elif boton_p_configuracion_rect.collidepoint(posicion_cursor) and click_raton[0]:
    # Verifica si se hizo click con el botón izquierdo del ratón en el botón para acceder a la pantalla de configuración
    print("Cambiando a la pantalla  configuración")

    # Detiene la música de fondo de la pantalla de inicio
    pygame.mixer.music.stop()
    return "configuración"
  elif boton_p_preliminales_rect.collidepoint(posicion_cursor) and click_raton[0]:
    # Verifica si se hizo click con el botón izquierdo del ratón en el botón para acceder a la pantalla de preliminares
    print("Cambiando a la pantalla preliminares")

    # Agrega música de fondo a la pantalla de preliminares
    pygame.mixer.music.load("Sonidos/music_scores.mp3")
    pygame.mixer.music.play(-1)
    return "preliminares"
  else:
    return "inicio"

def mostrar_pantalla_de_acerca_de():
  ventana_interfaz.fill(negro)

  #Escribe un texto en la pantalla de Acerca de
  texto_p_acerca_de = fuente_letra.render("Acerca de", True, blanco)
  ventana_interfaz.blit(texto_p_acerca_de, (520, 50))

  texto_desarrolladores = fuente_letra.render("Desarrolladores", True, blanco)
  ventana_interfaz.blit(texto_desarrolladores, (50, 100))

  imagen_johel = pygame.image.load("Imágenes/Johel.jpg")
  imagen_wilson = pygame.image.load("Imágenes/Wilson.jpg")

  ventana_interfaz.blit(imagen_johel, (175, 150))
  ventana_interfaz.blit(imagen_wilson, (455, 150))

  texto_nombre_johel = fuente_letra_t.render("Jeison Johel Picado Picado", True, blanco)
  ventana_interfaz.blit(texto_nombre_johel, (125, 250))

  texto_nombre_wilson = fuente_letra_t.render("Wilson David Vasquez Ugalde", True, blanco)
  ventana_interfaz.blit(texto_nombre_wilson, (390, 250))

  texto_proyecto = fuente_letra.render("Proyecto: Pinball", True, blanco)
  ventana_interfaz.blit(texto_proyecto, (50, 300))

  texto_asignatura = fuente_letra_t.render("Asignatura: Fundamentos de Sistemas Computacionales", True, blanco)
  ventana_interfaz.blit(texto_asignatura, (50, 350))

  texto_carrera = fuente_letra_t.render("Carrera: Ingeniería en Computadores", True, blanco)
  ventana_interfaz.blit(texto_carrera, (50, 370))

  texto_anno = fuente_letra_t.render("Año: 2024", True, blanco)
  ventana_interfaz.blit(texto_anno, (50, 390))

  texto_profesor = fuente_letra_t.render("Profesor: Milton Enrique Villegas Lemus", True, blanco)
  ventana_interfaz.blit(texto_profesor, (50, 410))

  texto_institucion = fuente_letra_t.render("Institución: Tecnológico de Costa Rica", True, blanco)
  ventana_interfaz.blit(texto_institucion, (50, 430))

  texto_pais_de_produccion = fuente_letra_t.render("País de producción: Costa Rica", True, blanco)
  ventana_interfaz.blit(texto_pais_de_produccion, (50, 450))

  texto_version = fuente_letra_t.render("Versión: 1.0", True, blanco)
  ventana_interfaz.blit(texto_version, (50, 520))

  texto_version_pygame = fuente_letra_t.render("Versión de Pygame: 2.6.1", True, blanco)
  ventana_interfaz.blit(texto_version_pygame, (50, 540))

  texto_version_python = fuente_letra_t.render("Versión de Python: 3.13.0", True, blanco)
  ventana_interfaz.blit(texto_version_python, (50, 560))

  texto_version_micropython = fuente_letra_t.render("Versión de MicroPython: v1.24.0", True, blanco)
  ventana_interfaz.blit(texto_version_micropython, (50, 580))


  # Define un rectangulo para el boton para volver a la pantalla de inicio
  boton_p_inicio_rect = pygame.Rect(952, 568, 200, 80)

  # Dibuja el botón para volver a la pantalla de inicio
  pygame.draw.rect(ventana_interfaz, celeste, boton_p_inicio_rect)

  # Dibujar el texto del botón para volver a la pantalla de inicio
  texto_b_volver = fuente_letra.render("Volver", True, negro)
  escribe_texto_b_volver = texto_b_volver.get_rect(center=boton_p_inicio_rect.center)
  ventana_interfaz.blit(texto_b_volver, escribe_texto_b_volver)

  pygame.display.flip() # Actualiza toda la pantalla
  
  # Obtiene la posición del ratón
  posicion_cursor = pygame.mouse.get_pos()

  # Evento al hacer click iquierdo
  click_raton = pygame.mouse.get_pressed()

  # Verifica si el ratón está sobre el botón para volver a la pantalla de inicio
  if boton_p_inicio_rect.collidepoint(posicion_cursor) and click_raton[0]:
    # Verificar si se hizo clic con el botón izquierdo del ratón en el botón para volver a la pantalla de inicio
    print("Cambiando a la pantalla inicio")
    pygame.mixer.music.play()
    return "inicio"
  else:
    return "acerca de"

def mostrar_pantalla_de_como_jugar():
  ventana_interfaz.fill(blanco)

  # Escribe un texto en la pantalla de cómo jugar
  texto_p_como_jugar = fuente_letra.render("Cómo jugar", True, negro)
  ventana_interfaz.blit(texto_p_como_jugar, (430, 100))

  # Define un rectangulo para el boton para volver a la pantalla de configuración
  boton_p_como_jugar_rect = pygame.Rect(952, 568, 200, 80)

  # Dibuja el botón para volver a la pantalla de configuración
  pygame.draw.rect(ventana_interfaz, celeste, boton_p_como_jugar_rect)

  # Dibujar el texto del botón para volver a la pantalla de inicio
  texto_b_volver = fuente_letra.render("Volver", True, negro)
  escribe_texto_b_volver = texto_b_volver.get_rect(center=boton_p_como_jugar_rect.center)
  ventana_interfaz.blit(texto_b_volver, escribe_texto_b_volver)

  # Obtiene la posición del ratón
  posicion_cursor = pygame.mouse.get_pos()

  # Evento al hacer click iquierdo
  click_raton = pygame.mouse.get_pressed()

  pygame.display.flip()

  # Verifica si el ratón está sobre el botón para volver a la pantalla de inicio
  if boton_p_como_jugar_rect.collidepoint(posicion_cursor) and click_raton[0]:
      # Verificar si se hizo clic con el botón izquierdo del ratón en el botón para volver a la pantalla de inicio
      print("Cambiando a la pantalla configuración")
      return "configuración"
  else:
    return "cómo jugar"

def mostrar_pantalla_de_configuracion():
  global color_a_mostrar_boton_un_jugador, color_a_mostrar_boton_dos_jugadores
  ventana_interfaz.fill(blanco)



  #Escribe un texto en la pantalla de configuración
  texto_informacion = fuente_letra.render("Información del Juego", True, negro)
  ventana_interfaz.blit(texto_informacion, (430, 100))

  texto_informacion_juego = fuente_letra_t.render("Este juego recrea una versión del juego de salón electromecánico 'Pinball'.", True, negro)
  ventana_interfaz.blit(texto_informacion_juego, (240, 160))

  texto_como_jugar = fuente_letra_t.render("¿Cómo jugar?", True, negro)
  ventana_interfaz.blit(texto_como_jugar, (240, 185))

  texto_configuracion = fuente_letra.render("Configuración", True, negro)
  ventana_interfaz.blit(texto_configuracion, (480, 250))

  texto_cantidad_jugadores = fuente_letra_t.render("¿Cuántos jugadores van a jugar?", True, negro)
  ventana_interfaz.blit(texto_cantidad_jugadores, (240, 310))

  # Define un rectangulo para el boton para volver a la pantalla de inicio
  boton_p_inicio_rect = pygame.Rect(952, 568, 200, 80)

  # Dibuja el botón para volver a la pantalla de inicio
  pygame.draw.rect(ventana_interfaz, celeste, boton_p_inicio_rect)

  # Dibujar el texto del botón para volver a la pantalla de inicio
  texto_b_volver = fuente_letra.render("Volver", True, negro)
  escribe_texto_b_volver = texto_b_volver.get_rect(center=boton_p_inicio_rect.center)
  ventana_interfaz.blit(texto_b_volver, escribe_texto_b_volver)

  # Define un rectangulo para el botón para ir a la pantalla de cómo jugar
  boton_p_como_jugar_rect = pygame.Rect(355, 180, 30, 20)

  # Dibuja el botón para ir a la pantalla de cómo jugar
  pygame.draw.rect(ventana_interfaz, celeste, boton_p_como_jugar_rect)

  # Dibuja el texto del botón para ir a la pantalla de cómo jugar
  texto_b_como_jugar = fuente_letra_t.render("Ver", True, negro)
  escribe_texto_b_como_jugar = texto_b_como_jugar.get_rect(center=boton_p_como_jugar_rect.center)
  ventana_interfaz.blit(texto_b_como_jugar, escribe_texto_b_como_jugar)

   # Define un rectangulo para el botón 'un jugador' del selector de cantidad de jugadores
  boton_un_jugador_rect = pygame.Rect(520, 300, 150, 40)

  # Dibuja el botón 'un jugador' del selector de cantidad de jugadores
  pygame.draw.rect(ventana_interfaz, color_a_mostrar_boton_un_jugador, boton_un_jugador_rect)

  # Dibuja el texto del botón 'un jugador' del selector de cantidad de jugadores
  texto_b_un_jugador = fuente_letra_t.render("Un jugador", True, negro)
  escribe_texto_b_un_jugador = texto_b_un_jugador.get_rect(center=boton_un_jugador_rect.center)
  ventana_interfaz.blit(texto_b_un_jugador, escribe_texto_b_un_jugador)

   # Define un rectangulo para el botón 'dos jugadores' del selector de cantidad de jugadores
  boton_dos_jugadores_rect = pygame.Rect(695, 300, 150, 40)

  # Dibuja el botón 'dos jugadores' del selector de cantidad de jugadores
  pygame.draw.rect(ventana_interfaz, color_a_mostrar_boton_dos_jugadores, boton_dos_jugadores_rect)

  # Dibuja el texto del botón 'dos jugadores' del selector de cantidad de jugadores
  texto_b_dos_jugadores = fuente_letra_t.render("Dos jugadores", True, negro)
  escribe_texto_b_dos_jugadores = texto_b_dos_jugadores.get_rect(center=boton_dos_jugadores_rect.center)
  ventana_interfaz.blit(texto_b_dos_jugadores, escribe_texto_b_dos_jugadores)
  
  # Obtiene la posición del ratón
  posicion_cursor = pygame.mouse.get_pos()

  # Evento al hacer click iquierdo
  click_raton = pygame.mouse.get_pressed()

  if boton_un_jugador_rect.collidepoint(posicion_cursor) and click_raton[0]:
    print("Un jugador")
    color_a_mostrar_boton_un_jugador = azul
    color_a_mostrar_boton_dos_jugadores = celeste
  elif boton_dos_jugadores_rect.collidepoint(posicion_cursor) and click_raton[0]:
    print("Dos jugadores")
    color_a_mostrar_boton_un_jugador = celeste
    color_a_mostrar_boton_dos_jugadores = azul

  pygame.display.flip()

    

  # Verifica si el ratón está sobre el botón para volver a la pantalla de inicio
  if boton_p_inicio_rect.collidepoint(posicion_cursor) and click_raton[0]:
    # Verificar si se hizo clic con el botón izquierdo del ratón en el botón para volver a la pantalla de inicio
    print("Cambiando a la pantalla inicio")
    pygame.mixer.music.play()
    return "inicio"
  elif boton_p_como_jugar_rect.collidepoint(posicion_cursor) and click_raton[0]:
    # Verificar si se hizo clic con el botón izquierdo del ratón en el botón para ir a la pantalla de cómo jugar
    print("Cambiando a la pantalla cómo jugar")
    return "cómo jugar"
  else:
    return "configuración"

def mostrar_pantalla_de_preliminares():
  ventana_interfaz.fill(blanco)

  # Define un rectangulo para el boton para volver a la pantalla de inicio
  boton_p_inicio_rect = pygame.Rect(952, 568, 200, 80)

  # Dibuja el botón para volver a la pantalla de inicio
  pygame.draw.rect(ventana_interfaz, celeste, boton_p_inicio_rect)

  # Dibujar el texto del botón para volver a la pantalla de inicio
  texto_b_volver = fuente_letra.render("Volver", True, negro)
  escribe_texto_b_volver = texto_b_volver.get_rect(center=boton_p_inicio_rect.center)
  ventana_interfaz.blit(texto_b_volver, escribe_texto_b_volver)

  pygame.display.flip() # Actualiza toda la pantalla
  
  # Obtiene la posición del ratón
  posicion_cursor = pygame.mouse.get_pos()

  # Evento al hacer click iquierdo
  click_raton = pygame.mouse.get_pressed()

  # Verifica si el ratón está sobre el botón para volver a la pantalla de inicio
  if boton_p_inicio_rect.collidepoint(posicion_cursor) and click_raton[0]:
    # Verificar si se hizo clic con el botón izquierdo del ratón en el botón para volver a la pantalla de inicio
    print("Cambiando a la pantalla inicio")
    pygame.mixer.music.load("Sonidos/music_menu.mp3")
    pygame.mixer.music.play(-1)
    return "inicio"
  else:
    return "preliminares"

#Mantiene la ventana de la interfaz en ejecucción
while ejecucion_ventana_interfaz:
  for evento in pygame.event.get(): #bucle para detectar el evento en la ventana (espera el presionar "x" en la ventana)
    if evento.type == pygame.QUIT: #Condición para salir del "for"
      ejecucion_ventana_interfaz = False #cierra la ventana

  # Determina qué pantalla mostrar
  if pantalla_actual == "presentación":
    pantalla_actual = mostrar_pantalla_de_presentacion()
  elif pantalla_actual == "acerca de":
    pantalla_actual = mostrar_pantalla_de_acerca_de()
  elif pantalla_actual == "inicio":
    pantalla_actual = mostrar_pantalla_de_inicio()
  elif pantalla_actual == "configuración":
    pantalla_actual = mostrar_pantalla_de_configuracion()
  elif pantalla_actual == "preliminares":
    pantalla_actual = mostrar_pantalla_de_preliminares()
  elif pantalla_actual == "cómo jugar":
    pantalla_actual = mostrar_pantalla_de_como_jugar()

  # print("Pantalla actual:", pantalla_actual)

pygame.mixer.quit()  # Cierra el mixer de pygame
# Salir de Pygame
pygame.quit()
