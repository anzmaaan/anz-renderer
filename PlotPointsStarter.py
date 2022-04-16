import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-500, 500, -400, 400)


def plot_graph():
    glBegin(GL_POINTS)
    glVertex2f(0, 0)
    glEnd()


done = False
init_ortho()
glPointSize(5)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_graph()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
