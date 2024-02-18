import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Gato")

fondo = pygame.image.load('fondo.jpg')
circulo = pygame.image.load('circle.jpg')
equis = pygame.image.load('x.png')

fondo = pygame.transform.scale(fondo, (450, 450))
circulo = pygame.transform.scale(circulo, (125, 125))
equis = pygame.transform.scale(equis, (125, 125))

tablero = [['', '', ''],
           ['', '', ''],
           ['', '', '']]

turno = 'X'
game_over = False
clock = pygame.time.Clock()

def dibujar_tablero():
    screen.blit(fondo, (0, 0))
    for fila in range(3):
        for col in range(3):
            pygame.draw.rect(screen, (255, 255, 255), (50 + col * 150, 50 + fila * 150, 100, 100), 2)
            if tablero[fila][col] == 'O':
                screen.blit(circulo, (50 + col * 150, 50 + fila * 150))
            elif tablero[fila][col] == 'X':
                screen.blit(equis, (50 + col * 150, 50 + fila * 150))

def verificar_ganador():
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != '':
            return fila[0]
    
    # Verificar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] != '':
            return tablero[0][col]
    
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
        return tablero[0][2]
    
    return None

while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            for fila in range(3):
                for col in range(3):
                    if 50 + col * 150 < mouseX < 200 + col * 150 and 50 + fila * 150 < mouseY < 200 + fila * 150:
                        if tablero[fila][col] == '':
                            tablero[fila][col] = turno
                            turno = 'O' if turno == 'X' else 'X'
                            ganador = verificar_ganador()
                            if ganador:
                                print("¡El ganador es:", ganador, "!")
                                game_over = True
    
    dibujar_tablero()
    pygame.display.update()
