from pyray import *

class Display_Win():

    def __init__(self):

        self.pos = Vector2(790, 20)
        self.size = Vector2(290, 560)

    def update(self):

        pass

    def render(self):

        begin_drawing()
        draw_rectangle_v(self.pos, self.size, WHITE)