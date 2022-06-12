from .Mesh import *


class Triangle(Mesh):
    def __init__(self, program_id, location):
        vertices = [[0.0, 0.5, -1.0],
                    [0.5, -0.5, -1.0],
                    [-0.5, -0.5, -1.0]]
        colors = [[1, 0, 0], [1, 1, 0], [0, 1, 1]]
        super().__init__(program_id, vertices, colors, GL_TRIANGLES, location)
