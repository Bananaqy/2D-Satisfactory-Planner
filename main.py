from pyray import *
from view_win import View_Win
from display_win import Display_Win
import math

init_window(1100, 600, "2D Satisfactory Panner")
view_win = View_Win()
display_win = Display_Win()

while not window_should_close():

    begin_drawing()
    view_win.render()
    display_win.render()
    end_drawing()