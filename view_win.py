from pyray import *

class View_Win():

    def __init__(self):

        self.pos = Vector2(20, 20)
        self.size = Vector2(750, 450)

    def render(self):

        begin_drawing()
        draw_rectangle_v(self.pos, self.size, WHITE)