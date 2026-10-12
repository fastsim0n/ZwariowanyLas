import pygame
import sys

from button import Button
from mini_games.catch_hedgehog import CatchHedgehogMiniGame


class Game:
    def __init__(self):
        pygame.init()

        self.WIDTH = 1280 # Wysokosc i szerokosc ekranu (w przyszlosci mozna dodac ustawienia i tam to zmieniac)
        self.HEIGHT = 720

        self.screen = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT)
        )

        pygame.display.set_caption("Zwariowany Las")

        self.clock = pygame.time.Clock()

        self.buttons = [ # Przyciski widoczne na ekranie
            Button(
                x=self.WIDTH//3,
                y=self.HEIGHT//2,
                width=300,
                height=80,
                image=pygame.image.load("assets/hedgehog.png").convert_alpha(), # Przycisk może wyświetlac tekst lub zdjęcie (patrz niżej)
                action=self.start_catch_hedgehog_minigame # Funkcja którą wywołuje dany przycisk
            ),

            Button(
                x=self.WIDTH // 3 * 2,
                y=self.HEIGHT // 2,
                width=300,
                height=80,
                color=(200, 0, 0),
                hover_color=(0, 200, 0),
                text_color=(0, 0, 0),
                text="Wyjdz z gry",
                action=self.quit_game
            )
        ]

        self.running = True # Gra działa w pętli tak długo jak zmienna running jest True

    def start_catch_hedgehog_minigame(self): # Przykładowa funkcja startu minigry
        start_catch_hedgehog_minigame = CatchHedgehogMiniGame()
        start_catch_hedgehog_minigame.run()

    def quit_game(self):
        self.running = False

    def run(self):
        while self.running:
            for event in pygame.event.get(): # Eventy w PyGame to wszystkie zdarzenia w stylu kliknięcie myszki / klawiatury

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

                for button in self.buttons:
                    button.handle_event(event)

            self.screen.fill((0, 150, 30)) # Tło głównego okna

            for button in self.buttons:
                button.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60) # Ogracznienie do 60FPS

        pygame.quit()
        sys.exit()