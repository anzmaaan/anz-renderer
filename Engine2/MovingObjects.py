import pygame

from glapp.PyOGLApp import *
import numpy as np
from glapp.Utils import *
from glapp.GraphicsData import *
from glapp.Square import *
from glapp.Triangle import *
from glapp.Axes import *
from glapp.Cube import *
from glapp.LoadMesh import *
from glapp.MovingCube import *


vertex_shader = r'''
#version 330 core

in vec3 position;
in vec3 vertex_color;
uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;
out vec3 color;
void main()
{
    gl_Position = projection_mat * inverse(view_mat) * model_mat * vec4(position,1);
    color = vertex_color;
}
'''

fragment_shader = r'''
#version 330 core

in vec3 color;
out vec4 frag_color;

void main()
{
    frag_color = vec4(color, 1);
}
'''


class MovingObjects(PyOGLApp):

    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.axes = None
        self.moving_cube = None
        self.suzanne1 = None
        self.suzanne2 = None

    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.axes = WorldAxes(self.program_id, pygame.Vector3(0, 0, 0))
        self.moving_cube = Cube(self.program_id, location=pygame.Vector3(2, 1, 2),
                                move_rotation=Rotation(1, pygame.Vector3(0, 1, 0)))
        self.suzanne1 = LoadMesh("D:\\Projekte\\anz-renderer\\Engine2\\models\\Suzanne.obj", self.program_id,
                                location=pygame.Vector3(0, -1, 0),
                                move_rotation=Rotation(1, pygame.Vector3(0, 1, 0)),
                                move_translate=pygame.Vector3(0, 5, 0),
                                move_scale=pygame.Vector3(0.3, .3, .5)
                                )
        # self.suzanne2 = LoadMesh("models\\teapot.obj", self.program_id,
        #                         location=pygame.Vector3(0, -1, 0),
        #                         move_rotation=Rotation(1, pygame.Vector3(0, 1, 0)),
        #                         move_translate=pygame.Vector3(0, 5, 0),
        #                         move_scale=pygame.Vector3(2, 1, 1))
        self.camera = Camera(self.program_id, self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update()
        self.axes.draw()
        self.moving_cube.draw()
        self.suzanne1.draw()


MovingObjects().mainloop()
