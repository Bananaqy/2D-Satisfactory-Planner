from pyray import *
from Vector import Vector2

class Display_Win():

    def __init__(self):

        self.pos = Vector2(790, 20)
        self.size = Vector2(290, 560)
        self.screen = load_render_texture(int(self.size.x), int(self.size.y))  

    def clear(self):

        begin_texture_mode(self.screen)
        clear_background(WHITE)
        end_texture_mode()

    def update(self, mouse_pos = Vector2, within = bool):

        self.clear()
        mouse_pos = mouse_pos - self.pos

    def render(self):

        draw_texture_rec(self.screen.texture, Rectangle(0, 0, self.size.x, -self.size.y), self.pos.v(), WHITE)