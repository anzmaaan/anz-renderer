from OpenGL.GL import *
import pygame


class Mesh:
    def __init__(self):
        self.vertices = [(0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5)]
        self.triangles = [0, 2, 3, 0, 3, 1]
        self.draw_type = GL_LINE_LOOP

    def draw(self, line_width=1, viewport_color=(1, 1, 1)):
        for t in range(0, len(self.triangles), 3):
            glLineWidth(line_width)
            glColor(viewport_color)
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
