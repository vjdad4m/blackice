import pygame as pg

from application import Application
from window import Window
from window_manager import WindowManager
from ui import TextLabel

WWIDTH = 800
WHEIGHT = 600
FPS = 60

if __name__ == "__main__":
    app = Application(WWIDTH, WHEIGHT, "Test Application", FPS)
    
    win1 = Window(0, 0, 400, 200, "Test Window - 1", border_color=(0, 255, 0))
    win2 = Window(130, 50, 400, 300, "Test Window - 2", border_color=(0, 0, 255), border_width=10, is_closable=False)
    win3 = Window(250, 350, 150, 300, "Test Window - 3", border_color=(255, 0, 0), border_width=15)

    label = TextLabel(0, 0, 400, 200, "Hello, World!", pg.font.SysFont("Arial", 20), (0, 0, 0), (255, 255, 255), centered=True)

    def win1_draw(is_focused: bool):
        label.draw()
        win1.draw_ui_component(label)

    def win1_update(is_focused: bool):
        pass

    win1.draw = win1_draw
    win1.update = win1_update

    winmngr = WindowManager(app)

    winmngr.register_window(win1)
    winmngr.register_window(win2)
    winmngr.register_window(win3)

    def draw():
        winmngr.draw()

    def update():
        winmngr.update()

    app.draw = draw
    app.update = update
    app.run()
