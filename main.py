from pyray import *
from view_win import View_Win
from display_win import Display_Win
from Vector import Vector2
import math

init_window(1100, 600, "2D Satisfactory Panner")
set_target_fps(120)
view_win = View_Win()
display_win = Display_Win()

def mouse_within(win, mouse_pos = Vector2):

    if win.pos.x < mouse_pos.x and mouse_pos.x < win.pos.x + win.size.x:
        if win.pos.y < mouse_pos.y and mouse_pos.y < win.pos.y + win.size.y:
            return True
    return False

while not window_should_close():

    mouse_pos = get_mouse_position()
    mouse_pos = Vector2(mouse_pos.x, mouse_pos.y)

    if is_mouse_button_pressed(0):
        view_win.selected = "smelter"

    view_win.update(mouse_pos, mouse_within(view_win, mouse_pos))
    display_win.update(mouse_pos, mouse_within(display_win, mouse_pos))

    begin_drawing()
    clear_background(BLACK)

    view_win.render()
    display_win.render()

    draw_fps(20, 20)

    end_drawing()

unload_texture(display_win.screen.texture)
unload_texture(view_win.screen.texture)
close_window()