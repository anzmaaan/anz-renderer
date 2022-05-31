from pygame.locals import *
from Camera import *
import os
from OpenGL.GL import *
from OpenGL.GLU import *


class PyOGLApp:
    def __init__(self, screen_posX, screen_poxY, screen_width, screen_height):
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{screen_posX},{screen_poxY}"
        self.screen_width = screen_width
        self.screen_height = screen_height
        pygame.init()
        pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
        pygame.display.set_caption('Gilfoyle-Carmack Engine - OpenGL in Python')
        self.camera = Camera()

    def draw_world_axes(self):
        glLineWidth(4)
        glBegin(GL_LINES)
        glColor(1, 0, 0)
        glVertex3d(-1000, 0, 0)
        glVertex3d(1000, 0, 0)
        glColor(0, 1, 0)
        glVertex3d(0, -1000, 0)
        glVertex3d(0, 1000, 0)
        glColor(0, 0, 1)
        glVertex3d(0, 0, -1000)
        glVertex3d(0, 0, 1000)
        glEnd()

        # x pos sphere
        sphere = gluNewQuadric()
        glColor(1, 0, 0)
        glPushMatrix()
        glTranslated(1, 0, 0)
        gluSphere(sphere, 0.05, 8, 8)
        glPopMatrix()

        # y pos sphere
        glColor(0, 1, 0)
        glPushMatrix()
        glTranslated(0, 1, 0)
        gluSphere(sphere, 0.05, 8, 8)
        glPopMatrix()

        # z pos sphere
        glColor(0, 0, 1)
        glPushMatrix()
        glTranslated(0, 0, 1)
        gluSphere(sphere, 0.05, 8, 8)
        glPopMatrix()

    def initialise(self):
        pass

    def display(self):
        pass

    def camera_init(self):
        pass

    def mainloop(self):
        done = False
        self.initialise()
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.mouse.set_visible(True)
                        pygame.event.set_grab(False)
                    if event.key == K_SPACE:
                        pygame.mouse.set_visible(False)
                        pygame.event.set_grab(True)
            self.camera_init()
            self.display()
            pygame.display.flip()
            # pygame.time.wait(100)
        pygame.quit()