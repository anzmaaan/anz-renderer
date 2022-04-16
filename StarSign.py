import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)


def draw_star(x, y, size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


done = False
init_ortho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    draw_star(153, 149, 20)
    draw_star(208, 141, 5)
    draw_star(268, 121, 5)
    draw_star(351, 124, 5)
    draw_star(411, 124, 20)
    draw_star(418, 149, 5)
    draw_star(457, 364, 5)
    draw_star(468, 404, 20)
    draw_star(299, 228, 5)
    draw_star(235, 203, 10)
    draw_star(178, 176, 5)
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
