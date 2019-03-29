# Autor: Juan Carlos Flores García A01376511. Grupo 02.

# Programa que crea figuras al dibujar círculos, usando ecuaciones para que sean similares a las de un espirógrafo.


import pygame   # Librería de pygame
import math
import random


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO = (0, 0, 0)


# Esta función genera colores aleatorios.
def color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# Esta función utiliza las ecuaciones necesarias para dibujar la figura.
def dibujarCirculos(ventana, r, variableR, l):
    k = (r / variableR)
    anguloFormula = ((1 - k) / k)
    periodoCirculo = r // math.gcd(r, variableR)
    periodoCompleto = periodoCirculo * 360

    for angulo in range(0, periodoCompleto + 1, 1):
        valorAngulo = math.radians(angulo)
        x = int(variableR * ((1 - k) * (math.cos(valorAngulo)) + l * k * math.cos(valorAngulo * anguloFormula)))
        y = int(variableR * ((1 - k) * (math.sin(valorAngulo)) - l * k * math.sin(valorAngulo * anguloFormula)))
        pygame.draw.circle(ventana, color(), (x + ANCHO // 2, ALTO // 2 - y), 1)


# Esta función abre una ventana y dibuja la figura usando los parámatros recibidos y la función dibujarCirculos.
def dibujar(r, variableR, l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)
        dibujarCirculos(ventana, r, variableR, l)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
    pygame.quit()


# Función principal en la que se piden los valores de las variables al usuario y las envía como parámetros a dibujar().
def main():
    r = int(input("Teclea el valor de r: "))
    variableR = int(input("Teclea el valor de R: "))
    l = float(input("Teclea el valor de l: "))
    dibujar(r, variableR, l)


# Llamada a la función main.
main()
