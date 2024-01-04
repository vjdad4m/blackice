import pygame as pg

class Window:
    def __init__(self, x: int, y: int, width: int, height: int, title: str, border_color: tuple = (0, 0, 0), border_width: int = 5, is_closable: bool = True, is_movable: bool = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.border_color = border_color
        self.border_width = border_width
        self.is_closable = is_closable
        self.is_movable = is_movable
        self.is_moving = False
        # Create window surface
        self.surface = pg.Surface((self.width, self.height))
        self.header = self.create_window_header()
        self.is_visible = True

    def create_window_header(self):
        # Create surface for window contents
        self.header_surface = pg.Surface((self.width, 20))
        self.header_surface.fill((0, 0, 0))
        self.header_surface.set_alpha(220)
        # Render window title
        self.header_text = pg.font.SysFont("Arial", 12).render(self.title, True, (255, 255, 255))
        self.header_text_rect = self.header_text.get_rect()
        self.header_text_rect.center = (self.width / 2, 10)
        self.header_surface.blit(self.header_text, self.header_text_rect)
        # Render red X
        if self.is_closable:
            self.header_x = pg.font.SysFont("Arial", 12).render("X", True, (255, 0, 0))
            self.header_x_rect = self.header_x.get_rect()
            self.header_x_rect.center = (self.width - 10, 10)
            self.header_surface.blit(self.header_x, self.header_x_rect)

    def draw(self, is_focused: bool = False):
        pass

    def update(self, is_focused: bool = False):
        pass

    def render(self, is_focused: bool = False):
        # Create new surface
        new_surface = pg.Surface((self.width + self.border_width * 2, self.height + 20 + self.border_width * 2))
        # Fill border with border color
        new_surface.fill(self.border_color)
        # Fill surface with white
        self.surface.fill((255, 255, 255))
        # Render window contents
        self.draw(is_focused=is_focused)
        # Render header
        new_surface.blit(self.header_surface, (self.border_width, self.border_width))
        # Render window
        new_surface.blit(self.surface, (self.border_width, 20 + self.border_width))
        return new_surface
    
    def is_mouse_in(self, mouse_pos: tuple):
        mouse_x_check =  (mouse_pos[0] >= self.x and mouse_pos[0] <= self.x + self.width + self.border_width * 2)
        mouse_y_check = (mouse_pos[1] >= self.y and mouse_pos[1] <= self.y + self.height + 20 + self.border_width * 2)
        return mouse_x_check and mouse_y_check

    def is_mouse_on_x(self, mouse_pos: tuple):
        if self.is_mouse_in(mouse_pos):
            x_pos = mouse_pos[0] - self.x
            y_pos = mouse_pos[1] - self.y
            if x_pos >= self.width + self.border_width - 20 and x_pos <= self.width + self.border_width and y_pos >= self.border_width and y_pos <= self.border_width + 20:
                return True
        return False

    def is_mouse_on_banner(self, mouse_pos: tuple):
        if self.is_mouse_in(mouse_pos):
            x_pos = mouse_pos[0] - self.x
            y_pos = mouse_pos[1] - self.y
            if x_pos >= self.border_width and x_pos <= self.width + self.border_width and y_pos >= self.border_width and y_pos <= self.border_width + 20:
                return True
        return False
