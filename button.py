import pygame


class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        action=None,
        text=None,
        image=None,
        color=(80, 80, 80),
        hover_color=(110, 110, 110),
        text_color=(255, 255, 255),
    ):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)

        self.action = action
        self.text = text

        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color

        self.font = pygame.font.SysFont(None, 36)

        self.image = None
        self.hover_image = None
        self.mask = None

        if image is not None:
            self.image = pygame.transform.smoothscale(
                image,
                self.rect.size,
            ).convert_alpha()

            self.mask = pygame.mask.from_surface(self.image)

            # Po najechaniu na przycisk wyswietlamy jego jasniejsza kopie
            self.hover_image = self.image.copy()

            # Dodaje sporo jasności tylko do nieprzezroczystych pikseli
            brightness = pygame.Surface(
                self.rect.size,
                pygame.SRCALPHA,
            )
            brightness.fill((100, 100, 100, 0))

            self.hover_image.blit(
                brightness,
                (0, 0),
                special_flags=pygame.BLEND_RGB_ADD,
            )

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()

        if not self.rect.collidepoint(mouse_pos):
            return False

        if self.mask is None:
            return True

        local_pos = (
            mouse_pos[0] - self.rect.x,
            mouse_pos[1] - self.rect.y,
        )

        return bool(self.mask.get_at(local_pos))

    def draw(self, screen):
        hovered = self.is_hovered()

        if self.image is not None:
            image = self.hover_image if hovered else self.image
            screen.blit(image, self.rect)
            return

        color = self.hover_color if hovered else self.color

        pygame.draw.rect(
            screen,
            color,
            self.rect,
        )

        if self.text:
            text_surface = self.font.render(
                self.text,
                True,
                self.text_color,
            )

            text_rect = text_surface.get_rect(
                center=self.rect.center,
            )

            screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.is_hovered()
            and self.action is not None
        ):
            self.action()