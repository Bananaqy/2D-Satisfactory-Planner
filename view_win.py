from pyray import *
from assets import Buildings
from Vector import Vector2

class View_Win():

    def __init__(self):

        self.pos = Vector2(20, 20)
        self.size = Vector2(750, 450)
        self.screen = load_render_texture(int(self.size.x), int(self.size.y))
        self.selected = False

    def draw_selected(self):

        begin_texture_mode(self.screen)
        building = Buildings[self.selected]
        draw_rectangle_v((self.mouse_pos - (building[0] / 2)).v(), building[0].v(), building[1])
        end_texture_mode()

    def clear(self):

        begin_texture_mode(self.screen)
        clear_background(WHITE)
        end_texture_mode()

    def update(self, mouse_pos = Vector2, within = bool):

        self.clear()

        if within:
            self.mouse_pos = mouse_pos - self.pos
            if self.selected:
                self.draw_selected()

    def render(self):

        draw_texture_rec(self.screen.texture, Rectangle(0, 0, self.size.x, -self.size.y), self.pos.v(), WHITE)