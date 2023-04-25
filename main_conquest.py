import sys
import pygame
from settings import Settings
from knight import Knight, Knight_2
from pygame.sprite import Sprite

FPS = 10

class Conquest:
    """overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Conquest")

        self.knight = Knight(self, 'player_1')
        self.knight_2 = Knight(self, 'player_2')

        self.current_army = pygame.sprite.Group(self.knight)
        self.inactive_army = pygame.sprite.Group(self.knight_2)

        self.all_sprites = pygame.sprite.Group(self.knight, self.knight_2)

        self.current_player = self.knight
        self.inactive_player = self.knight_2

        self.game_active = True

    def main_loop(self):
        """Start the main loop for the game."""
        self.clock = pygame.time.Clock()
        while self.game_active:
            self.clock.tick(FPS)
            self.set_current_player()
            self.process_input()
            self.knight.check_hp()
            self.all_sprites.update()

            # Calls update_screen method.
            self.update_screen()

    def set_current_player(self):
        if self.current_player.actions_per_turn == 0:
            # swap current player to inactive player
            aux_player = self.current_player
            self.current_player = self.inactive_player
            self.inactive_player = aux_player
            self.inactive_player.actions_per_turn = 2

            # swap current army to inactive army
            aux_army = self.current_army
            self.current_army = self.inactive_army
            self.inactive_army = aux_army

            # if self.current_player.name == 'player_1':
            #     self.current_player = self.knight_2
            #     self.inactive_player = self. knight
            #     self.knight.actions_per_turn = 2
            # else:
            #     self.current_player = self.knight
            #     self.inactive_player = self.knight_2
            #     self.knight_2.actions_per_turn = 2

    def process_input(self):
        for event in pygame.event.get():
            print(self.current_player.actions_per_turn)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.current_player.K_UP()
                    self.current_player.actions_per_turn -= 1
                    if self.process_collision():
                        self.current_player.collision_UP()

                elif event.key == pygame.K_DOWN:
                    self.current_player.K_DOWN()
                    self.current_player.actions_per_turn -= 1
                    if self.process_collision():
                        self.current_player.collision_DOWN()

                elif event.key == pygame.K_LEFT:
                    self.current_player.K_LEFT()
                    self.current_player.actions_per_turn -= 1
                    if self.process_collision():
                        self.current_player.collision_LEFT()

                elif event.key == pygame.K_RIGHT:
                    self.current_player.K_RIGHT()
                    self.current_player.actions_per_turn -= 1
                    if self.process_collision():
                        self.current_player.collision_RIGHT()

    def process_collision(self):
        collision = pygame.sprite.spritecollide(self.current_player, self.inactive_army, False, pygame.sprite.collide_rect)

        if collision:
            self.inactive_player.HP = self.inactive_player.HP + self.current_player.attack
            print(f"{self.inactive_player.name} HP: {self.inactive_player.HP}")
            return True



           # self.army_1.remove(self.inactive_player)


    def draw_grid(self):
        self.grid_color = (0, 0, 0)

        self.rows = 6
        self.columns = 6

        self.cell_width = 600 / self.columns
        self.cell_height = 600 / self.rows

        for row in range(self.rows):
            for col in range(self.columns):
                x = col * self.cell_width
                y = row * self.cell_height
                pygame.draw.rect(self.screen, self.grid_color,
                                 [x, y, self.cell_width, self.cell_height], 1)

    def get_turn(self, player):
        while player.actions_per_turn > 0:

            if player.actions_per_turn == 0:
                player.actions_per_turn = 2
                return True
        return False

    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.all_sprites.draw(self.screen)

        self.draw_grid()

        # Make most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and then run the game.
    con = Conquest()
    con.main_loop()




