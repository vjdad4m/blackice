import pygame as pg

from application import Application
from window import Window

class WindowManager:
    def __init__(self, app: Application):
        self.windows = []
        self.current_focus_index = 0
        self.app = app
    
    def register_window(self, window: Window):
        self.windows.append(window)
        # Set focus to new window
        self.current_focus_index = len(self.windows) - 1
    
    def unregister_window(self, window: Window):
        self.windows.remove(window)

    def draw(self):
        for window in self.windows:
            if window.is_visible:
                win_surface = window.render()
                self.app.screen.blit(win_surface, (window.x, window.y))

    def update(self):
        # Get mouse position
        mouse_pos = pg.mouse.get_pos()
        # Get mouse button state
        mouse_pressed = pg.mouse.get_pressed()
        
        # Set focus to uppermost window
        if mouse_pressed[0]:
            for i in reversed(range(len(self.windows))):
                window = self.windows[i]
                if window.is_visible:
                    if window.is_mouse_in(mouse_pos):
                        self.current_focus_index = i
                        break
            else:
                self.current_focus_index = None

        # Move focused window to end of the list
        if self.current_focus_index is not None and self.current_focus_index != len(self.windows) - 1:
            if len(self.windows) > self.current_focus_index:
                self.windows.append(self.windows.pop(self.current_focus_index))
            else:
                self.current_focus_index = len(self.windows) - 1

        # Update windows
        for idx, window in enumerate(self.windows):
            is_current_focus = idx == self.current_focus_index
            window.update(is_focused=is_current_focus)
            # Check if window is closable and if it is focused
            if is_current_focus and window.is_closable:
                # Check if close is clicked
                if mouse_pressed[0]:
                    if window.is_mouse_on_x(mouse_pos):
                        self.unregister_window(window)
                