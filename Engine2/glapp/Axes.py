from .Mesh import *


class WorldAxes(Mesh):
    def __init__(self, program_id, location):
        vertices = [[-100.0, 0, 0],
                    [100.0, 0, 0],
                    [0, -100.0, 0],
                    [0, 100.0, 0],
                    [0, 0, -100.0],
                    [0, 0, 100.0]]
        colors = [[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]]
        super().__init__(program_id, vertices, colors, GL_LINES, location)
