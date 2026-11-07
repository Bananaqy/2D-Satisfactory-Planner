from pyray import *
from view_win import View_Win
from display_win import Display_Win
import math

init_window(1100, 600, "2D Satisfactory Panner")
view_win = View_Win()
display_win = Display_Win()

def mouse_within(win, mouse_pos = Vector2):

    if win.pos.x < mouse_pos.x and mouse_pos.x < win.pos.x + win.size.x:
        if win.pos.y < mouse_pos.y and mouse_pos.y < win.pos.y + win.size.y:
            return True
    return False

while not window_should_close():

    mouse_pos = get_mouse_position()

    begin_drawing()

    if mouse_within(view_win, mouse_pos):
        view_win.update()
    view_win.render()

    if mouse_within(display_win, mouse_pos):
        display_win.update()
    display_win.render()

    end_drawing()