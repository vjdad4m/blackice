import pygame as pg

class Application:
    def __init__(self, width: int, height: int, window_name: str, fps: int):
        # Initialize pygame
        pg.init()
        pg.display.set_caption(window_name)
        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        self.fps = fps
        self.running = True

    def run(self):
        while self.running:
            self._events()
            self.update()
            self._draw()
            self.clock.tick(self.fps)
        self._quit()

    # Override these methods
    def update(self):
        pass

    def draw(self):
        pass

    def _events(self):
        # Handle events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def _draw(self):
        self.screen.fill((0, 0, 0))
        self.draw()
        pg.display.flip()

    def _quit(self):
        pg.quit()
