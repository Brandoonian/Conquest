import pygame
from pygame.sprite import Sprite

class Knight(Sprite):
    """ A class to manage the knight character."""

    def __init__(self, con_game, name):
        """Initialize the knight and set it's starting position."""
        super().__init__()
        self.name = name
        self.HP = 100
        self.attack = -100

        self.screen = con_game.screen
        self.screen_rect = con_game.screen.get_rect()
        # Load knight image and get it's rect.
        self.image = pygame.image.load('images\KNIGHT_FIGURE.bmp')
        self.resized_image = pygame.transform.scale(self.image, (90, 100))
        self.rect = self.resized_image.get_rect()

        self.actions_per_turn = 2


        if name == 'player_1':
            self.range_color = (0, 255, 0)
            self.rect.bottomleft = self.screen_rect.bottomleft
            self.attack_range = pygame.Rect((self.rect.left - 100), (self.rect.top - 100), 300, 300)
        else:
            self.range_color = (255, 0, 0)
            self.rect.topright = self.screen_rect.topright
            self.attack_range = pygame.Rect((self.rect.left - 100), (self.rect.top - 100), 300, 300)

    def update(self):
        self.blitme()
        self.draw_range()
        self.check_hp()

    def check_hp(self):
        if self.HP <= 0:
            self.kill()

    def blitme(self):
        """Draw the knight at its start"""
        self.screen.blit(self.image, self.rect)

    def draw_range(self):
        pygame.draw.rect(self.screen, self.range_color,
                         self.attack_range, 2)

    def K_UP(self):
        self.rect.y -= 100
        self.attack_range.y -= 100

    def collision_UP(self):
        self.rect.y += 100
        self.attack_range.y += 100

    def K_DOWN(self):
        self.rect.y += 100
        self.attack_range.y += 100

    def collision_DOWN(self):
        self.rect.y -= 100
        self.attack_range.y -= 100

    def K_LEFT(self):
        self.rect.x -= 100
        self.attack_range.x -= 100

    def collision_LEFT(self):
        self.rect.x += 100
        self.attack_range.x += 100

    def K_RIGHT(self):
        self.rect.x += 100
        self.attack_range.x += 100

    def collision_RIGHT(self):
        self.rect.x -= 100
        self.attack_range.x -= 100

class Knight_2(Knight,Sprite):
    def __init__(self, con_game):
        super().__init__(con_game)

        # Start enemy at the top right of the screen.




        self.range_color = (255, 0, 0)