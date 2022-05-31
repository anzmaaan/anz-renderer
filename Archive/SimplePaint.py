import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

import math
import numpy as np

pygame.init()

screen_width = 800
screen_height = 800
ortho_top = -400
ortho_bottom = 400
ortho_left = -400
ortho_right = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Creating, saving and loading drawings in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_bottom, ortho_top)


def plot_point():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


def plot_graph():
    glBegin(GL_LINE_STRIP)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(0, 4, 0.005):
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        glVertex2f(px, py)
    glEnd()


def plot_lines():
    for l in points:
        glBegin(GL_LINE_STRIP)
        for coords in l:
            glVertex2f(coords[0], coords[1])
        glEnd()


def save_drawing():
    f = open("drawing.txt", "w")
    f.write(str(len(points)) + "\n")
    for l in points:
        f.write(str(len(l)) + "\n")
        for coords in l:
            f.write(str(coords[0]) + " " + str(coords[1]) + "\n")
    f.close()
    print("Drawing saved.")


def load_drawing():
    f = open("drawing.txt", "r")
    num_of_lines = int(f.readline())
    global points
    global line
    points = []
    for l in range(num_of_lines):
        line = []
        points.append(line)
        num_of_coords = int(f.readline())
        for coord_number in range(num_of_coords):
            px, py = [float(value) for value in next(f).split()]
            line.append((px, py))
            print(str(px) + "," + str(py))
    print("Drawing loaded.")


done = False
init_ortho()
glPointSize(5)
points = []
line = []
mouse_down = False

while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
            elif event.key == pygame.K_s:
                save_drawing()
            elif event.key == pygame.K_l:
                load_drawing()
            elif event.key == pygame.K_SPACE:
                points = []
                print("Canvas cleared.")
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
            line = []
            points.append(line)
        elif event.type == MOUSEBUTTONUP:
            mouse_down = False
        elif event.type == MOUSEMOTION and mouse_down is True:
            p = pygame.mouse.get_pos()
            '''orto_height steht vorne, weil die 
            koordinatensysteme von pygame (0,0 = top left) und opengl (0,0 = bottom left) 
            unterschiedliche ursprünge haben.'''
            line.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                           map_value(0, screen_height, ortho_top, ortho_bottom, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_lines()
    pygame.display.flip()
    pygame.time.wait(2)

pygame.quit()
