import numpy as np
import pygame
from OpenGL.GLU import *
from math import *
from .Transformations import *


class Camera:
    def __init__(self, program_id, w, h):
        self.transformation = identity_mat()
        self.last_mouse = pygame.math.Vector2(0, 0)
        self.mouse_sensitivityX = 0.1
        self.mouse_sensitivityY = 0.1
        self.key_sensitivity = 0.008
        self.projection_mat = self.perspective_mat(60, w/h, 0.01, 10000)

    def perspective_mat(self, angle_of_view, aspect_ratio, near_plane, far_plane):
        a = radians(angle_of_view)
        d = 1.0/tan(a/2)
        r = aspect_ratio
        b = (far_plane + near_plane) / (near_plane - far_plane)
        c = far_plane * near_plane / (near_plane - far_plane)
        return np.array([[d/r, 0, 0, 0],
                        [0, d, 0, 0],
                        [0, 0, b, c],
                        [0, 0, -1, 0]], np.float32)

    def rotate(self, yaw, pitch):
        self.transformation = rotate(self.transformation, yaw, "Y")
        self.transformation = rotate(self.transformation, pitch, "X")

    def update(self, w, h):
        if pygame.mouse.get_visible():
            return
        mouse_pos = pygame.mouse.get_pos()
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)
        pygame.mouse.set_pos(w / 2, h / 2)
        self.last_mouse = pygame.mouse.get_pos()
        self.rotate(mouse_change.x * self.mouse_sensitivityX, mouse_change.y * self.mouse_sensitivityY)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.transformation = translate(self.transformation, 0, 0, self.key_sensitivity)
        if keys[pygame.K_UP]:
            self.transformation = translate(self.transformation, 0, 0, -self.key_sensitivity)
        if keys[pygame.K_RIGHT]:
            self.transformation = translate(self.transformation, self.key_sensitivity, 0, 0)
        if keys[pygame.K_LEFT]:
            self.transformation = translate(self.transformation, -self.key_sensitivity, 0, 0)

        self.look = self.eye + self.forward
        gluLookAt(self.eye.x, self.eye.y, self.eye.z,
                  self.look.x, self.look.y, self.look.z,
                  self.up.x, self.up.y, self.up.z)
