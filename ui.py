import pygame as pg

class UIComponent:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_visible = True
        self.surface = pg.Surface((self.width, self.height))
    
    def draw(self):
        pass

    def update(self):
        pass

class TextLabel(UIComponent):
    def __init__(self, x, y, width, height, text, font, color, bg_color = ((255, 255, 255)), centered=False):
        super().__init__(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color
        self.bg_color = bg_color
        self.centered = centered

    def draw(self, centered = False):
        self.surface.fill(self.bg_color)
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        if self.centered:
            text_rect.center = (self.width / 2, self.height / 2)
        else:
            text_rect.topleft = (0, 0)
        self.surface.blit(text_surface, text_rect)

    def update(self):
        pass    
